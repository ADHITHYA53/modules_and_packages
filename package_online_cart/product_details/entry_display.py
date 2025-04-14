product_list=[]  # empty list to store the data

def add_product():
    name = input("Enter the name of the product :")
    price = float(input("Enter the price of the product :"))
    quantity = int(input("Enter product quantity :"))
    product_list.append({"Name" : name , "Price" : price, "Quantity" : quantity })
    print(f"{name} added successfully")

def display_product():
    if not product:
        print("Product is not available")
    else:
        print("\nAvailable Products:")
        for idx, product in enumerate(product_list, start=1):
            print(f"{idx}. Name: {product['name']}, Price: ₹{product['price']}, Quantity: {product['quantity']}")
