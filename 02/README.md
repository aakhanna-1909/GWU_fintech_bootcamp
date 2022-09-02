# Project - Loan Qualifier App

This project builds a Loan Qualifier App. This app can be used to determine out of a list of 24 lenders, which one will extend loan to a customer based on following information about the customer:

    a) Customer's credit score, which represents the customer's creditworthiness based on his or her credit history, including the number of accounts opened, the amount of debt owed, and the repayment history. 

    b) Customer's debt-to-income ratio, which compares how much the customer owes to how much the customer earns per month

    c) The loan amount requested by the customer

    d) Customer's loan-to-value ratio, which compares the amount of loan requested by customer to the appraised value of the asset customer wants to buy.

---

## Technologies

Technologies used to complete this project include:

a) Programming Language: Python version 3.9.12 (this application will be stable for Python versions 3.7 and above)

b) Libraries and frameworks: I used following Python libraries and frameworks to complete this project"
 - sys
 - fire
 - questionary
 - pathlib, specifically the Path() function
 - csv

c) Operating Systems: This application was created in Windows 10.

d) I also created several custom functions in Python, some of which are listed out in "Usage" section.

---

## Installation Guide

Before running the application, first install the following dependencies:
    
    pip install fire
    pip install questionary

---

## Usage

1) The program starts by asking the user to input the location path of where the CSV file containing lender information is saved.



2) The program then asks the user to enter his or her information about:
    - Credit score
	- Amount of monthly debt
	- Gross monthly income
	- Desired loan amount
	- Value of home customer wishes to buy

 


3) Based on the values entered by the customer, the loan qualifier application performs the following actions: 
    - It calculates customer's monthly debt-to-income ratio using the custom function "calculate_monthly_debt_ratio()" and returns the ratio as the output..

    - It calculates customer's loan_to_value ratio using the custom function "calculate_loan_to_value_ratio()" and returns the ratio as the output.

    - It uses several calculations to filter and return the number of qualifying lenders that are willing to extend loan to the customer. The following custom-developed are used:
        - "filter_max_loan_size()": Compares the customer's desired loan against the bank's maximum loan size so that we can know which banks offer the loan amount requested by the customer.

        - "filter_credit_score()": Compares the customer's credit score to determine if it is equal to or greater than the minimum allowed credit score defined by the bank so that we can know which banks are willing to offer a loan to the customer.

        - "filter_debt_to_income()": Compares the customer's debt-to-income to determine if it is equal to or less than the maximum debt-to-income ratio allowed by the bank so that we can assess if the customer will have payment capacity according to the bank's criteria.

        - "filter_loan_to_value()": Compares the customer's loan-to-value to determine if it is equal to or less than the maximum loan-to-value ratio allowed by the bank so that we can assess if the customer's home value is worth enough as an asset to secure the loan.


    
4) The program then asks the user if he or she wants to save the qualifying loans to a CSV. 
	- If "Yes", the program asks the user to provide the location where he or she wants the CSV file to be saved.
	- If "No", the program ends.


---

## Contributors

 - Main contribution - Aanchal Khanna
 - LinkedIn Profile - https://www.linkedin.com/in/aanchal-khanna-7b126721b/

---

## License

The license used for this project is "MIT License"