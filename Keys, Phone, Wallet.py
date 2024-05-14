# Read the number of items grabbed
n = int(input())

# Create a set to store the grabbed items
grabbed_items = set()

# Read the grabbed items
for _ in range(n):
    grabbed_items.add(input())

# Check which items are missing
missing_items = ["keys", "phone", "wallet"]
for item in missing_items:
    if item not in grabbed_items:
        print(item)
        
# If no item is missing, print "ready"
if all(item in grabbed_items for item in missing_items):
    print("ready")
