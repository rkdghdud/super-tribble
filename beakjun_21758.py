n = int(input())
honey = [0]
ldp = [0 for i in range(100002)]
rdp = [0 for i in range(100002)]
result = -1

for i in map(int,input().split()):
    honey.append(i)

for i in range(1,n+1):
    ldp[i] = ldp[i - 1] + honey[i]

for i in range(n,0,-1):
    rdp[i] = rdp[i + 1] + honey[i]

for i in range(2,n):
    result = max(result, (ldp[n] - ldp[1] - honey[i]) + (ldp[n] - ldp[i]))
for i in range(n-1,1,-1):
    result = max(result, (rdp[1] - rdp[n] - honey[i]) + (rdp[1] - rdp[i]))
for i in range(2,n):
    result = max(result, ldp[i] - honey[1] + rdp[i] - honey[n])

print(result)
