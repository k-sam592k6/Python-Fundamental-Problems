n = int(input("Enter a number:"))

sieve = [True]*(n+1)
sieve[0] = False
sieve[1] = False

for i in range(2,n+1):
    if sieve[i] == True:
        for j in range(i*i,n+1,i):
            sieve[j] = False
    
primes = [for i in range(n+1) if sieve[i] == True]

print("Primes upto {n}")
print(*primes)
print(len(primes))
