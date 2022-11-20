"""
Student: elon hadad
ID: 034672139
Assignment no. 1
Program: prime_decomposition.py
"""

def decompose(n):
    '''Receives a positive integer n and returns a representative list 
    The decomposition of the number into prime numbers in ascending order'''
    
	factors= []
	i=2
	while n > 1:
		rem = n%i
		if rem == 0:
			n = n/i
			factors.append(i)
		else:
			i=i+1    
	return factors
   

def print_decomposition(n):
    '''Receives a list from decompose and print'''
    
    n = int(n)
    factors = decompose(n)
    cnt = 1
    if n > 1 :
        print(n,"=",end = "", sep = "")
    for index in range(0, len(factors)-1):
        f_lst = factors[index]
        if factors[index+1] == f_lst:
            cnt += 1
        elif cnt != 1:
            print(factors[index],"^",cnt, end = "*" ,sep = "")
            f_lst = factors[index+1]
            cnt = 1
        else:
            print(factors[index], end = "*" ,sep = "")
            
    if cnt == 1:
        print(factors[-1])
    else:
        print(factors[index],"^",cnt,sep= "")  
        
        
def main():
    while True:
        n = input("Please enter an integer greater than 1 (quit to stop): ")
        if n == "quit":
            print("program ends, good bye")
            break
        try:
            print_decomposition(n)
        except ValueError:
            print("Illegal input. Try again")
        except IndexError:
            print("Illegal input. Try again")
main()