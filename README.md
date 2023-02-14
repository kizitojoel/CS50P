# CS50P
Final Project for CS50 Introduction to Principles of Programming using Python.

## Initial Launch
The goal of this project is to design a real time currency trading application to be run from the Command Line Interface. The API used is
[Python Exchange Rate API](https://www.exchangerate-api.com/docs/python-currency-api) which generates exchange rates from the dollar to other currencies. Future updates will involve Graphical User Interfaces with the use of libraries like Tkinter or even Pygame. _To be explored_

## Added Functionality
The application is to have three main uses:
- Buying
- Quoting
- Selling

The users buying and selling transactions are to be stored in a CSV file along with time and date of transactions. This is to simulate currency trading as the value of currencies will be realtime thanks to the [Python Exchange Rate API](https://www.exchangerate-api.com/docs/python-currency-api).

For testing, each user will begin with $10,000 and progress while making transactions and storing each transaction in memory. That way, a user can grow a portfolio over time.

_Further functionality to be explored_

## Functions

## Problems Encountered
1. ### Limited number of API requests

The [Python Exchange Rate API](https://www.exchangerate-api.com/docs/python-currency-api) only offers 1500 requests per month

2. ### Implementing different functions for the buy and sell

The buy function will store cost in negative values to indicate that money is going out. It will however store quantity in positive values to indicate that currency is being bought, or rather is coming in. Better representation to be researched

3. ### Initialising the csv file once only
