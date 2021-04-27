"""
@auth: ztandrews

Create a Radar chart that plots an MLLB pitchers Z-Scores for certain statistics.
The visualization will give us a good idea of how the hitter comaprees to the average MLB hitter.

The stats we will be using are:
    - wOBA
    - xwOBA
    - Whiff%
    - Hard Hit %
    - Barrel %
    - Avg Exit Velo

STEPS TO RUN
1. Get the stats from a csv from this link:
    https://baseballsavant.mlb.com/leaderboard/custom?year=
    2021&type=pitcher&filter=&sort=5&sortDir=asc&min=75&
    selections=p_formatted_ip,woba,xwoba,exit_velocity_avg,
    barrel_batted_rate,hard_hit_percent,whiff_percent,
    &chart=false&x=woba&y=woba&r=no&chartType=beeswarm
    
    Make sure Qualified pitchers is selected and press 'Download CSV'

2. Once the file is downlaoded, put it in the same directory as this code
3. Change the file name variable on line 40 (rigth after import modules) to match the name of your csv. Make sure to include .csv extension
4. Change the name of the player on line 42 (also right after import modules)
5. Run the code!
"""

#Import modules
import pandas as pd
import matplotlib.pyplot as plt
from math import pi


#Enter the name of the file you downloaded from Baseball Savant
fileName = '26.csv'
#Change this to get the player's data that we want to chart
playerToChart = 'Tyler Glasnow'

#Read CSV file
data = pd.read_csv (r'C:/Users/ztand/Desktop/Python/'+fileName)
data['name'] = data[' first_name'] + ' ' + data['last_name']

#Get the means of each column
wobamean = data['woba'].mean()
evamean = data['exit_velocity_avg'].mean()
bbrmean = data['barrel_batted_rate'].mean()
xwobamean = data['xwoba'].mean()
wmean = data['whiff_percent'].mean()
hhpmean = data['hard_hit_percent'].mean()

#Get the standard deviation of each column
wobasd = data['woba'].std()
evasd = data['exit_velocity_avg'].std()
bbrsd = data['barrel_batted_rate'].std()
xwobasd = data['xwoba'].std()
wsd = data['whiff_percent'].std()
hhpsd = data['hard_hit_percent'].std()

#Create z-score columns for each player and each stat
#Z-Score = (observed value - mean of the sample) / standard deviation of the sample
data['woba_zscore'] = -1*((data['woba'] - wobamean) /wobasd)
data['eva_zscore'] = -1*((data['exit_velocity_avg'] - evamean)/evasd)
data['bbr_zscore'] = -1*((data['barrel_batted_rate']- bbrmean)/bbrsd)
data['xwoba_zscore'] = -1*((data['xwoba'] - xwobamean) /xwobasd)
data['whiff_zscore'] = (data['whiff_percent'] - wmean) /wsd
data['hhp_zscore'] = -1*((data['hard_hit_percent'] - hhpmean) /hhpsd)

#Create a column for each player that is a sum of their Z-Scores. This will determine the color of their chart
data['zsc_sum'] = (data['hhp_zscore']+data['whiff_zscore']+data['xwoba_zscore']+data['bbr_zscore']+data['eva_zscore']+data['woba_zscore'] )
zscavg = data['zsc_sum'].mean()

#Get the Z-Scores and other stats from the DataFrame
player = data[data['name'].str.contains(playerToChart)]
whiff = float(player['whiff_zscore'])
woba = float(player['woba_zscore'])
xwoba = float(player['xwoba_zscore'])
eva = float(player['eva_zscore'])
bbr = float(player['bbr_zscore'])
hhp = float(player['hhp_zscore'])
year = str(player['year'])
ip = str(player['p_formatted_ip'])
zum = str(player['zsc_sum'])

stats = ['WHIFF %', 'wOBA', 'xwOBA', 'AVG. EV', 'BARREL %','HARD HIT %']
values = [whiff,woba,xwoba,eva,bbr,hhp]
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 30}
#Style and plot the Polar Chart
zscoresum = (whiff+woba+xwoba+eva+bbr+hhp)
#The color of the chart logic. If the players sum of Z-Scores is more than the mean of the sum of every players Z-Scores, the chart will be blue. If it is less, the chart will be red
if zscoresum < zscavg:
    col='#ff4c4c'
elif zscoresum > zscavg:
    col='#123ed6'
fig = plt.figure(figsize=(25,25))
ax = plt.subplot(polar="True")
N= len(stats)
values+= values[:1]
angles = [n/float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
plt.polar(angles, values,col,marker='.')
plt.fill(angles,values,col,alpha=.3)
plt.xticks(angles[:-1], stats)
ax.set_rlabel_position(30)
plt.yticks([-3,-2,-1,0,1,2,3], color='grey',size=25)
plt.ylim(-3,3)
yearList = year.split(' ')
yearList2 = yearList[4].split('\n')
year = yearList2[0]
ipList = ip.split(' ')
ipList2 = ipList[4].split('\n')
ip = ipList2[0]
plt.title(playerToChart + '\n' + year + '\n' + ip + ' Innings Pitched' + '\nY-Ticks are Z-Score',fontdict=font)
plt.xticks(fontsize='20',fontweight='bold')
plt.show()

