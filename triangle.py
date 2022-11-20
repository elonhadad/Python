"""
Student: elon hadad
ID: 034672139
Assigmment no. 2
Program: triangle.py
"""
def inside_str(length, d, s, new_d):
    #make string for the inner triangle 
    
    cnt = 0
    y = ''
    for j in range(length):
        if d >0:
            y += '$'
            d -= 1
        else:
            y += ' '
            cnt += 1
            if cnt == s:
                cnt = 0
                d = new_d
    return (d, y)

def triangle(h, d, s, new_d):
    #print the triangle and the string
    
    for i in range(1,(h+1)):
        length = 2 * (i)-3
        d,y  =  inside_str(length, d, s, new_d)
        if i == 1:
            print(' ' * (h-i) + '*')
        elif i != h and i != 1:
            print(' ' * (h-i) + '*' + y + '*')
        else:
            print('*' * ((2*h)-1))            
        
def main():
    height = int(input('Please enter height: '))
    dollars = int(input('Please enter number of $: '))
    space = int(input('Please enter number of spaces: '))
    new_d= dollars
    triangle(height, dollars, space, new_d)

main()

