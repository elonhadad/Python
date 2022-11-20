"""
Student: elon hadad
ID: 034672139
Assigmment no. 3
Program: dice.py
"""

import random

def rolling_dice(n):    
    #rolling dice with random and append to result
    result=[]
    x=0
    while x != n:
        roll_1 = random.randint(1, 6)
        roll_2 = random.randint(1, 6)
        roll_t = roll_1 + roll_2
        x+=1
        result.append(roll_t)        
    return result

def highest_column(n,result): 
    #find the most appearance number and set the highest column
    count = 0
    height = 0
    no_apper = []
    for j in range (2,13):
        for k in range (0,n):
            if j == result[k]:
                count += 1
        if count>height:
                height = count
        no_apper.append(count)
        count = 0
    return no_apper,height
    
def print_column(no_apper,height,n):
    #print the rows from column
    for i in range (0,max(no_apper)):
        for n in range (0,len(no_apper)):
            if height == no_apper[n]:
                print("x", end='\t' )
                no_apper[n] -=1
            else:
                print("\t",end="")
        print()
        height -= 1
    for i in range (2,13):
        if i < 9:
            print(i, end="\t")
        else:
            print(i, end="\t")


def main():
    n = int(input('Please enter number of throws: '))
    result = rolling_dice(n)
    no_apper,height = highest_column(n, result)
    print_column(no_apper,height,n)

main()
        
    
