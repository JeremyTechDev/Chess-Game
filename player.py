class Player():
    def __init__(self, team, king):
        #set team and teamName
        self.team = team
        if team == "w":
            self.teamName = "WHITE"
            self.opTeamName = "BLACK"
            self.opTeam = "b"
        else:
            self.teamName = "BLACK"
            self.opTeamName = "WHITE"
            self.opTeam = "w"

        #ask name and set name
        print("Insert a nickname for the " + self.teamName + "'S player:")
        while True:
            name = input()
            if name != "" and name != " ":
                self.name = name #save name
                break
            else:
                print("Invalid name, please try another one.")

        #set player's king by paramether
        self.king = king