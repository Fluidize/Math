import os, math
from tqdm import tqdm

#OLD ALGORITHM
# def SOE(count):
#     num = 0
#     array = []
#     for x in range(count):
#         array.append(x+2)
#     while True:
#         removed = 0
#         for x in tqdm.tqdm(range(len(array))):
#             if array[x-removed] % array[num] == 0 and array[x-removed] != array[num]:
#                 array.remove(array[x-removed])
#                 removed += 1
#         if removed == 0:
#             break
#         num += 1 
#     return array

#sieve of eratotheses
def gen_primes(count):
    arr = [x for x in range(count+1)]; arr[0:2] = []
    iteration = 0;
    while True:
        try:
            divisor = arr[iteration]; count = 0
        except:
            return arr
        for num in tqdm(arr):
            if not (num % divisor) and (not (num == divisor)):
                arr.remove(num)
                count += 1
        if count == 0:
            break
        iteration += 1
    return arr

#trial division
def is_prime(num):
    primes = gen_primes(math.floor(math.sqrt(num)))
    for prime in tqdm(primes):
        if num % prime == 0:
            return False
    return True

def prime_factor(num):
    primes = gen_primes(math.floor(math.sqrt(num)))
    factors = []
    for prime in tqdm(primes):
        while True:
            if (num % prime == 0):
                factors.append(prime)
                num /= prime
            else:
                break
    
    #special case
    if is_prime(num) and not 1:
        factors.append(int(num))
    
    if factors == []: return [num]
    return factors

if __name__ == "__main__":
   print(prime_factor(1495641))