"""
***********************************************************************
This program tosses d100 die and states the result based on skill level
in RuneQuest 3rd edition
***********************************************************************
"""

# This programs creates die class to emulate die rolls
# import random to simulate die cast

from random import randint

class Die:

    # initial die value
    def __init__(self):
        self.score = 0

    # die_roll generates a random number between 1 and 100. In this case 0 means 100
    # as only values 01 is the lowest possible in RuneQuest 3rd edition
    def die_roll(self):
        self.score = randint(1, 100)
        return self.score

# the main roll function with results
def main():


    # prompt the player for skill level
    skill_lvl = (raw_input("Input skill level: "))

    # loop until a valid numeric value is given
    while skill_lvl.isalpha():
        print "Please give numeric value"
        skill_lvl = (raw_input("Input skill level: "))
    # converts given string value to numberic
    skill_lvl = int(skill_lvl)
    # caling Die class to create casting object
    casting = Die()
    # casting objects calls die_roll method
    casting.die_roll()
    # roll varibale using casting object
    roll = casting.die_roll()
    print roll
   
# This monstrosity really needs some work...
    skill_list = {
            xrange(1, 8) : {1 : "Critical", 96 : "Fumble", 97 : "Fumble", 98 : "Fumble", 99 : "Fumble", 100 : "Fumble"},
            xrange(8, 11) : {1 : "Critical", 2 : "Exceptional", 96 : "Fumble", 97 : "Fumble", 98 : "Fumble", 99 : "Fumble", 100 : "Fumble"},                          
            xrange(11, 13) : {1 : "Critical", 2 : "Exceptional", 97 : "Fumble", 98 : "Fumble", 99 : "Fumble", 100 : "Fumble"},                                      
            xrange(13, 18) : {1 : "Critical", 2 : "Exceptional", 3 : "Exceptional", 97 : "Fumble", 98 : "Fumble", 99 : "Fumble", 100 : "Fumble"},                                     
            xrange(18, 23) : {1 : "Critical", 2 : "Exceptional", 3 : "Exceptional", 4 : "Exceptional", 97 : "Fumble", 98 : "Fumble", 99 : "Fumble", 100 : "Fumble"},                                       
            xrange(23, 28) : {1 : "Critical", 2 : "Exceptional", 3 : "Exceptional", 4 : "Exceptional", 5 : "Exceptional", 97 : "Fumble", 98 : "Fumble", 99 : "Fumble", 100 : "Fumble"},                                     
            xrange(28, 30) : {1 : "Critical", 2 : "Exceptional", 3 : "Exceptional", 4 : "Exceptional", 5 : "Exceptional", 6 : "Exceptional", 97 : "Fumble", 98 : "Fumble", 99 : "Fumble", 100 : "Fumble"},                                       
            xrange(30, 31) : {1 : "Critical", 2 : "Critical", 3 : "Exceptional", 4 : "Exceptional", 5 : "Exceptional", 6 : "Exceptional", 97 : "Fumble", 98 : "Fumble", 99 : "Fumble", 100 : "Fumble"},                        
            xrange(31, 33) : {1 : "Critical", 2 : "Critical", 3 : "Exceptional", 4 : "Exceptional", 5 : "Exceptional", 6 : "Exceptional", 98 : "Fumble", 99 : "Fumble", 100 : "Fumble"}, 
            xrange(33, 38) : {1 : "Critical", 2 : "Critical", 3 : "Exceptional", 4 : "Exceptional", 5 : "Exceptional", 6 : "Exceptional", 7 : "Exceptional", 98 : "Fumble", 99 : "Fumble", 100 : "Fumble"},
            xrange(38, 43) : {1 : "Critical", 2 : "Critical", 3 : "Exceptional", 4 : "Exceptional", 5 : "Exceptional", 6 : "Exceptional", 7 : "Exceptional", 8 : "Exceptional", 98 : "Fumble", 99 : "Fumble", 100 : "Fumble"},    
            xrange(43, 48) : {1 : "Critical", 2 : "Critical", 3 : "Exceptional", 4 : "Exceptional", 5 : "Exceptional", 6 : "Exceptional", 7 : "Exceptional", 8 : "Exceptional", 9 : "Exceptional", 98 : "Fumble", 99 : "Fumble", 100 : "Fumble"}, 
            xrange(48, 50) : {1 : "Critical", 2 : "Critical", 3 : "Exceptional", 4 : "Exceptional", 5 : "Exceptional", 6 : "Exceptional", 7 : "Exceptional", 8 : "Exceptional", 9 : "Exceptional", 10 : "Exceptional", 98 : "Fumble", 99 : "Fumble", 100 : "Fumble"},  
            xrange(50, 51) : {1 : "Critical", 2 : "Critical", 3 : "Critical", 4 : "Exceptional", 5 : "Exceptional", 6 : "Exceptional", 7 : "Exceptional", 8 : "Exceptional", 9 : "Exceptional", 10 : "Exceptional", 98 : "Fumble", 99 : "Fumble", 100 : "Fumble"},      
            xrange(51, 53) : {1 : "Critical", 2 : "Critical", 3 : "Critical", 4 : "Exceptional", 5 : "Exceptional", 6 : "Exceptional", 7 : "Exceptional", 8 : "Exceptional", 9 : "Exceptional", 10 : "Exceptional", 99 : "Fumble", 100 : "Fumble"},    
            xrange(53, 58) : {1 : "Critical", 2 : "Critical", 3 : "Critical", 4 : "Exceptional", 5 : "Exceptional", 6 : "Exceptional", 7 : "Exceptional", 8 : "Exceptional", 9 : "Exceptional", 10 : "Exceptional", 11 : "Exceptional", 99 : "Fumble", 100 : "Fumble"},         
            xrange(58, 63) : {1 : "Critical", 2 : "Critical", 3 : "Critical", 4 : "Exceptional", 5 : "Exceptional", 6 : "Exceptional", 7 : "Exceptional", 8 : "Exceptional", 9 : "Exceptional", 10 : "Exceptional", 11 : "Exceptional", 12 : "Exceptional", 99 : "Fumble", 100 : "Fumble"},          
            xrange(63, 68) : {1 : "Critical", 2 : "Critical", 3 : "Critical", 4 : "Exceptional", 5 : "Exceptional", 6 : "Exceptional", 7 : "Exceptional", 8 : "Exceptional", 9 : "Exceptional", 10 : "Exceptional", 11 : "Exceptional", 12 : "Exceptional", 13 : "Exceptional", 99 : "Fumble", 100 : "Fumble"},        
            xrange(68, 70) : {1 : "Critical", 2 : "Critical", 3 : "Critical", 4 : "Exceptional", 5 : "Exceptional", 6 : "Exceptional", 7 : "Exceptional", 8 : "Exceptional", 9 : "Exceptional", 10 : "Exceptional", 11 : "Exceptional", 12 : "Exceptional", 13 : "Exceptional", 14 : "Exceptional", 99 : "Fumble", 100 : "Fumble"},         
            xrange(70, 71) : {1 : "Critical", 2 : "Critical", 3 : "Critical", 4 : "Critical", 5 : "Exceptional", 6 : "Exceptional", 7 : "Exceptional", 8 : "Exceptional", 9 : "Exceptional", 10 : "Exceptional", 11 : "Exceptional", 12 : "Exceptional", 13 : "Exceptional", 14 : "Exceptional", 99 : "Fumble", 100 : "Fumble"},        
            xrange(71, 73) : {1 : "Critical", 2 : "Critical", 3 : "Critical", 4 : "Critical", 5 : "Exceptional", 6 : "Exceptional", 7 : "Exceptional", 8 : "Exceptional", 9 : "Exceptional", 10 : "Exceptional", 11 : "Exceptional", 12 : "Exceptional", 13 : "Exceptional", 14 : "Exceptional", 100 : "Fumble"},      
            xrange(73, 78) : {1 : "Critical", 2 : "Critical", 3 : "Critical", 4 : "Critical", 5 : "Exceptional", 6 : "Exceptional", 7 : "Exceptional", 8 : "Exceptional", 9 : "Exceptional", 10 : "Exceptional", 11 : "Exceptional", 12 : "Exceptional", 13 : "Exceptional", 14 : "Exceptional", 15 : "Exceptional", 100 : "Fumble"},  
            xrange(78, 83) : {1 : "Critical", 2 : "Critical", 3 : "Critical", 4 : "Critical", 5 : "Exceptional", 6 : "Exceptional", 7 : "Exceptional", 8 : "Exceptional", 9 : "Exceptional", 10 : "Exceptional", 11 : "Exceptional", 12 : "Exceptional", 13 : "Exceptional", 14 : "Exceptional", 15 : "Exceptional", 16 : "Exceptional", 100 : "Fumble"},      
            xrange(83, 88) : {1 : "Critical", 2 : "Critical", 3 : "Critical", 4 : "Critical", 5 : "Exceptional", 6 : "Exceptional", 7 : "Exceptional", 8 : "Exceptional", 9 : "Exceptional", 10 : "Exceptional", 11 : "Exceptional", 12 : "Exceptional", 13 : "Exceptional", 14 : "Exceptional", 15 : "Exceptional", 16 : "Exceptional", 17 : "Exceptional", 100 : "Fumble"},    
            xrange(88, 90) : {1 : "Critical", 2 : "Critical", 3 : "Critical", 4 : "Critical", 5 : "Exceptional", 6 : "Exceptional", 7 : "Exceptional", 8 : "Exceptional", 9 : "Exceptional", 10 : "Exceptional", 11 : "Exceptional", 12 : "Exceptional", 13 : "Exceptional", 14 : "Exceptional", 15 : "Exceptional", 16 : "Exceptional", 17 : "Exceptional", 18 : "Exceptional", 100 : "Fumble"},        
            xrange(90, 93) : {1 : "Critical", 2 : "Critical", 3 : "Critical", 4 : "Critical", 5 : "Critical", 6 : "Exceptional", 7 : "Exceptional", 8 : "Exceptional", 9 : "Exceptional", 10 : "Exceptional", 11 : "Exceptional", 12 : "Exceptional", 13 : "Exceptional", 14 : "Exceptional", 15 : "Exceptional", 16 : "Exceptional", 17 : "Exceptional", 18 : "Exceptional", 100 : "Fumble"},        
            xrange(93, 98) : {1 : "Critical", 2 : "Critical", 3 : "Critical", 4 : "Critical", 5 : "Critical", 6 : "Exceptional", 7 : "Exceptional", 8 : "Exceptional", 9 : "Exceptional", 10 : "Exceptional", 11 : "Exceptional", 12 : "Exceptional", 13 : "Exceptional", 14 : "Exceptional", 15 : "Exceptional", 16 : "Exceptional", 17 : "Exceptional", 18 : "Exceptional", 19 : "Exceptional", 100 : "Fumble"},     
            xrange(98, 101) : {1 : "Critical", 2 : "Critical", 3 : "Critical", 4 : "Critical", 5 : "Critical", 6 : "Exceptional", 7 : "Exceptional", 8 : "Exceptional", 9 : "Exceptional", 10 : "Exceptional", 11 : "Exceptional", 12 : "Exceptional", 13 : "Exceptional", 14 : "Exceptional", 15 : "Exceptional", 16 : "Exceptional", 17 : "Exceptional", 18 : "Exceptional", 19 : "Exceptional", 20 : "Exceptional", 100 : "Fumble"},      

                }



# Need to still workout what happens if value not in dictionary
    try:
        for key in skill_list:
            if skill_lvl in key:
                print skill_list[key][roll]        
                break
    except(KeyError):
        pass
    
       
            

count = 100
while count > 0:
    main()
    count -= 1




