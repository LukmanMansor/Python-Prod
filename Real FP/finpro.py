# Import flask, jsonify and render_template module from FLask package
from flask import Flask, jsonify, render_template
# Calling another script from the same directory
import user
# Import requests module
import requests

# Initializing
app = Flask(__name__)

# Calling variable from another script
name = user.username
roles = user.role

# Creating main route
@app.route('/')
def wazap(): 
	# Use f-string format and single line html format in return
	return f"<h1>Hello World.</h1> <p>Great to have you, {name}! You are {roles} of this project.</p> <img src = 'https://i.gifer.com/UJr.gif' width='300' height='200'>"

# Obtain data from API
@app.route('/getquo')
def getquo():
	quote = requests.get('https://quote-garden.onrender.com/api/v3/quotes')
	# Convert the data into json form data
	quote_data = quote.json()
	return quote_data

# Creating list of quote author from the API
@app.route('/quodata')
def quodata ():
	# Use getquo function from above to get results from the API
	quodat = getquo()
	# Creating empty list to be returned
	whoquo = []
	# Code to make a list of author and quote
	for i in quodat['data']:
		whoquo.append(i['quoteAuthor'])
	# Covert list into string in json 
	return jsonify(whoquo)

# Creating dynamic url
@app.route('/quote/<author>')
def quo_author (author):
	# Use getquo function from above to get results from the API
	quotes = getquo()
	# Creating variabe with empty string to get falsey
	author_quo = ""
	# Code for matching author and their quote
	for i in quotes['data']:
		if i["quoteAuthor"] == author:
			# To make author_quo variable become truethy
			author_quo = i["quoteText"]
	# Code to asamble author and their qoute within single line
	if author_quo:
		return f"{author} once said that \"{author_quo}\" about age."
	else:
		return f"There are no such {author} leaving any quotes. Please use correct authors or check your spelling and caps."

# Obtain data from API
@app.route('/forex')
def forex():
	money = requests.get('https://open.er-api.com/v6/latest/USD')
	# Convert the data into json form data
	money_data = money.json()
	return money_data

# Code to extract exchange rates dictionary into a new variable
@app.route('/forex/rates')
def rates():
	# Use forex function from above to get results from the API
	rate = forex()
	exc_rate = rate['rates']
	return exc_rate

# Code to compare other currency to USD
@app.route('/forex/exchange')
def exc_usd():
    # Use rate function from above to get dictionary of rates
    usd = rates()
    # Use while loop to get input from the user as many times
    while True:
        # Use try function to eliminate numbers in the input
        try:
            # Get input from the user
            country = input("Please enter your preferred country currency (3-letter code) or 'exit' to quit: ").upper()           
            # Set a condition to break out of the loop
            if country == 'EXIT':
                break
            # Code to check if the input contains only 3 alphabetic characters
            if country.isalpha() and len(country) == 3:
                # Code to compare other currencies and USD
                if country in usd:
                    exchange_rate = usd[country]
                    return f"1 USD equals {exchange_rate} {country}"
                else:
                	# If user input 3 alpabert that are not in usd variabe key or numbers
                    print("Invalid currency code. Please enter a valid 3-letter currency code.")
            else:
            	# If user input length more or less than 3
                print("Invalid input. Please enter a valid 3-letter currency code.")
        # Code to catch any error outside of if else statement
        except Exception as e:
            print(f"An error occurred: {e}")


# Create a route  and function using html and css file
@app.route('/readhtml')
def read_html():
	# use render_tempate function to linking the file
	return render_template('index.html')	


# Code create environment simulataneusly edit and view
if __name__ == '__main__':
	app.run(debug = True)