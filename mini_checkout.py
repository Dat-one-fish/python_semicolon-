psudocode = """
collect a name from user

collect the product pruchased from user

collect the price of product

ask if used wishes to add another product 

if yes 

repeat process 

if no 

calculate total

then print it as reciept 

"""
print (psudocode)

print ("---____________________________________________________________________________________________________________________________________________________________________________________________________________________________---")



sub_total = 0
cashier_name = input( "enter your name: ")

name_input = input( "Enter Customer's Name:" )

product_input = input( "Enter Product Name:" )

quantity_product_input = int( input( "Enter quantity of" + " " + product_input + ":" ) )

price_product_input = int( input( "Enter price of" + " " + product_input + ":" ) )

total_cost = quantity_product_input * price_product_input

add_more = input( "Do you wish to proceed? (Y/N):" ) 
sub_total += total_cost

if(add_more == "y" ):
    while (add_more == "y"):

        product_input = input( "Enter Product Name:" )

        quantity_product_input = int( input( "Enter quantity of" + " " + product_input + ":" ) )

        price_product_input = int( input( "Enter price of" + " " + product_input + ":" ) )

        add_more = input( "Do you wish to proceed? (Y/N):" ) 
        
        total_cost = quantity_product_input * price_product_input
        sub_total += total_cost

if (add_more == "n"):
   

    display = (f"""

========ODOGWU SUPERMARKET========

Cashier's Name: {cashier_name}
Customer's Name: {name_input}


Total Item Cost: {sub_total}
Payment option: CARD
=========HAVE A NICE DAY=========

""")
print( display )

    
     
  
    


 
   





