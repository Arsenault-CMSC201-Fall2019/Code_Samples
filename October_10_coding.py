# Live coding for October 10
# We will uncomment sections of code as needed
#

# Here are all the NFL Teams that are not the New Orleans Saints
nfl_Teams = ["New England Patriots", "New York Jets", "Miami Dolphins", "Buffalo Bills", "Baltimore Ravens", "Pittsburgh Steelers", "Cleveland Browns", "Cincinnati Bengals", "Jacksonville Jaguars", "Tennessee Titans", "Indianapolis Colts", "Houston Texans", "Kansas City Chiefs",
"Denver Broncos", "Oakland Raiders", "Los Angeles Chargers", "New York Giants", "Philadelphia Eagles", "Washington Redskins", "Dallas Cowboys", "Carolina Panthers", "Atlanta Falcons", "Tampa Bay Buccaneers", "Chicago Bears", "Minnesota Vikings", "Green Bay Packers", "Detroit Lions", "Los Angeles Rams", "San Francisco 49ers", "Seattle Seahawks", "Arizona Cardinals"]

# First define the famous cheer as a constant:
CHEER = "WHO DAT"

# There should be 31 of them; let's check
if len(nfl_Teams != 31):
    print("Error; you missed some teams")
else:
    print ("We have all the teams listed")

# Now let's insert the "CHEER" into the name of each team
# First do it at the end

for team in nfl_Teams:
    team = team + CHEER
    print(team)

# Okay, that seems kind of simple. It's almost cheating
# How about if we put the CHEER in between the city name
# and the team name.
# That is, between "Chicago" and "Bears"

# Look for a blank space, then insert the cheer, then
# finish the string

# do this for each team
for team in nfl_Teams:

# find the last blank space in the team name
# this finds the last blank space because when it finds
# the first blank space it keeps going through the rest
# of the team name. The blank space between "Angeles" and
# "Rams" will overwrite the blank space between "Los" and
# "Angeles"

    for i in range(len(team)):
        if team[i] == ' '  :
            blanks = i

# now build the new string
    our_team = team[:blanks] + CHEER + team[blanks:]

# and print it
    print(our_team)

# what if we wanted to stop at the first blank space and
# insert the cheer between the "New" and the "York";
# between the "Los" and the Angeles"?

# The easiest thing to do would be to use a while loop
for team in nfl_Teams:
    no_blanks_yet = True
    i = 0
    while no_blanks_yet:
        if team[i] == ' ':
            no_blanks_yet = False
            blanks = i
        else:
            i += 1

# note - the above while loop will fail if there is a
# team name without a blank space. If that is a possibility
# we need to insert an error check.

# now build the new string the same as before
    our_team = team[:blanks] + CHEER + team[blanks:]
    print(our_team)

# now suppose you wanted to print out the name of each
# team backwards. First, without the CHEER inserted

# if you wanted to do this with the CHEER inserted,
# you would build the list of "our_team" as above
# Then print each value of "our_team" backwards

# Again, we'll do this for each team in the list

for team in nfl_Teams:

#Using a for each loop first

# define a new string to hold the backward value
    backward_team = ''
    for i in team:
        backward_team = i + backward_team

# Note: this is *NOT* commutative. You have to start
# with i and append backward team. If you do
# backward_team = backward_team + 1 you'll just get the
# team name in regular order

# Now print out the team name backwards
    print(backward_team)

# If you want to do the same thing using a while loop
# instead of a for each loop it would look something
# like this
for team in nfl_Teams:

    backward_team = ''
    team_length = len(team) - 1
    while team_length >= 0:
        backward_team = backward_team + team[team_length]
        team_length = team_length - 1
    print(backward_team)

