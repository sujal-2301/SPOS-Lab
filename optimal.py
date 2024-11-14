# Get user inputs
capacity = int(input("Enter the capacity of memory: "))
pages = [int(x) for x in input("Enter the reference string: ")]
faults = hits = 0
memory = []

# Function to find the optimal page to replace


def findOptimalPage(startIndex):
    maxDist, optimalPage = 0, None
    for page in memory:
        if page not in pages[startIndex + 1:]:
            return page
        dist = pages[startIndex + 1:].index(page)
        if dist > maxDist:
            maxDist, optimalPage = dist, page
    return optimalPage


# Print header
print("Page\tMemory\t\tStatus")

# Process each page
for i, page in enumerate(pages):
    if page in memory:  # Page hit
        hits += 1
        status = 'H'
    else:  # Page fault
        if len(memory) == capacity:
            memory.remove(findOptimalPage(i))
        memory.append(page)
        faults += 1
        status = 'F'

    # Print current state
    print(f"{page}\t{memory}\t\t{status}")

# Final statistics
print(f"\nHit Ratio = {hits}/{len(pages)} = {hits / len(pages):.2f}")
print(f"Fault Ratio = {faults}/{len(pages)} = {faults / len(pages):.2f}")
