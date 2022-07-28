def readNums ():
    file_str = open('100000likliste 4.txt','r').read()
    nums = file_str.split('\n')
    intNums = []
    for i in nums:
        x = float(i)
        y = int(x * 1000)
        intNums.append(y)
    return intNums

def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

def radixSort(array):
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


import time
data = readNums()
resp = []
start = time.time()
radixSort(data)
end = time.time()

for i in data:
    resp.append(i/1000)
#f=open('100000liklisteradixsort.txt','w') #Radix sorttan sonra siralanmis verileri almak için dosya satirlari
#for ele in resp:
    #f.write(str(ele)+'\n')
print(resp)
print("Geçen zaman:",end - start)