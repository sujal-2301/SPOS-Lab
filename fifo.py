# FIFO Page Replacement Algorithm Implementation

# Get user inputs
capacity = int(input("Enter the capacity of memory: "))  # Memory capacity
reference_string = input(
    "Enter the reference string (without spaces): ")  # Reference string

# Initialize variables
memory = []
faults = 0
hits = 0
top = 0  # To keep track of the first page to replace

# Convert reference string to a list of integers
pages = list(map(int, reference_string))

# Print the header for the table
print("\nPage    Memory          Status")
print("------------------------------")

# Iterate through the reference string
for page in pages:
    if page not in memory:  # Page fault
        if len(memory) < capacity:
            memory.append(page)  # Add page to memory
        else:
            memory[top] = page  # Replace the page at the front (FIFO)
            # Move the pointer to the next page in FIFO order
            top = (top + 1) % capacity
        faults += 1
        status = 'F'  # Page fault
    else:  # Page hit
        hits += 1
        status = 'H'  # Page hit

    # Print the current state of the page, memory, and status
    print(f"{page}\t{memory}\t\t{status}")

# Final output: Hit and Fault ratios along with the number of hits
print("\nTotal requests: ", len(pages))
print("Total Page Faults: ", faults)
print("Total Hits: ", hits)
print("Fault Rate:", (faults / len(pages)) * 100, "%")
print("Hit Rate:", (hits / len(pages)) * 100, "%")
