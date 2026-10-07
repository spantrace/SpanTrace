
from supervisor import supervise
from refund import process_refund


# ==========================================
# AI PRIVACY SUPERVISOR
# ==========================================

def privacy_system():

    print()
    print("===================================")
    print("       AI PRIVACY SUPERVISOR")
    print("===================================")

    while True:

        user_input = input("Enter text (or type 'back'): ")

        if user_input.lower() == "back":
            break

        result = supervise(user_input)

        if not result["allowed"]:

            print()
            print("BLOCKED:")
            print(result["message"])

        else:

            print()
            print("Detected:", result["findings"])
            print("AI WOULD RECEIVE:")
            print(result["message"])


# ==========================================
# REFUND SYSTEM
# ==========================================

def refund_system():

    print()
    print("===================================")
    print("          FAKE REFUND SYSTEM")
    print("===================================")
    print("Refunds over $100 are rejected.")
    print()

    while True:

        user_input = input("Enter refund amount (or type 'back'): ")

        if user_input.lower() == "back":
            break

        try:

            amount = float(user_input)

            if amount < 0:

                print("REJECTED: Amount cannot be negative.")

            else:

                print(process_refund(amount))

        except ValueError:

            print("Please enter a number.")


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print()
    print("===================================")
    print("       MY SECURITY PROGRAM")
    print("===================================")
    print("1. AI Privacy Supervisor")
    print("2. Refund System")
    print("3. Exit")
    print("===================================")

    choice = input("Choose an option: ")

    if choice == "1":

        privacy_system()

    elif choice == "2":

        refund_system()

    elif choice == "3":

        print("Goodbye!")
        break

    else:

        print("Invalid option.")