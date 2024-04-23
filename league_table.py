import matplotlib as mpl
import matplotlib.patches as patches
from matplotlib import pyplot as plt


# Set matplotlib parameters
mpl.rcParams['figure.dpi'] = 100

# In order to finish this tutorial, we'll create a fresh example
# using sample data

# first, we'll create a new figure and axis
fig, ax = plt.subplots(figsize=(10,10))

# set the number of rows and cols
rows = 20
cols = 10

# set up the axis limits with "spacing" (a bit of padding on each side)
ax.set_ylim(-1, rows + 1)
ax.set_xlim(0, cols + .5)

league_data = [
    {"Team": "Manchester United", "Played": 38, "Won": 28, "Drawn": 5, "Lost": 5, "Goals For": 81, "Goals Against": 20},
    {"Team": "Liverpool", "Played": 38, "Won": 27, "Drawn": 6, "Lost": 5, "Goals For": 82, "Goals Against": 22},
    {"Team": "Chelsea", "Played": 38, "Won": 22, "Drawn": 10, "Lost": 6, "Goals For": 64, "Goals Against": 34},
    {"Team": "Tottenham", "Played": 38, "Won": 18, "Drawn": 8, "Lost": 12, "Goals For": 69, "Goals Against": 40},
    {"Team": "Arsenal", "Played": 38, "Won": 16, "Drawn": 11, "Lost": 11, "Goals For": 58, "Goals Against": 49},
    {"Team": "Manchester", "Played": 38, "Won": 15, "Drawn": 13, "Lost": 10, "Goals For": 61, "Goals Against": 47},
    {"Team": "West Ham", "Played": 38, "Won": 16, "Drawn": 8, "Lost": 14, "Goals For": 60, "Goals Against": 51},
    {"Team": "Leicester", "Played": 38, "Won": 14, "Drawn": 10, "Lost": 14, "Goals For": 56, "Goals Against": 56},
    {"Team": "Everton", "Played": 38, "Won": 13, "Drawn": 10, "Lost": 15, "Goals For": 49, "Goals Against": 58},
    {"Team": "Aston Villa", "Played": 38, "Won": 13, "Drawn": 7, "Lost": 18, "Goals For": 48, "Goals Against": 59},
    {"Team": "Newcastle", "Played": 38, "Won": 10, "Drawn": 9, "Lost": 19, "Goals For": 44, "Goals Against": 60},
    {"Team": "Wolverhampton", "Played": 38, "Won": 10, "Drawn": 13, "Lost": 15, "Goals For": 38, "Goals Against": 49},
    {"Team": "Southampton", "Played": 38, "Won": 9, "Drawn": 14, "Lost": 15, "Goals For": 43, "Goals Against": 50},
    {"Team": "Crystal Palace", "Played": 38, "Won": 9, "Drawn": 14, "Lost": 15, "Goals For": 41, "Goals Against": 50},
    {"Team": "Brentford", "Played": 38, "Won": 7, "Drawn": 14, "Lost": 17, "Goals For": 48, "Goals Against": 63},
    {"Team": "Brighton", "Played": 38, "Won": 7, "Drawn": 12, "Lost": 19, "Goals For": 32, "Goals Against": 57},
    {"Team": "Leeds", "Played": 38, "Won": 9, "Drawn": 11, "Lost": 18, "Goals For": 43, "Goals Against": 79},
    {"Team": "Burnley", "Played": 38, "Won": 7, "Drawn": 14, "Lost": 17, "Goals For": 34, "Goals Against": 54},
    {"Team": "Norwich", "Played": 38, "Won": 5, "Drawn": 7, "Lost": 26, "Goals For": 22, "Goals Against": 88},
    {"Team": "Watford", "Played": 38, "Won": 5, "Drawn": 7, "Lost": 26, "Goals For": 29, "Goals Against": 77}
]



# Plot the data into the table
for row in range(len(league_data)):
    d = league_data[row]

    # Team name column
    ax.text(x=.5, y=row, s=d['Team'], va='center', ha='left', weight='bold')
    # Played column
    ax.text(x=3, y=row, s=d['Played'], va='center', ha='right')
    # Won column
    ax.text(x=4, y=row, s=d['Won'], va='center', ha='right')
    # Drawn column
    ax.text(x=5, y=row, s=d['Drawn'], va='center', ha='right')
    # Lost column
    ax.text(x=6, y=row, s=d['Lost'], va='center', ha='right')
    # Goals For column
    ax.text(x=7, y=row, s=d['Goals For'], va='center', ha='right')
    # Goals Against column
    ax.text(x=8, y=row, s=d['Goals Against'], va='center', ha='right')
    # Goal Difference column
    ax.text(x=9, y=row, s=(d['Goals For'] - d['Goals Against']), va='center', ha='right')
    # Points column
    ax.text(x=10, y=row, s= (d['Won'] * 3) + (d['Drawn'] * 1), va='center', ha='right')

# Add column headers
# plot them at height y=9.75 to decrease the space to the
# first data row (you'll see why later)
ax.text(.5, 19.75, 'Team', weight='bold', ha='left')
ax.text(3, 19.75, 'P', weight='bold', ha='right')
ax.text(4, 19.75, 'W', weight='bold', ha='right')
ax.text(5, 19.75, 'D', weight='bold', ha='right')
ax.text(6, 19.75, 'L', weight='bold', ha='right')
ax.text(7, 19.75, 'GF', weight='bold', ha='right', va='bottom')
ax.text(8, 19.75, 'GA', weight='bold', ha='right', va='bottom')
ax.text(9, 19.75, 'GD', weight='bold', ha='right', va='bottom')
ax.text(10, 19.75, 'Pts', weight='bold', ha='right', va='bottom')

# Next up: formatting!
# let's add some gridlines
for row in range(rows):
    ax.plot([0, cols + 1], [row -.5, row - .5], ls=':', lw='.5', c='grey')

# let's add a main header divider
# remember that we plotted the header row slightly closer to the first data row
ax.plot([0, cols + 1], [19.5, 19.5], lw='.5', c='black')

# highlight the column we are sorting by
# I will use a rectangle patch for this
# this can be a bit fiddly but given our coordinate space we can easily automate this!
# set the starting position (left bottom corner), then set a width and height
# the trick is to set the alpha (transparency) to a low number!
rect = patches.Rectangle((9.5, -.5), .65, 20, lw=1, ec='none', fc='grey', alpha=.2, zorder=-1)
ax.add_patch(rect)

# now the magic piece, hide the axis!
#ax.axis('off')

# We can also add a title to our table
ax.set_title('Premier League Table', loc='left', fontsize=18, weight='bold')
