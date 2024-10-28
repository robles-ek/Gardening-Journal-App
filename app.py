import csv
from datetime import datetime

# File for storing gardening entries
Journal_file = 'journal.csv'

# Function to add an entry to the gardening journal
def add_journal_entry():
    date = input("Enter the date (YYYY-MM-DD): ")
    client_name = input("Enter the client name: ")
    activity = input("Enter the activity (planting/fertilizing/etc.): ")
    notes = input("Enter any notes: ")

    # Save the entry to CSV
    with open(Journal_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, client_name, activity, notes])

    print("Entry added to the journal!")

# Function to view all entries in the gardening journal
def view_journal_entries():
    try:
        with open(Journal_file, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Date: {row[0]}, Client: {row[1]}, Activity: {row[2]}, Notes: {row[3]}")
    except FileNotFoundError:
        print("No journal entries found.")

# Function to delete an entry based on the client name and date
def delete_journal_entry():
    client_name = input("Enter the client name to delete: ")
    date = input("Enter the date of the entry (YYYY-MM-DD): ")
    
    updated_entries = []
    entry_found = False

    # Read and filter the entries
    with open(Journal_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == date and row[1] == client_name:
                entry_found = True
                continue  # Skip this entry
            updated_entries.append(row)
    
    if entry_found:
        # Overwrite the file with updated entries
        with open(Journal_file, 'w', newline='') as file: #'w' Wite Mode
            writer = csv.writer(file)
            writer.writerows(updated_entries)
        print(f"Entry for {client_name} on {date} deleted.")
    else:
        print("Entry not found.")

# Function to update an entry
def update_journal_entry():
    client_name_update= input("Enter the client name to update: ")
    date = input("Enter the date of the entry (YYYY-MM-DD): ")
    
    updated_entries = []
    entry_found = False

    # Read existing entries and find the one to update
    with open(Journal_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == date and row[1] == client_name_update:
                entry_found = True
                print("\nExisting entry:")
                print(f"Date: {row[0]}, Client: {row[1]}, Activity: {row[2]}, Notes: {row[3]}")
                
                # Ask user what they want to update
                print("\nWhat would you like to update?")
                print("1. Date")
                print("2. Client Name")
                print("3. Activity")
                print("4. Notes")
                choice = input("Choose an option: ")
4
                if choice == '1':
                    new_date = input("Enter new date (YYYY-MM-DD): ")
                    row[0] = new_date
                elif choice == '2':
                    new_client_name = input("Enter new client name: ")
                    row[1] = new_client_name
                elif choice == '3':
                    new_activity = input("Enter new activity (planting/fertilizing/etc.): ")
                    row[2] = new_activity
                elif choice == '4':
                    new_notes = input("Enter new notes: ")
                    row[3] = new_notes
                else:
                    print("Invalid option. No changes made.")
                
                print("Entry updated!")
            
            # Keep the (possibly modified) row
            updated_entries.append(row)
    
    if entry_found:
        # Overwrite the file with updated entries
        with open(Journal_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_entries)
    else:
        print("Entry not found.")

# Main menu for the Gardening Journal App
def gardening_journal_menu():
    while True:
        print("\nGardening Journal Menu:")
        print("1. Add a journal entry")
        print("2. View all journal entries")
        print("3. Delete a journal entry")
        print("4. Update a journal entry")

        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_journal_entry()
        elif choice == '2':
            view_journal_entries()
        elif choice == '3':
            delete_journal_entry()
        elif choice == '4':
            update_journal_entry()
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    gardening_journal_menu()
