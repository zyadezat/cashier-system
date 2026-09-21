import time
products = ["Laptop", "Phone", "Headphones", "Mouse"]
prices = [15000, 8000, 1500, 300]
total_products = []
total_prices = []
all_total=0
# display_products -------->function
def display(x):
    print("\n","-"*10,f"{x} list".title(),"-"*10)
    for i in range(len(products)):
        print(f"{i+1}. {products[i]:<11}: {prices[i]:<6} EGP")
# add_massage -------->function
def added():
    print("✅ Product added successfully!".title())
# append_to_(products, prices)_list -------->function
def total(x, y):
    total_products.append(x)
    total_prices.append(y)
# cart_type -------->function
def cart(x):
    print("\n","-"*10,f"{x} list".title(),"-"*10)
    for i in range(len(total_products)):
                print(f"{i+1}. {total_products[i]:<11}: {total_prices[i]} EGP")
print("-"*10,"💲 welcome to cashier app".title(),"-"*10)
while True:
    print("\n","-"*10,"main list".title(),"-"*10)
    print("1. show product".title())
    print("2. add to cart".title())
    print("3. delete product".title())
    print("4. view cart & total".title())
    print("5. checkout & exit".title())
    try:
        choose = int(input("📋 what do you to do ? "))
        # show_product
        if choose==1:
            display("Item")
            time.sleep(1.5)
        
        # add_to_cart
        elif choose==2:
            display("Add")
            try:
                add = int(input("choose item number from available products: ".title()))
                if 1 <= add <= len(products): #----------->
                    added()
                    total(products[add-1],prices[add-1])
                    all_total+=prices[add-1]
                else:
                    print("invalid number! try again.".title())

            except ValueError:
                print("invalid choice! must be valid number.".title())
        
        # delete_product
        elif choose==3:
            if not total_products:
                print(f"❌ no products yet. ".title())
                continue
            cart("Delete")
            try:
                delete = int(input("delete item by number: ".title()))
                if delete < 1 or delete > len(total_products):
                    print("invalid choice! must be valid number.".title())
                else:
                    print(f"🗑️   Product Deleted: {total_products[delete-1]} : {total_prices[delete-1]} EGP")
                    all_total-=total_prices[delete-1]
                    total_products.pop(delete-1)
                    total_prices.pop(delete-1)

            except ValueError:
                print("invalid choice! must be valid number.".title())

        # view_cart_&_total
        elif choose==4:
            if not total_products:
                print(f"❌ no products yet. ".title())
                continue
            cart("Cart")
        
        # checkout_&_exit
        elif choose==5:
            cart("Checkout")
            print(f"\ntotal price is : {all_total} EGP")
            print(f"👋 Thank you for shopping with us!".title())
            input("click enter to end the program. ".title())
            break
        
        else:
            print("invalid choice! must be valid number.".title())
            
    except ValueError:
        print("invalid choice! must be valid number.".title())
