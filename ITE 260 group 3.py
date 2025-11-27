print("=================================================================")
print("           WELCOME TO BUBBLELICIOUS MILKTEA SHOP")
print("=================================================================")


prices = {"small": 35, "medium": 45, "large": 50}
flavors = ["okinawa", "taro", "chocolate", "cookies and cream"]


while True:
   print("\n[1] SEE MENU(S)")
   print("[2] BUY PRODUCT(S)")
   print("[3] EMPLOYEE MENU")
   print("[4] EXIT")


   try:
       option = int(input("Enter option [1-4]: "))
   except ValueError:
       print("Invalid input! Please enter a number between 1 and 4.")
       continue


   if option == 1:
       print("\n========= MENU =========")
       print("SIZES:")
       print("SMALL  - ₱35")
       print("MEDIUM - ₱45")
       print("LARGE  - ₱50")
       print("\nFLAVORS:")
       for f in flavors:
           print("•", f.title())
       print("========================")


   elif option == 2:
       if not flavors:
           print("No available products right now.")
           continue


       orders = []
       product_input = input("\nEnter flavor(s) you want (separate by space or comma): ").lower().replace(",", " ").split()


       joined_flavors = []
       i = 0
       while i < len(product_input):
           if i + 2 < len(product_input) and product_input[i] == "cookies" and product_input[i + 1] == "and" and product_input[i + 2] == "cream":
               joined_flavors.append("cookies and cream")
               i += 3
           else:
               joined_flavors.append(product_input[i])
               i += 1


       valid_flavors = [f for f in joined_flavors if f in flavors]
       invalid_flavors = [f for f in joined_flavors if f not in flavors]


       if invalid_flavors:
           print("Invalid flavor(s): ", ", ".join(invalid_flavors))
           continue


       for flavor in valid_flavors:
           size = input("Size for " + flavor.title() + " [small/medium/large]: ").strip().lower()
           if size not in prices:
               print("Invalid size for ", flavor.title(), "! Skipping this item.")
               continue


           try:
               quantity = int(input("How many cups?: "))
           except ValueError:
               print("Invalid quantity! Skipping this item.")
               continue


           subtotal = prices[size] * quantity
           orders.append({
               "flavor": flavor,
               "size": size,
               "quantity": quantity,
               "subtotal": subtotal
           })


       if not orders:
           print("No valid items ordered.")
           continue


       total = sum(item["subtotal"] for item in orders)
       print("Total amount: ₱", total)


       while True:
           try:
               payment = int(input("Customer Payment: ₱"))
           except ValueError:
               print("Please enter a valid amount.")
               continue


           if payment < 0:
               print("Invalid payment! Negative amounts are not accepted.")
               continue
           elif payment >= total:
               change = payment - total
               print("Change: ₱", change)
               print("Thanks for purchasing! Enjoy your milktea ")
               break
           else:
               print("Insufficient amount! Please try again.")


       print("\n========== RECEIPT ==========")
       print("BUBBLELICIOUS MILKTEA SHOP")
       print("----------------------------")
       for item in orders:
           print(item["flavor"].title(), "(", item["size"].capitalize(), ") x", item["quantity"], "= ₱", item["subtotal"])
       print("----------------------------")
       print("Total: ₱", total)
       print("Received: ₱", payment)
       print("Change: ₱", change)
       print("----------------------------")
       print("Mode of Payment: Cash")
       print("Serial No.: 12345")
       print("Thank you for supporting BUBBLELICIOUS!")
       print("==============================")


   elif option == 3:
       while True:
           print("\n========= EMPLOYEE MENU =========")
           print("[1] ADD NEW PRODUCT")
           print("[2] EDIT PRODUCT")
           print("[3] REMOVE PRODUCT")
           print("[4] BACK TO MAIN MENU")
           print("=================================")


           try:
               emp_option = int(input("Enter option [1-4]: "))
           except ValueError:
               print("Invalid input! Please enter a number between 1 and 4.")
               continue




           if emp_option == 1:
               new_flavor = input("Enter new product name: ").strip().lower()
               if new_flavor in flavors:
                   print("Product already exists!")
                   continue
               try:
                   small_price = int(input("Enter price for SMALL size: ₱"))
                   medium_price = int(input("Enter price for MEDIUM size: ₱"))
                   large_price = int(input("Enter price for LARGE size: ₱"))
               except ValueError:
                   print("Invalid input! Prices must be numbers.")
                   continue


               prices["small"] = small_price
               prices["medium"] = medium_price
               prices["large"] = large_price
               flavors.append(new_flavor)
               print("Product added successfully!")


           elif emp_option == 2:
               edit_flavor = input("Enter the product name to edit: ").strip().lower()
               if edit_flavor not in flavors:
                   print("Product not found!")
                   continue
               try:
                   new_small = int(input("New SMALL price (₱): "))
                   new_medium = int(input("New MEDIUM price (₱): "))
                   new_large = int(input("New LARGE price (₱): "))
               except ValueError:
                   print("Invalid input! Prices must be numbers.")
                   continue


               prices["small"] = new_small
               prices["medium"] = new_medium
               prices["large"] = new_large
               print("Product prices updated successfully!")


           elif emp_option == 3:
               remove_flavor = input("Enter product name to remove: ").strip().lower()
               if remove_flavor in flavors:
                   flavors.remove(remove_flavor)
                   print("Product removed successfully!")
               else:
                   print("Product not found!")


           elif emp_option == 4:
               print("Returning to main menu...")
               break


           else:
               print("Invalid option! Please choose between [1-4].")


   # ----------------- EXIT -----------------
   elif option == 4:
       print("Thank you for visiting BUBBLELICIOUS Milktea Shop! Goodbye ")
       break


   else:
       print("Invalid option! Please choose between [1-4].")


