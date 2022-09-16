# Project 7 - Create a Web Application for an ETF Analyzer

---

## Technologies

Technologies used to complete this project include:

a) Programming Language: Python version 3.9.12 (this application will be stable for Python versions 3.7 and above)

b) Libraries and frameworks: I used following Python libraries and frameworks to complete this project
 - Pandas
 - pathlib, specifically the Path() function
 - Numpy
 - Hvplot.pandas
 - SQLAlchemy

c) Operating Systems: This application was created in Windows 10.

d) Database: The data is stored in SQLite database

---

## Installation Guide

Before running the application, first import the following libraries:
    
    import numpy as np
    import pandas as pd
    import hvplot.pandas
    import sqlalchemy

Also ensure that connection is made to SQLite database using sqlalchemy's "create_engine()" function.

Additionally, the database must already have four tables already populated with the data. The four tables should be - "GDOT", "GS", "PYPL", & "SQ".

Finally, we use Voila package to convert our script into a web application.

---

## Usage

1) We start by collecting historical data for four assets in the FinTech ETF - GDOT (Green Dot Corporation), GS (Goldman Sachs Group Inc), PYPL (PayPal Holdings Inc), & SQ (Block Inc). These data are saved in a SQLite database. We'll use SQL queries to retrieve the data from the database and convert the data into a Pandas DataFrame.

2) We then go to the next phase. We analyze and plot the closing prices, daily returns, and cumulative returns for only one stock - PYPL. We retrieve PYPL data using optimized SQL queries

3) We then combine daily returns for all stocks into a single DataFrame. We use SQL Joins query to join daily returns data for each stock from multiple tables. 

4) We finally analyze the entire FinTech ETF Portfolio - 
    a) We calculate the average daily returns for all stocks.
    b) We calculate and plot the annualized returns.
    c) We calculate and plot the cumulative returns.

5) We finally deploy these analyses into a web application using Voila library. The following are screenshots of how the web application looks when deployed locally on my machine - 


 
 ![screenshot_1](https://user-images.githubusercontent.com/109806489/190547178-32bd1cf6-89f3-4d3d-8b16-f3ec0d67b8e8.png)

 

![screenshot_2](https://user-images.githubusercontent.com/109806489/190547243-2d6df488-6d3d-4e84-892b-092a58e2f023.png)

 ![screenshot_3](https://user-images.githubusercontent.com/109806489/190547249-a33e8c21-54fb-45b3-8d93-cb3f14d284d9.png)

 
 ![screenshot_4](https://user-images.githubusercontent.com/109806489/190547258-533e5714-407e-41ac-a09a-3f5894e4859a.png)
![screenshot_5](https://user-images.githubusercontent.com/109806489/190547262-78c19513-c55e-47e3-880c-2a1e2c5bd097.png)

![screenshot_6](https://user-images.githubusercontent.com/109806489/190547276-c7b625a3-3af7-48b0-be7d-54bd05875141.png)



![screenshot_7](https://user-images.githubusercontent.com/109806489/190547290-f3fef5c5-5ff2-49d4-a05c-665cd945342f.png)



![screenshot_8](https://user-images.githubusercontent.com/109806489/190547296-ae39b4e5-cdcc-4777-bac6-14d45bcb8d6d.png)



---

## Contributors

 - Main contribution - Aanchal Khanna
 - LinkedIn Profile - https://www.linkedin.com/in/aanchal-khanna-7b126721b/

---

## License

The license used for this project is "MIT License"
