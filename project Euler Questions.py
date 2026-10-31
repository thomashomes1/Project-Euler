#Project Euler Questions 

def multi(x):
    valid = []
    for i in range(1,x):
        if i % 3 == 0:
            valid.append(i)
        elif i % 5 == 0:
            valid.append(i)
    total = 0
    for i in valid:
        total = total + i
        
    print(total)
    
def fib():
    prev2 = 1
    prev1 = 2
    evens = []
    for i in range(1,100):
        now = prev1 + prev2
        prev2 = prev1
        prev1 = now
        if now > 4000000:
            break
        if now % 2 == 0:
            evens.append(now)
        
    total = 2
    for i in evens:
        total = total+ i
    print(evens)
    print(total)
        
        
        
def primeFactors(x): #doesn't work
    status2 = True
    status3 = True
    while status2 == True:
        if x % 2 == 0:
            x = x / 2
        else:
            status2 = False
            print(x)
    while status3 == True:
        if x % 3 == 0:
            x = x / 3
        else:
            status3 = False
            print(x)

#primeFactors(11266)

    

def sumSquare(x):
    sumOfSquares = 0
    for i in range(1,x+1):
        num = i**2
        sumOfSquares = sumOfSquares + num
    print("sumOfSquares", sumOfSquares)
    val = 0
    for i in range(1,x+1):
        val = val + i
    squareOfSum = val**2
    ans = squareOfSum - sumOfSquares
    print(ans)
    

def smallestNum(): #works but just takes a long time 
    valid = []
    for i in range(1,1000000000000):
        counter = 0
        
        for x in range(11,21): #all of the factors of 1 to 10 are included in the 11 to 20 so don't need to check
            if i % x == 0:
                counter = counter + 1
        if counter == 10:
            print(i)
            break
            
def primeGenerator():     #takes too long
    valid = []
    while len(valid) < 10002:
        for i in range(1,1000000000):
            counter = 0
            for x in range(2,i):
                if i % x != 0:
                    counter = counter + 1
            if counter == i-2:
                valid.append(i)
    print(valid[10000])
    

def pythagoras():
    for a in range (1,1000):
        for b in range(1, 1000-a):
            c = 1000 - a - b
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
                print("Answer: ",a,b,c)
                print("TOTAL", a*b*c)
                break
    
        
                    
def largestProduct():
    largest = 0
    number = [int(i) for i in str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)]
    print(number)
    for i in range(len(number)-12):
        val = number[i]*number[i+1]*number[i+2]*number[i+3]*number[i+4]*number[i+5]*number[i+6]*number[i+7]*number[i+8]*number[i+9]*number[i+10]*number[i+11]*number[i+12]
        if val > largest:
            largest = val
        
    print(largest)
    
def primeBelow():
    valid = []
    for i in range(1,2000000):
        counter = 0
        for x in range(2,i):
            if i % x != 0:
                counter = counter + 1
        if counter == i-2:
            valid.append(i)
           
    print(sum(valid))

import math

def SieveOfEratosthenes(x):
    root = x**0.5
    rootL = math.ceil(root)
    print(rootL)
    numbers = []
    for c in range(1,x+1):
        numbers.append(True)
    print(numbers)
    for a in range(2,rootL):
        if numbers[a-1] == True:
            length = len(numbers)
            half = math.ceil(len(numbers) / 2)
            for i in range(2,half+1):
                nonPrime = a*i
                if nonPrime < len(numbers)+1:
                    numbers[nonPrime-1] = False
    numbers[0] = False
    print(numbers)  #upto here is crux of the sieve
    total = 0
    for d in range(len(numbers)):
        if numbers[d] == True:
            total = total + d+1
    print(total)
   
    

