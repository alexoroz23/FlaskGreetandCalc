# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add():
    """
    Route function for adding two numbers.
    Expects 'a' and 'b' to be passed as query parameters.
    """
    # Retrieve 'a' and 'b' from the URL query parameters and convert to integers
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    # Call the 'add' function from the 'operations' module with 'a' and 'b' as arguments
    result = operations.add(a, b)
    
    # Return the result as a string
    return str(result)

@app.route('/sub')
def sub():
    """
    Route function for subtracting two numbers.
    Expects 'a' and 'b' to be passed as query parameters.
    """
    # Retrieve 'a' and 'b' from the URL query parameters and convert to integers
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    # Call the 'sub' function from the 'operations' module with 'a' and 'b' as arguments
    result = operations.sub(a, b)
    
    # Return the result as a string
    return str(result)

@app.route('/mult')
def mult():
    """
    Route function for multiplying two numbers.
    Expects 'a' and 'b' to be passed as query parameters.
    """
    # Retrieve 'a' and 'b' from the URL query parameters and convert to integers
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    # Call the 'mult' function from the 'operations' module with 'a' and 'b' as arguments
    result = operations.mult(a, b)
    
    # Return the result as a string
    return str(result)

@app.route('/div')
def div():
    """
    Route function for dividing two numbers.
    Expects 'a' and 'b' to be passed as query parameters.
    """
    # Retrieve 'a' and 'b' from the URL query parameters and convert to integers
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    # Call the 'div' function from the 'operations' module with 'a' and 'b' as arguments
    result = operations.div(a, b)
    
    # Return the result as a string
    return str(result)