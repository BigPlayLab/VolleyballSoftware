# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 11:29:26 2018

@author: Joel Chandler
"""
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

class data():
    """
    Stores all data for project
    """
    def __init__(self, team):
        """ Initializes class """
        self.team = team
        self.scoreline = []
        self.cumulative_score = []
        self.setline = []
    def get_team_name(self):
        """Gets name of team and returns as <str>"""
        return self.team
    def add_score(self):
        """Adds single score to list"""
        self.scoreline.append(1)
        self.cumulative_score = np.cumsum(self.scoreline)
        self.cumulative_score = self.cumulative_score.tolist()
    def no_score(self):
        """Adds no score to cumulative list"""
        self.scoreline.append(0)
        np.pad(self.cumulative_score, (0, 1), 'constant')
    def get_score_list(self):
        """Gets list of scores"""
        return self.scoreline
    def get_cumulative_score_list(self):
        return self.cumulative_score
        
    def get_score(self):
        """Returns numerical value of score"""
        return sum(self.scoreline)

    def plot_score(self):
        plt.close()
        plt.ion()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        line1, = ax.plot(self.cumulative_score, 'r-')
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.plot(self.cumulative_score)
        #plt.show()
    def close_plot(self):
        plt.close()
class process(data):
    """
    Class to process the information
    """
    def __init__(self, team, margin):
        data.__init__(self, team)
        self.margin = margin
        
def make_teams(team1_name, team2_name):
    team1_name = str(team1_name)
    team2_name = str(team2_name)
    team_1 = data(team1_name)
    team_2 = data(team2_name)
    return team_1, team_2
    
team_1, team_2 = make_teams("SPLC","SLC")

def margin(team1,team2):
    print(team1.get_cumulative_score_list())
    print(team2.get_cumulative_score_list())
    team1_score = np.array(team1.get_cumulative_score_list())
    team2_score = np.array(team2.get_cumulative_score_list())
    difference = team1_score - team2_score
    print(difference)
    
    plt.close()
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1, = ax.plot(difference, 'r-')
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.plot(difference)
    plt.show()
    
def main():
    team_1.add_score()
    team_1.add_score()
    team_1.add_score()
    team_1.no_score()
    team_1.no_score()
    team_1.no_score()
    team_1.add_score()
    team_1.add_score()
    team_1.add_score()
    
    team_2.no_score()
    team_2.add_score()
    team_2.add_score()
    team_2.add_score()
    team_2.add_score()
    team_2.add_score()
    team_2.add_score()
    team_2.no_score()
    team_2.add_score()
    if input("test") == 'g':
        plt.close()
        team_1.add_score()
        team_2.no_score()
    #team_1.plot_score()
#    if __name__ == "__main__":
    
main()
         