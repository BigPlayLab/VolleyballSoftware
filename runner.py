import scoreboard as sb
import output
import displaybox

# To output wrapped text box: "output.boxPrint(text,20)"

def main():
    if __name__ == "__main__":
        team1_name = input("Enter name of team 1: ")
        team2_name = input("Enter name of team 2: ")

        team1 = sb.scoreboard(team1_name)
        team2 = sb.scoreboard(team2_name)

        #Set to random points
        team1.set_sets(0)
        team1.set_points(0)
        team2.set_sets(0)
        team2.set_points(0)

        # Instructions
        print("Press a to add a point to team 1")
        print("Press s to add a point to team 2")
        print("Press d to add a set to team 1")
        print("Press f to add a set to team 2")
        print("\n")

        # Text Option 1
        '''text = "{}: Sets: {} Points: {} \n {}: Sets: {} Points: {}".format(
            team1.get_teamname(), team1.get_sets(), team1.get_points(),
            team2.get_teamname(), team2.get_sets(), team2.get_points())'''
        
        # Text Option 2
        print("Game is: \n")

        text = "{} vs. {} \n Sets: {} - {} \n Points: {} - {}".format(
                team1.get_teamname(), team2.get_teamname(),
                team1.get_sets(), team2.get_sets(),
                team1.get_points(), team2.get_points())
        output.boxPrint(text,40)

        
        
        add_points = input("Press c to cancel. Otherwise press any key to continue. ")
        while(add_points != 'c'):
            add_points = input("")
            if(add_points == 'a'):
               team1.add_points()
               text = "{} vs. {} \n Sets: {} - {} \n Points: {} - {}".format(
                    team1.get_teamname(), team2.get_teamname(),
                    team1.get_sets(), team2.get_sets(),
                    team1.get_points(), team2.get_points())
               output.boxPrint(text,40)
               
            elif(add_points == 's'):
                team2.add_points()
                text = "{} vs. {} \n Sets: {} - {} \n Points: {} - {}".format(
                    team1.get_teamname(), team2.get_teamname(),
                    team1.get_sets(), team2.get_sets(),
                    team1.get_points(), team2.get_points())
                output.boxPrint(text,40)
                
            elif(add_points == 'd'):
                team1.add_sets()
                text = "{} vs. {} \n Sets: {} - {} \n Points: {} - {}".format(
                    team1.get_teamname(), team2.get_teamname(),
                    team1.get_sets(), team2.get_sets(),
                    team1.get_points(), team2.get_points())
                output.boxPrint(text,40)
                
            elif(add_points == 'f'):
                team2.add_sets()
                text = "{} vs. {} \n Sets: {} - {} \n Points: {} - {}".format(
                    team1.get_teamname(), team2.get_teamname(),
                    team1.get_sets(), team2.get_sets(),
                    team1.get_points(), team2.get_points())
                output.boxPrint(text,40)
            elif(add_points == 'r'):
                team1.reset_all()
                team2.reset_all()
                text = "{} vs. {} \n Sets: {} - {} \n Points: {} - {}".format(
                    team1.get_teamname(), team2.get_teamname(),
                    team1.get_sets(), team2.get_sets(),
                    team1.get_points(), team2.get_points())
                output.boxPrint(text,40)
            
        print("Program cancelled.")
               
        
        print("Passed Test")
    
main()
