import random
import numpy as np

def main():
    player_name1 = str(input('What is the name of player one? '))
    player_name2 = str(input('What is the name of player two? '))
    dice_rolls = 6
    dice_size = 6
    dice_avail = []
    dice_kept = []
        
    for i in range(0,dice_rolls):
        roll = random.randint(1,dice_size)
        dice_avail.append(roll)
    
    dice_avail = np.array(dice_avail)    
    dice_avail = np.sort(dice_avail)
    
    print(f'{player_name1}, you rolled the following: {dice_avail} ')
    num_dice_kept = int(input(f'{player_name1}, how many dice would you like to keep? '))   
    
    for i in range(0,num_dice_kept):
        keep = int(input(f'What is dice {i+1} that you would like to keep? '))            
        dice_kept.append(keep)
 
    dice_rolls -= keep
    dice_avail = []
    
    for i in range(0, dice_rolls):
        roll = random.randint(1,dice_size)
        dice_avail.append(roll)
        
    
if __name__== "__main__":
  main()