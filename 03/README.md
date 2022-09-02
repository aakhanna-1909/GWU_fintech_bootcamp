# Project - Finding arbitrage opportunities for Bitcoin traded on two different exchanges 

This project attempts to find arbitrage opportunities for Bitcoin traded on two exchanges: Bitstamp and Coinbase. We'll look at historical data for Bitcoin traded on both these exchanges to determine if we can make profit on simultaneous price dislocations in those exchanges. To make profit from price dislocations, we'll use  the strategy of buying Bitcoin from the lower priced exchange and selling it on the higher priced exchange simultaneously without holding onto it.

---

## Technologies

Technologies used to complete this project include:

a) Programming Language: Python version 3.9.12 (this application will be stable for Python versions 3.7 and above)

b) Libraries and frameworks: I used following Python libraries and frameworks to complete this project
 - Pandas
 - pathlib, specifically the Path() function

c) Operating Systems: This application was created in Windows 10.

---

## Installation Guide

Before running the application, first import the following libraries:
    
    import pandas as pd
    from pathlib import Path()

---

## Usage

1) We start by collecting data historical data for Bitcoin traded on Bitstamp and Coinbase. We have two CSV files from which we'll import the data to Pandas dataframe.

2)  We then go to the next phase of preparing the data for further analysis. We first remove the $ sign from the close price and make sure that all price variables are of the correct data type (float). We then make sure that there are no empty or null values and duplicate values in our dataframes.


3) We finally analyze the data, create summary statistics, visualizations, and calculate the arbitrage profits.

---

## Contributors

 - Main contribution - Aanchal Khanna
 - LinkedIn Profile - https://www.linkedin.com/in/aanchal-khanna-7b126721b/

---

## License

The license used for this project is "MIT License"