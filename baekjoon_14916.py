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
    
=============================================
n = int(input())
coin = [50001, 50001, 1, 50001, 2, 1]

for i in range(6,n+1):
    coin.append(min(coin[i - 2] + 1, coin[i - 5] + 1))
if coin[n]>50000:
    print(-1)
else:
    print(coin[n])
