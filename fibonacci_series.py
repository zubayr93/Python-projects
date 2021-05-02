num =int(input("Enter a number to find fibonacci series :"))

def fib(n) :
    count = 0
    arr = [1]
    n1 = 0
    n2 = 1
    if n == 0:
            return 0
    else:
         for i in range(1,n):
             nth = n1 + n2
             n1 = n2 
             n2 = nth
             arr.append(n2)
    count = count + 1
    return arr      
ans = fib(num)
print (ans)
