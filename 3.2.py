def test(n):    
    return [n + 2 * i for i in range(n)]   
        
        #  there is a for loop // the range of i is 0 1 2 
        # when n = 2
        # i = 0 // 2 + 2 * 0
        # i = 1 // 2 + 2 * 1

n = 2
print("Number of piles:",n)
print("Number of stones in each pile:")
print(test(n)) 
n = 10
print("\nNumber of piles:",n)
print("Number of stones in each pile:")
print(test(n)) 
n = 3
print("\nNumber of piles:",n)
print("Number of stones in each pile:")
print(test(n)) 
n = 17
print("\nNumber of piles:",n)
print("Number of stones in each pile:")
print(test(n))
