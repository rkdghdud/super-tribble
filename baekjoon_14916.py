n = int(input())
coin = 0

if n == 1 or n == 3:
    print(-1)

elif n % 5 == 0:
    print(n // 5)

elif (n % 5) % 2 == 0:
    coin = (n//5) + ((n%5)//2)
    print(coin)

else:
    coin = ((n//5)-1) + ((n%5+5)//2)
    print(coin)
    
