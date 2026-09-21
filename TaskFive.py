total_bill = float(input("What is your bill please: "))
membership = input("Do you have a membership? Yes/No: ")

if total_bill >= 1000 and membership == "Yes":
    discount = total_bill * 0.10
    final_amount = total_bill - discount
    print("final amount =", final_amount)

if total_bill >= 1000 and membership == "No":
    discount = total_bill * 0.05
    final_amount = total_bill - discount
    print("final amount =", final_amount)

if total_bill < 1000:
    discount = total_bill * 0.00
    final_amount = total_bill - discount
    print("final amount =", final_amount)
