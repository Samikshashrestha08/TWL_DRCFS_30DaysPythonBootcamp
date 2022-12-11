import random
options=['rock','paper','scissor']
for _ in range(5):
    player_1=input('player 1 choose either Rock,Paper or Scissor')
    player_2=input('player 2 choose either rock,Paper or Scissor')
    rock='rock'
    paper='paper'
    scissor='scissor'
    if player_1==rock and player_2==rock:
        print('its a toie')
    elif player_1==scissor and player_2==scissor:
        print('its a tie') 
    elif player_1==paper and player_2==paper:
        print('its a tie') 
    elif player_1==paper and player_2==scissor:
        print('player_2 wins')  
    elif player_1==scissor and player_2==paper:
        print('player_1 wins')         
    elif player_1==rock and player_2==paper:
        print('player_2 wins')
    elif player_1==paper and player_2==rock:
        print('player_1 wins')                          
    elif player_1==scissor and player_2==rock:
        print('player_2 wins') 
    elif player_1==rock and player_2==scissor:
        print('player_1 wins')                     