from email_handler import handle_email
from database import create_database, get_available_items

def main():
    print("Welcome to the Film Equipment Inquiry System!")
    create_database()
    print("Database created with sample data (if it didn't exist).")
    
    available_items = get_available_items()
    print("Here are some available products:")
    for item in available_items:
        print(f" - {item['item']} at ${item['price']}")

    while True:
        body = input("Enter the content of the email: ")
        response = handle_email('', body)
        print(response)

if __name__ == "__main__":
    main()
