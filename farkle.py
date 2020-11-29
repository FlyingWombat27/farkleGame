import random
import numpy as np

def main():
    team_name1 = str(input('What is the name of team one?'))
    team_name2 = str(input('What is the name of team two?'))
    who_goes_first = str(input('Who will go first?'))
    dice_rolls = 6
    dice_size = 6
    who_goes_second = str()
    dice_avail = []
    
    if who_goes_first == team_name1:
        who_goes_second = team_name2
    else:
        who_goes_second = team_name1
        
    print(f'{who_goes_second} goes second!')
    
    for i in range(0,dice_rolls):
        roll = random.randint(1,dice_size)
        dice_avail.append(roll)
    dice_avail = np.array(dice_avail)    
    dice_avail = np.sort(dice_avail)
    print(f'{who_goes_first}, you rolled the following: {dice_avail} ')
    
if __name__== "__main__":
  main()