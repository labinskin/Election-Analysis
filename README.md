# Election Analysis

By: Nicholas Labinski

##### Project Overview

A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

##### Resources Used

- [ ] Data Source: election_results.csv
- [ ] Software: Python 3.7.6, Visual Studio Code

##### Election-Audit Results

- How many votes were cast in this congressional election?
  - Total votes cast: 369,711
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
- Which county had the largest number of votes?
  - County with largest number of votes: Denver
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  - Winner: Diana DeGette
  - Winning Vote Count: 272,892
  - Winning Percentage: 73.8%
 ![](https://github.com/labinskin/Election-Analysis/blob/main/Resources/Election%20Results%20Printed%20to%20Terminal.png)

##### Election-Audit Summary
Election Commission, while this code was used for this congressional race, the code itself has the potential to be used for a broad range of elections, with only some slight modifications. I will primarily be discussing the code below and how some slight modifications to this code would allow it to be used on a broad basis.

![](https://github.com/labinskin/Election-Analysis/blob/main/Resources/Code%20to%20modify.png)

For local elections, we change the variable of counties to local precincts, as we are no longer focused on larger counties, but the specific municipalities with their many different precincts. By doing this, we can not only tally the total votes to declare a winner, as the winning candidate code remains the same, but we would be able to see how each local municipality voted. This has applicability for everything from mayoral races to local school boards. Expanding slightly, this would also be a useful modification for state elections, like state representatives and state senators, as these elections are still smaller and more localized than federal house congressional districts that this audit examined.

Keeping the code the same, it would be useful for federal senate and presidential elections. The basis for this is the code is able to calculate county level outputs, the main grouping for these statewide contests. Statewide data at the county or congressional level would also be useful for presidential primary vote totaling.

The code would need more modification for nationwide contests, say totaling the national raw vote totals for presidential elections (major modifications in variables would be needed to account for the Electoral College). However, by changing county to state and inputting state vote totals, the code would be able to give the vote totals for each presidential candidate for each state.

An interesting modification to U.S. elections proposed by some political scientists, like Lee Drutman, is the idea of multimember districts to reduce the effects of gerrymandering. If U.S. elections were to be changed to have multimember districts, the code I would need to change would be to the winning candidate and winning count code (see the code below). What would need to be added would be extra variables and `if`statments that included the winning percentage or possibly if a candidate attained a certain threshold of votes (say at least 50%). It would be difficult to state exactly how the code would look, without knowing the exact changes and specifications--whether it is rank choice voting or proportional representation voting. Though, in the case of rank choice voting, we can add code to total how many votes a candidate recieved, dropping the lowest ranked candidate, then rerunning, with a nested loop, to add their votes to new candidates. Overall, the code, with some modification, would still be able to calculate the totals, percentages, and declare winners.
![](https://github.com/labinskin/Election-Analysis/blob/main/Resources/Code%20to%20modify%202.png)
