# Smart Waste Management System

bio_bin = 0
non_bio_bin = 0
capacity = 10

print("SMART WASTE MANAGEMENT SYSTEM")

while True:
    print("\n1. Add Biodegradable Waste")
    print("2. Add Non-Biodegradable Waste")
    print("3. Show Status")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        qty = int(input("Enter quantity: "))
        bio_bin += qty
        if bio_bin >= capacity:
            print("⚠ Biodegradable bin is FULL!")
        else:
            print("Waste added successfully.")

    elif choice == 2:
        qty = int(input("Enter quantity: "))
        non_bio_bin += qty
        if non_bio_bin >= capacity:
            print("⚠ Non-Biodegradable bin is FULL!")
        else:
            print("Waste added successfully.")

    elif choice == 3:
        print("\n--- Bin Status ---")
        print("Biodegradable Waste:", bio_bin)
        print("Non-Biodegradable Waste:", non_bio_bin)

    elif choice == 4:
        print("Exiting system. Keep your surroundings clean!")
        break

    else:
        print("Invalid choice! Try again.")
