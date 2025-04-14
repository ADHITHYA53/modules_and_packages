from product_details.entry_display import add_product, display_product
from product_details.update_delete import update_product, delete_product
from purchase_billing.purchase import purchase

def main():
    while True:
        print("\n====== Online Cart Menu ======")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Purchase Products")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            display_product()
        elif choice == '3':
            update_product()
        elif choice == '4':
            delete_product()
        elif choice == '5':
            purchase()
        elif choice == '6':
            print("Thank you for using Online Cart!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
