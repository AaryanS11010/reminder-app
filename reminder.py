# Reminder Application

def display_menu():
    print("\nReminder Application")
    print("1. Add Reminder")
    print("2. View Reminders")
    print("3. Delete Reminder")
    print("4. Exit")

def add_reminder(reminders):
    reminder = input("Enter your reminder: ")
    reminders.append(reminder)
    print("Reminder added!")

def view_reminders(reminders):
    if reminders:
        print("\nYour Reminders:")
        for idx, reminder in enumerate(reminders, start=1):
            print(f"{idx}. {reminder}")
    else:
        print("No reminders to show.")

def delete_reminder(reminders):
    if reminders:
        view_reminders(reminders)
        reminder_number = int(input("Enter the number of the reminder to delete: "))
        if 1 <= reminder_number <= len(reminders):
            reminders.pop(reminder_number - 1)
            print("Reminder deleted!")
        else:
            print("Invalid number.")
    else:
        print("No reminders to delete.")

def main():
    reminders = []
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_reminder(reminders)
        elif choice == '2':
            view_reminders(reminders)
        elif choice == '3':
            delete_reminder(reminders)
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
