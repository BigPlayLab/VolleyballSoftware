import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

class scoreboard():
    """
    Keeps a record of the score for the game.

    Types:
    self.set_counter : int --> max number of sets in a game is 3
    self.point_counter : list --> keeps record of order in which points are scored
        Perhaps consider using a dictionary?
    
    """
    def __init__(self, teamname):
        self.teamname = teamname
        self.set_counter = 0
        self.point_counter = []
# Teamname
    def set_teamname(self, new_name):
        """
        Sets the name of a specific team.
        """
        self.teamname = new_name

    def get_teamname(self):
        """
        Retrieves the name of the team.
        """
        return self.teamname
# Sets
    def set_sets(self, value):
        """
        Takes a parameter to manually change the number of sets
        """
        self.set_counter = value
    
    def add_sets(self):
        """
        Adds a set to a team.
        """
        self.set_counter += 1

    def remove_sets(self):
        """
        Removes a set from a team.
        """
        self.set_counter +- 1

    def get_sets(self):
        """
        Retrieves the number of sets for a particular team.
        """
        return self.set_counter
# Points
    def set_points(self, value):
        """
        Takes a parameter to manually change the number of points
        """
        s = sum(self.point_counter)
        if(s < value):
            while(s != value):
                self.point_counter.append(int(1))
        elif(s > value):
            while(s != value):
                del self.point_counter[-1]
                
    
    def add_points(self):
        """
        Adds a point to a team
        """
        self.point_counter.append(1)
        print("{}".format(self.teamname), self.point_counter)

    def remove_points(self):
        """
        Removes a point from a team
        """
        del self.point_counter[-1]
    def get_points(self):
        """
        Retrieves the number of sets for a particular team
        """
        return sum(self.point_counter)

# Reset
    def reset_all(self):
        """
        Resets everything to 0
        """

        self.set_counter = 0
        self.point_counter.clear()

# Display
    def init_graph(self):
        """
        Initializes graph
        """
        x = [1,2,3,4]
        y = [1,2,3,2]

        tick_spacing = 1
        
        fig, ax = plt.subplots(1,1)
        plt.plot(x,y, 'k-o')
        ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        
        plt.ylabel('Margin')
        plt.xlabel('Points')
        plt.title('Everest Form Plot')
        
        plt.show()


    """
        hl, = plt.plot([], [])

        def update_line(hl, new_data):
            hl.set_xdata(numpy.append(hl.get_xdata(), new_data))
            hl.set_ydata(numpy.append(hl.get_ydata(), new_data))
            plt.draw()
    """
#graph()
        


