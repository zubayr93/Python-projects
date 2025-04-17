from customer import Customer
import db_manager

def main():
    db_manager.create_table()
    print("Customer Management System")
    
    while True:
        print("\n1. Add Customer\n2. View All\n3. Exit")
        choice = input("Select Option \n")
        
        if choice == "1":
            name = input("Name: ") 
            email = input("Email: ")
            phone = input("Phone: ")
            customer = Customer(name,email,phone)
            db_manager.add_customer(customer)
            print("CUstomer Added")
            
        elif choice == "2":
            customers = db_manager.get_all_customers()
            for c in customers:
                print (c)
        
        elif choice == "3":
            break
        
if __name__ == "__main__":
    main() 