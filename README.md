### Description of Project
The purpose of this project is to better understand the NBA sports betting market. I am concerned with the three main markets in NBA sports betting: Spreads, Totals and Moneylines. 

1. Spreads: A handicap on how much a team is expected to win by
2. Moneyline: A probabalistic estimate as to which team will win
3. Totals: A prediction of how many total points will be scored (over or under)

Ideally, Oddsmakers provide a 50% win rate for both Spreads and Totals. 

We start by trying to identify possible instances where we might have an "edge" over the given odds by Vegas. Specifically, I want to see if we can find these anomalies in the odds by looking at certain teams, years, and markets. This will help us understand how accurate the odds generally are

The second part of the project is concerned with understanding the relationship **between** markets. For example, do we think that the Spread of a given game should affect the Total for a given game?

### Why this project?
Of course, the goal of any Sports Betting Data Analysis is a (perhaps futile) attempt to find some competitive edge against the sports books. The hope here is that users of this application to generate insights about what teams and years the Oddsmakers had trouble, and perform further anaysis to discover the causes. Additionally, I hope that by understanding the relationship between markets, it will become easier to understand when two related markets are acting strangely so that one might be able to take advantage of a discrepancy in the market


### Rationale for Design Decisions
For the first visualization I chose to use a bar plot with the number of correct Vegas predictions placed right next to the number of incorrect Vegas predictions. I had also considered doing a stacked bar chart, but based on the readings, and my personal experience, it became clear that a stacked bar chart would make it more difficult to compare the Vegas Win and Lose rates. I chose a bar plot over a scatter or boxplot because I had discrete values and I was mostly concerned with the performance of the Vegas odds in aggregate.

The second visualization i chose a scatter plot because we were trying to identify an unknown relationship. I had also considered using a line plot, but quickly realized that since the data had no sequential ordering this did not make sense. Additionally, I had considered visualizations that would track changes of sports betting odds over time, and for this a line plot would have been beneficial. However, I ultimately chose to forego that analysis because a preliminary exploratory data analysis had already revealed that the answers to such questinos were self-explanatory.


### Development Process
This was done as an individual project so all of the work was done by me. The order of the tasks, along with the approximate amount of time it took for the project, are as follows

- Identify a data set (1.5 hours)
- Clean dataset (3 hours)
- Explore dataset (1 hour)
- Come up with actionable questions (2 hour)
- Design Visualizations (2 hour)
- Code visualizations (3 hours)
- Debug, final touches (1 hour)
- Deploy (10 minutes)
- Write up (1 hour)

The aspects that took the most time were cleaning the dataset and actually coding up the visualizations. Since the raw data was in a form that was not exactly amenable to the questions that I wanted to answer, I had to perform a signifcant amount of cleaning. This really took the bulk of the time. I found the development process for this to be at times stratightforward and iterative. For example, the general workflow was linear, but there would be times where I would come up with a possible question and, before building a visualization, I first tried to answer it directly with numbers. Oftentimes I found that those questions did not need a visualization so it pushed me to come up with more interesting ideas 





