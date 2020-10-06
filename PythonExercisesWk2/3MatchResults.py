#This program displays a match result of two teams


hometeam_name = input("Home team name? ")

hometeam_score = int(input("Home team score? "))

awayteam_name = input("Away team name? ")

awayteam_score = int(input("Away team score? "))

if hometeam_score > awayteam_score:
    print("Winner: ",hometeam_name)
elif awayteam_score > hometeam_score:
    print("Winner: ",awayteam_name)
elif awayteam_score == hometeam_score:
    print("Draw")
else:
    print("Invalid") 


