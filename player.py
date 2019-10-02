class Player():
    def __init__(self, team):
        #set team and teamName
        self.team = team
        if team == "w":
            self.teamName = "WHITE"
        else:
            self.teamName = "BLACK"

        #ask name
        print("Insert a nickname for the " + self.teamName + "'S player:")
        while True:
            name = input()
            if name != "" and name != " ":
                self.name = name
                break
            else:
                print("Please, insert a valid name")
        
        #set oppsite team
        if (team == "w"):
            self.opTeam = "b"
        else:
            self.opTeam = "w"