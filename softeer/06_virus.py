K, P, N = list(map(int, input().split()))

nVirus = K
for i in range(N):
    nVirus *= P
    nVirus %= 1000000007

print(nVirus)