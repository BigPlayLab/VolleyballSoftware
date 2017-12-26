# Gather Info
        # Team 1
        team1_name = input("Please enter name of Team 1: ") # Team 1 input
        team1 = sb.scoreboard(str(team1_name)) # Create Team 1 Object
        #print(team1_name)
        print("Team 1 is:", team1.get_teamname()) # Confirm this is team 1

        team2_name = input("Please enter name of Team 2: ") # Team 2 input
        team2 = sb.scoreboard(str(team2_name))
        print("Team 2 is:", team2.get_teamname())

        print(
            "Press 1 to select team 1, and 2 to select team 2.",
            "Press p to add a point, and s to add a set",
            "Press c to cancel"
            )
        input_team = input("Choose team:")
        input_scan = input("Test 1:")
        #print("Feedback is:", input_scan)
        
        while(input_scan != 'c'):
            if(input_team == '1'):
                input_scan = input("Make modifications to the score here:")
                if(input_scan == 'p'):
                    team1.add_points()
                    print(str(team1_name),"Sets:", team1.get_sets(), "Points:", team1.get_points())
                if(input_scan == 's'):
                    team1.add_sets()
                    print(str(team1_name),"Sets:", team1.get_sets(), "Points:", team1.get_points())
            if(input_team == '2'):
                input_scan = input("Make modifications to the score here:")
                if(input_scan == 'p'):
                    team2.add_points()
                    print(str(team2_name),"Sets:", team2.get_sets(), "Points:", team2.get_points())
                if(input_scan == 's'):
                    team2.add_sets()
                    print(str(team2_name),"Sets:", team2.get_sets(), "Points:", team2.get_points())
                    
            
                
        
                

