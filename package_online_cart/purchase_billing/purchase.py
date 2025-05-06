from product_details.entry_display import product_list, display_product

def purchase():
    if not product_list:
        print("No products to purchase.")
        return
    display_product()
    cart = []
    while True:
        name = input("Enter product name to buy (or 'done' to checkout): ")
        if name.lower() == 'done':
            break
        found = None
        for p in product_list:
            if p['name'].lower() == name.lower():
                found = p
                break
        if not found:
            print("Product not found.")
            continue
        qty = int(input("Enter quantity: "))
        if qty > found['quantity']:
            print("Not enough stock.")
            continue
        cart.append({'name': found['name'], 'price': found['price'], 'quantity': qty})
        found['quantity'] -= qty
    if not cart:
        print("Cart is empty.")
        return
    print("\n --- BILL ---")
    total = 0
    for item in cart:
        cost = item['price'] * item['quantity']
        total += cost
        print(f"{item['name']} x {item['quantity']} = ₹{cost}")

    discount = 0.1 * total if total > 1000 else 0
    taxed_total = (total - discount) * 1.18

    print(f"Subtotal: ₹{total:.2f}")
    print(f"Discount: ₹{discount:.2f}")
    print(f"Tax (18%): ₹{(taxed_total - (total - discount)):.2f}")
    print(f"Final Amount: ₹{taxed_total:.2f}")
