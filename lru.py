# LRU Page Replacement Algorithm Implementation

# Get user inputs
capacity = int(input("Enter the capacity of memory: "))  # Memory capacity
reference_string = input(
    "Enter the reference string (without spaces): ")  # Reference string

# Convert reference string to a list of integers
pages = list(map(int, reference_string))

# Initialize variables
memory = []
indexes = {}
faults = 0
hits = 0

# Print the header for the table
print("\nPage    Memory          Status")
print("------------------------------")

# Iterate through the reference string
for i, page in enumerate(pages):
    if page not in memory:  # Page fault
        if len(memory) < capacity:
            memory.append(page)  # Add page to memory if space is available
        else:
            # Find the least recently used page among the current memory
            lru_page = min((p for p in memory),
                           key=lambda x: indexes.get(x, -1))
            memory.remove(lru_page)  # Remove the LRU page from memory
            memory.append(page)  # Add the new page
        faults += 1
        status = 'F'  # Page fault
    else:  # Page hit
        hits += 1
        status = 'H'  # Page hit

    # Update the index of the current page
    indexes[page] = i

    # Print the current state of the page, memory, and status
    print(f"{page}\t{memory}\t\t{status}")

# Final output: Hit and Fault ratios along with the number of hits
print("\nTotal requests: ", len(pages))
print("Total Page Faults: ", faults)
print("Total Hits: ", hits)
print("Fault Rate:", (faults / len(pages)) * 100, "%")
print("Hit Rate:", (hits / len(pages)) * 100, "%")
