import pandas
from turtle import Screen, title
from brain import Brain
from scoreboard import Score
import playsound

l_state = []
data = pandas.read_csv('50_states.csv')  #reading my data from my csv document
title("US States Quiz Game")
for i in data.state:                       #this will create a list of all states from csv states data
    l_state.append(i)

Score = Score()
b = Brain()
screen = Screen()
screen.setup(750,500)
screen.bgpic("blank_states_img.gif")
Score.update_score()                        #this module will shows up my currunt ponint which  default is 0
Game_on = True
while Game_on:
    player_choice = screen.textinput(title="Please Type!",prompt='Enter State Name').title()
    
    if player_choice in l_state:              #checking if user has entered right answer

            pd = pandas.Index(data.state)
            index_location = pd.get_loc(player_choice)          #this will return index location of any states that are in data.states
            b.show_states(data.x[index_location],data.y[index_location],player_choice)
            Score.score+=5
            Score.update_score()
            l_state.remove(player_choice)                   #removing the state name that has player/user has already guessed 

    else:                                                  #this will run if user has entered wrong anser 
        Game_on = False
        Score.game_over()
        playsound.playsound("wrong.wav")
    
    








screen.exitonclick()


#this code is written by pramod 
#bug ho ya koi suggetion ho to contact me on email - pramodsingh0591@gmail.com