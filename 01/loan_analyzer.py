# coding: utf-8
import csv
from pathlib import Path

discount_rate = 0.20  #This is annual discount rate that will be used to calculate present value of different loans


# Part 1
loan_costs = [500, 600, 200, 1000, 450]

# Counting the number of loans in the list and printing it
number_of_loans = len(loan_costs)
print(f"The number of loans is {number_of_loans}")

# Determining the sum total of all loans and printing it
sum_of_loans = sum(loan_costs)
print(f"The sum total of all loans is ${sum_of_loans: .2f}")

# Calculating the Average loan amount and printing it
average_of_loans = sum_of_loans/number_of_loans
print(f"The average amount of the loans is ${average_of_loans: .2f}")



# Part 2
# We have a loan called "Loan" (saved in 'loan' dictionary)
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000}

# Extracting the Future Value and Remaining Months of Loan and printing them
loan_remaining_months = loan.get("remaining_months")
loan_future_value = loan.get("future_value")
print(f"The number of months remaining for the Loan is {loan_remaining_months} months")
print(f"The future value of the Loan is ${loan_future_value}")

# Creating a function to calculate the Present Value
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value/((1 + annual_discount_rate/12)**remaining_months)
    return present_value

# Calculating the Present Value of Loan using discount rate of 20% and printing it
loan_present_value = calculate_present_value(loan_future_value, loan_remaining_months, discount_rate)
print(f"The present value of the loan is ${loan_present_value: .2f}")

# Comparing the loan price with the present value and deciding if it is worthwhile to buy the loan
if loan_present_value >= loan.get("loan_price"):
    print("The loan is worth at least the cost to buy it")
else:
    print("The loan is too expensive and not worth the price.")


# Part 3
# We have another loan called "New Loan" (saved in 'new_loan' dictionary)
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000}

# Extracting the Future Value and Remaining Months of Loan and printing them
new_loan_remaining_months = new_loan.get("remaining_months")
new_loan_future_value = new_loan.get("future_value")

# Calculating the present value of the New Loan using the function "calculate_present_value" that we used in Part 2. We will use same discount rate of 20%
new_loan_present_value = calculate_present_value(new_loan_future_value, new_loan_remaining_months, discount_rate)
print(f"The present value of the New Loan is ${new_loan_present_value: .2f}")



# Part 4
# We have a series of loans saved as a list of dictionaries called "loans"
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    }]

# Creating an empty list called `inexpensive_loans` where the inexpensive loans will be stored
inexpensive_loans = []

# Looping through all the loans and appending any loan that cost $500 or less to the `inexpensive_loans` list
for each_loan in loans:
    each_loan_price = each_loan.get("loan_price")
    if each_loan_price <= 500:
        inexpensive_loans.append(each_loan_price)

# Printing the `inexpensive_loans` list
print(f"The list of inexpensive loans is: {inexpensive_loans}")


#Part 5
# Header for the CSV file
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Output file path
output_path = Path("inexpensive_loans.csv")

# Writing the "loan_price", "remaining_months", "repayment_interval", and "future_value" for those loans that were determined to be Inexpensive Loans

with open(output_path, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for each_val in inexpensive_loans:
        for each_dict in loans:
            if each_dict.get("loan_price") == each_val:
                csvwriter.writerow(each_dict.values())




