capacity = int(input('Enter the capacity of memory:'))
pages = list(input('Enter the reference string:'))
pages = [int(item) for item in pages]
faults = 0
hits = 0
memory = []


def findOptimalPage(startIndex):
    maxDistance = 0
    optimalPage: int
    distance = 0
    for page in memory:
        found = False
        for j in range(startIndex+1, len(pages)):
            if pages[j] == page:
                found = True
                break
            distance += 1
        if found:
            if distance > maxDistance:
                maxDistance = distance
                optimalPage = page
        else:
            optimalPage = page
            return optimalPage
        distance = 0
    return optimalPage


print(f'Page\tMemory\t\ttStatus')
for i in range(len(pages)):
    found = False
    if pages[i] in memory:
        found = True
        hits += 1
    else:
        if len(memory) == capacity:
            optimalPage = findOptimalPage(i)
            memory.remove(optimalPage)
        memory.append(pages[i])
        faults += 1

    print(f'{pages[i]}\t{list(memory)}', end='\t\t')
    if found:
        print('H')
    else:
        print('F')

print(f'Hit Ratio = {hits}/{len(pages)} = {hits/len(pages)}')
print(f'Fault Ratio = {faults}/{len(pages)} = {faults/len(pages)}')
