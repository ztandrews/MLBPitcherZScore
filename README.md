# MLBPitcherZScore
### V. 1.0.0
A Python program that shows how a hitter compares to the mean of a sample of MLB hitters in certain statistics using a Polar Chart
(Also see [this program for MLB Hitters](https://github.com/ztandrews/MLBHitterZScore))

## About
This is a program that will show an MLB Pitchers Z-Score for the following statistics:
- [wOBA Allowed](https://www.mlb.com/glossary/advanced-stats/weighted-on-base-average)
- [xWOBA Allowed](https://www.mlb.com/glossary/statcast/expected-woba)
- [Average Exit Velocity Allowed](https://www.mlb.com/glossary/statcast/exit-velocity)
- Whiff % (Swings and misses / pitches thrown)
- [Hard Hit % Allowed](https://www.mlb.com/glossary/statcast/hard-hit-rate)
- [Barrel % Allowed](https://www.mlb.com/glossary/statcast/hard-hit-rate)
 
For each one of these statistics, I computed the mean and standard deviation of the sample that is being worked with (Qualified MLB Pitchers, meaning they have a certain amount of plate appearences depending on how many games have been played). I then calculate the Z-Score so we can see how they compare to the mean. The Z-Scores are then plotted in a Radar Chart (also called Polar Chart) so we can visualize our Z-Scores. The general rule of thumb is that if the shaded area is larger, the player is better. Note that for wOBA, xWOBA, Avg. Exit Velo., Hard Hit %, and Barrel %, we are taking the inverse of the Z-Score, because for those statistics, the lower the number the better.
 
 
## How to Run
Note - It is reccomended to use the [Spyder IDE](https://www.spyder-ide.org/) to run this as it is great for Data Visualization and Python.
The steps to run the program are:
1. Go to [this link](https://baseballsavant.mlb.com/leaderboard/custom?year=2021&type=pitcher&filter=&sort=7&sortDir=desc&min=q&selections=p_formatted_ip,woba,xwoba,exit_velocity_avg,barrel_batted_rate,hard_hit_percent,whiff_percent,&chart=false&x=woba&y=woba&r=no&chartType=beeswarm)
2. Make sure you have the following columns selected (OPS, wOBA, xwOBA, Avg EV (MPH), Whiff %, Hard Hit %) and make sure Minimum PA is set to 'Q' for all qualified hitters
3. Click the 'Update' button
4. Download the csv and put it in the same directory as this program (NOTE - There is a CSV in this repo named <em>radarstats4.csv</em> that is an example of one. Refer to that to see what it should look like. You can also use that as a test file)
5. Change the file name varaible on line 40 to the name of your file 
6. Change the name of the player you want to visualize on line 42
7. Run and see the plot!

## Extra
Something to be aware of is that these Z-Score numbers don't mean a ton until about the All-Star break. The reason being we need a longer sample period to get an idea of what the league averages look like for every stat, and also it's always a good idea to use a larger sample size when evaluating a single player. That all being said, this program is still fun to use and it is neat to see how players stack up against eachother in terms of these vvisualizations.

## Version Updates
#### Current Version: 1.0.0
- Initial upload
### Previous Version Updates
None
