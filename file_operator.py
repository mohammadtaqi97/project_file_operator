import datetime
import os
class Journalmanager:
    def __init__(self,filename = "journal.txt"):
        self.filename = filename

# Adding New Entry:
    def add_entry(self,entry_text):
            timestamp = datetime.datetime.now()
            try:
                 with open(self.filename,"a") as f:
                      f.write(f"[{timestamp}]{entry_text} \n")
            except PermissionError:
                 print("There is no permission for writing file")
            except Exception as e:
                 print("General Error")
            finally:
                print("Entry Added Successfully")
    def view_entries(self):
        try:
            with open(self.filename,"r") as f:
                 content = f.read()
                 print(content)
        except FileNotFoundError:
             print("No journal entries found ")
        except Exception as e:
             print("Error reading file")
    def search_entries(self,keyword):
        try:
              with open(self.filename,"r") as f:
                    lines = f.readlines()
                    found = False
                    for line in lines:
                        if keyword.lower() in line.lower():
                             print(line)
                             found = True
                    if not found:
                         print("Text didn't found")
        except FileNotFoundError:
            print("No journal file found")          
    def delete_all(self):
        confirm = input("Are you sure you want to delete all entries?(yes/no): ")
        if confirm.lower() == "yes":
            try:
                os.remove(self.filename)
                print("All files deleted!")
            except FileNotFoundError:
                print("No journal file exists to delete")
        else:
                print("Deletion cancelled")


manager = Journalmanager()
print("_____Welcome to journal manager_____")
while True:
    print("1. Add a New Entry")
    print("2. View all Entries")
    print("3. Search for an Entry")
    print("4. Delete all Entries")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Add a New Entry: ")
        text = input("Enter your journal entry: ")
        manager.add_entry(text)

    elif choice == 2:
        print("View all Entries: ")
        manager.view_entries()
        
    elif choice == 3:
        print("Search for an Entry: ")
        keyword = input("Enter keyword to search: ")
        manager.search_entries(keyword)

    elif choice == 4:
        print("Delete all Entries: ")
        manager.delete_all()

    elif choice == 5:
        print("GoodBye!")
        break

    else:
        print("Invalid choice, please try again")

