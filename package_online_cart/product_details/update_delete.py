from product_details.entry_display import product_list
def update_product(name, new_name=None, new_price=None, new_quantity=None):
    for product in product_list:
        if product['name'].lower() == name.lower():
            if new_name:
                product['name'] = new_name
            if new_price is not None:
                product['price'] = new_price
            if new_quantity is not None:
                product['quantity'] = new_quantity
            print(f"Product '{name}' updated successfully.")
            return
    print(f"Product '{name}' not found.")
def delete_product(name):
    global product_list
    for product in product_list:
        if product['name'].lower() == name.lower():
            product_list.remove(product)
            print(f"Product '{name}' deleted successfully.")
            return
    print(f"Product '{name}' not found.")
