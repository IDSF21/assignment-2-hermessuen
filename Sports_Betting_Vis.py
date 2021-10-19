import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def load_data():
    # read data from CSV file

    return pd.read_csv('Data/cleaned_odds.csv', index_col=0)

def convert_to_percentage(odds):
    if odds < 0:
        odds = odds * -1
        return odds / (100 + odds)
    else:
        return 100 / (odds + 100)


def market_vis(df, team, home, year):
    # filters out by a specific team and year

    df = df[df["year"] == year]
    if  not home:
        df = df[df["AwayTeam"] == team]
    else:
        df = df[df["HomeTeam"] == team]

    # determine accuracy of odds makers
    num_correct_spread = 0
    num_over_totals = 0
    num_under_totals = 0
    num_correct_wins = 0
    total_games = len(df)
    for idx, row in df.iterrows():

        #### Find Correct Spread ####
        if row["Favorite"] == "Home":
            spread = row["HomeFinal"] - row["AwayFinal"]
            if home and spread >= row["Spread"]:
                num_correct_spread += 1
            elif not home and spread <= row["Spread"]:
                num_correct_spread += 1
        elif row["Favorite"] == "Away":
            spread = row["AwayFinal"] - row["HomeFinal"]
            if not home and spread >= row["Spread"]:
                num_correct_spread += 1
            elif home and spread <= row["Spread"]:
                num_correct_spread += 1

        if home:
            money_line = row["HomeML"]
            if row["HomeFinal"] > row["AwayFinal"]:
                win = True
            else:
                win = False
        else:
            money_line = row["AwayML"]
            if row["AwayFinal"] > row["HomeFinal"]:
                win = True
            else:
                win = False
        if money_line < 100 and win: # the team is favored to win
            num_correct_wins += 1
        elif money_line > 100 and not win:
            num_correct_wins += 1

        if row["AwayFinal"] + row["HomeFinal"] > row["TotalPoints"]:
            num_over_totals += 1
        else:
            num_under_totals += 1

    # now create the visualization that matters

    x = pd.DataFrame({"Spread": [num_correct_spread, total_games - num_correct_spread],
                      "Win": [num_correct_wins, total_games - num_correct_wins],
                      "Totals": [num_over_totals, num_under_totals]})

    x_totals = pd.DataFrame({"Over": x["Totals"].iloc[0], "Under": x["Totals"].iloc[1]}, index=["Totals Market"])


    x_spread_win = x[["Spread", "Win"]].transpose()
    x_spread_win.columns = ["Vegas Correct", "Vegas Incorrect"]

    return x_spread_win, x_totals, total_games


def run_app():

    odds_master = load_data()
    st.title('Understanding NBA Sports Betting odds')
    st.header('Brief Look at Our Data')
    st.write(odds_master.head(5))

    st.header('When is Vegas Right? When are they wrong?')
    st.caption('Were some sports betting markets better for certain teams and years? Specifically, how often was Vegas '
               'correct when it came to predicting Wins, Spreads, and Totals?')

    team_selection = st.selectbox("Pick a team", ("Cleveland", 'Miami', 'LALakers', 'Toronto', 'Philadelphia',
       'Detroit', 'NewOrleans', 'Chicago', 'Utah', 'Phoenix',
       'LAClippers', 'Portland', 'SanAntonio', 'Charlotte', 'Orlando',
       'Atlanta', 'Boston', 'Minnesota', 'OklahomaCity', 'NewYork',
       'GoldenState', 'Washington', 'Indiana', 'Brooklyn', 'Houston',
       'Dallas', 'Milwaukee', 'Memphis', 'Sacramento', 'Denver'))

    home_selection = st.radio("Home or Away", ("Home", "Away"))
    home = False
    if home_selection == "Home":
        home = True

    year = st.slider('What Year', 2012, 2020, 2012)
    f = plt.figure()
    ax = plt.axes()

    team_data, totals_data, total_games = market_vis(odds_master, team_selection, home, year)

    team_data.plot.bar(ax=ax, color=["g", "r"])
    ax.set_title("{0} : {1}".format(team_selection, home_selection))
    for p in ax.patches:
        ax.annotate(str(round(p.get_height()/total_games, 2)), (p.get_x() * 1.005, p.get_height() * 1.005))

    f2 = plt.figure()
    ax2 = plt.axes()
    totals_data.plot.bar(ax=ax2, color=["g", "r"])

    ax2.set_title("{0} : {1}".format(team_selection, home_selection))
    for p in ax2.patches:
        ax2.annotate(str(round(p.get_height() / total_games, 2)), (p.get_x() * 1.005, p.get_height() * 1.005))

    col1, col2 = st.columns(2)
    col1.pyplot(f)
    col2.pyplot(f2)

    st.subheader("Observations:")
    st.caption("A quick run through of the data makes it clear to betting on the Money Line is generally a bad idea: "
               "Vegas gets it correct the majority of the time. However, for some teams and years, Vegas does a poor job,"
               "for example the Totals Market for the LA Lakers @ Home - they were under 67% of the time in 2018,"
               "and predominantly under in 2019 and 2020! Similarly, Cleveland in 2012 and 2017 beat their spread"
               "the majority of the time")

    st.header('Are there identifiable relationships between the markets?')
    st.caption("NOTE: The money line odds have been converted to percentages for ease of interpretation")

    col3, col4 = st.columns(2)
    x_variable = col3.selectbox("X-Axis Variable:", ("HomeML", "AwayML", "Spread", "TotalPoints"))
    y_variable = col3.selectbox("Y-Axis Variable:", ("HomeML", "AwayML", "Spread", "TotalPoints"))

    # perform the plotting
    f3 = plt.figure()
    ax3 = plt.axes()

    # filter out extreme odds
    odds_master_filtered = odds_master[odds_master["HomeML"] > -1000]
    odds_master_filtered = odds_master_filtered[odds_master_filtered["HomeML"] < 1000]
    odds_master_filtered["HomeML"] = odds_master_filtered["HomeML"].apply(lambda x: convert_to_percentage(x))
    odds_master_filtered["AwayML"] = odds_master_filtered["AwayML"].apply(lambda x: convert_to_percentage(x))
    odds_master_filtered.plot(kind="scatter", x=x_variable, y=y_variable, ax=ax3)
    col4.pyplot(f3)

    st.subheader("Observations Part 2")
    st.caption("Playing around with the x and y axis we start to notice a few interesting relationships."
               "Firstly, the Home and Away Monelylines have a nearly perfect negative linear correlation which"
               "makes sense - they are mutually exclusive outcomes. Additionally, we see that there is NO easy"
               "visual relationship between the totals market and the spread and the money line markets. A strong"
               "team that is favored to win does not mean the odds will indicate a higher or smaller total. Finally,"
               "we see something of an absolute value function when we plot the Spread against the"
               "Moneyline percentages and it becomes clear that whenthe odds are 50/50 for each team winning,"
               "they set the spread at 0. As the odds swing in favor of one team or the other, the spread"
               "increases linearly")




















if __name__ == "__main__":
    run_app()