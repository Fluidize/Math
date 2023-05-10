import tqdm

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

def gen_primes(count):
    arr = [x for x in range(count+1)]; arr[0:2] = []
    print(len(arr))
    iteration = 0;
    while True:
        divisor = arr[iteration]; count = 0
        for num in tqdm.tqdm(arr):
            if not (num % divisor) and (not (num == divisor)):
                arr.remove(num)
                count += 1
        if count == 0:
            break
        iteration += 1
    return arr



if __name__ == "__main__":
    print(len(gen_primes(100000)))