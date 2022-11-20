"""
Student: elon hadad
ID: 034672139
Assigmment no. 1
Program: arithmetic.py
"""

def find_arithmetic(lst):
    #find the longest arithmetic from input
    long_len = 0
    long_index = 0
    for i in range (len(lst)-1):
        length = 1
        diff = int(lst[i+1]) - int(lst[i])
        for j in range (i+1, len(lst)):
            if int(lst[j]) - int(lst[j-1]) == diff:
                length += 1
            else:
                break
        if length > long_len:
            long_len = length
            long_index = i
    
    split_seq = ','.join(lst[long_index:long_len+long_index])
    
    return split_seq
        

def main():
    numbers = input('Please enter list of number separated by commas: ')
    split_num = numbers.split(',')    
    print("The longest arithmetic sequnce is: ",find_arithmetic(split_num))

main()