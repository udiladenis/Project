# Function that return the number of teams that we want to input
def get_number_of_teams():
    while True:
        nr = int(input("\nEnter the number of teams: "))
        if nr > 0:
            break
        else:
            print("The minimum number of teams is 2. Try again!")
    return nr


# Assign for each team, some name
def get_team_names(num_teams):
    lst_of_teams = []
    for i in range(1, num_teams+1):
        while True:
            names = input(f"Enter the name of team #{i}: ")
            if len(names.split()) <= 2 and len(names) >= 2:
                lst_of_teams.append(names)
                break
            else:
                print("Team names must have at least 2 characters, try again.")
    return lst_of_teams



def get_number_of_games_played(num_teams):
    while True:
        nr_games = int(input("\nEnter the number of games played by each team: "))
        if nr_games >= num_teams - 1:
            break
        else:
            print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
    return nr_games


def get_team_wins(team_names, games_played):
    lst_of_wins = []
    for i in team_names:
        while True:
            wins = int(input(f"Enter the of wins {i} had : "))
            if 0 <= wins <= games_played:
                lst_of_wins.append(wins)
                break
            elif wins < 0:
                print("The minimum number of wins is 0, try again.")
            else:
                print(f"The maximum number of wins is {games_played}, try again.")
    team_win_zip = zip(team_names, lst_of_wins)
    return (list(team_win_zip))
                

num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)


# Sorted teams
team_wins.sort(key = lambda x: x[1])
sorted_team = [i[0] for i in team_wins]

print("\nGenerating the games to be played in the first round of the tournament...", end = "\n")

current = 0
last = -1

# Printing the games
# HOME = team with the lowest wins
# AWAY = team with the highest wins
for i in range(len(sorted_team)-len(sorted_team)//2):
    print(f"Home: {sorted_team[current]} VS  Away: {sorted_team[last]}")
    current +=1
    last -=1