#SieveOfEratosthenes(2000000)    
    
    #extension for PE 10,001 prime 
   # l=[]
   # counter = 0
   # for i in range((len(numbers))):
   #     if numbers[i] == True:
   #         l.append(i+1)
    #        print(i+1)
     #       counter = counter + 1
     #       if counter == 10001:
       #         print(l[10000])
       #         break
            
    #extension for Project Euler prime factorisation
    #l = []
    #for i in range((len(numbers))):
     #   if numbers[i] == True:
     #       if 600851475143 % (i+1) == 0:
      #          print(i+1)
      #          l.append(i+1)
       #         total = 1
       #         for i in l:
        #            total = total*i
        #            if total == 600851475143:
         #               print("YAY")
         #               break
                    
            

def factorialDigitSum(x):
    total = 1
    for i in range(0,x):
        total = total * (x-i)
    print(total)
    l = []
    total = str(total)
    for num in total:
        l.append(num)
    print(l)
    counter = 0 
    for b in range(len(l)):
        counter = counter + int(l[b])
    print(counter)

def palindromeProduct():
    greatest = 0
    counter = 0
    dromes = []
    for i in range(999,99,-1):
        for x in range(999,99,-1):
            num = i * x
            if len(str(num)) % 2 == 0 and len(str(num)) == 6:
                l = list(str(num))
                if l[0] == l[5] and l[1] == l[4] and l[2] == l[3]:
                    dromes.append(num)
                if len(dromes) == 5:
                    print(dromes)
                    break
                    
                   # if counter == 0:
                   #     greatest = num
                   #     counter = 1
                  #  else:
                  #      if num <= greatest:
                  #          print(greatest)
                   #         break
    


def LongestCollatzSequence():
    
    greatest = 0
    stored = 0
    for i in range(1,1000000):
        x = i 
        counter = 1
        test = True
        while test == True:
            if i == 1:
                if counter > greatest:
                    greatest = counter
                    stored = x
                test = False
            elif i % 2 == 0:
                i = i /2
                counter = counter + 1 
            else:
                i = 3*i + 1
                counter = counter + 1
            
                
    print(greatest, stored)

def powerDigitSum(x,y):
    num = str(x**y)
    total = 0 
    l = [*num]
    for i in l:
        total = int(i) + total
    print(total)
    
''' 
def AmicableNumbers(x):
    
    for i in range(1,x):
        valid = []
        for a in range(1,i):
            if x % i == 0:
                valid.append(i)     
 '''   
    
def large_sum(numbers):
    first_ten = []
    carry = 0
    for i in range(1,51):
        total = 0 
        for number in numbers:
            total = int(str(number)[-i]) + total
        total += carry
        val = int(str(total)[-1])
        first_ten.append(val)
        carry = int(str(total)[:-1])
        if i == 50:
            first_ten.append(carry)
    first_ten = list(reversed(first_ten))
    print(first_ten)
            
def largest_prod_grid(grid):
    largest  = 0
    for y in range(20):
        for x in range(16):
            total = grid[x][y]*grid[x+1][y]*grid[x+2][y]*grid[x+3][y]
            if total > largest:
                largest = total
    for x in range(20):
        for y in range(16):
            total = grid[x][y]*grid[x][y+1]*grid[x][y+2]*grid[x][y+3]
            if total > largest:
                largest = total
    for y in range(20):
        for x in range(20):
            if x+3 < 20 and y+3 < 20:
                total = grid[x][y]*grid[x+1][y+1]*grid[x+2][y+2]*grid[x+3][y+3]
                if total > largest:
                    largest = total
    for y in range(19,-1,-1):
        for x in range(20):
            if x+3 < 20 and y-3 > -1:
                total = grid[x][y]*grid[x+1][y-1]*grid[x+2][y-2]*grid[x+3][y-3]
                if total > largest:
                    largest = total
                
    print(largest)
    print(grid[2][3])
    
largest_prod_grid([
    [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
    [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
    [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
    [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
    [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
    [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
    [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
    [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
    [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
    [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
    [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
    [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
    [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
    [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
    [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
    [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
    [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
    [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]
]
)
    
            
            