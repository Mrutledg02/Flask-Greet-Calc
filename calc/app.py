# Put your app in here.
'''
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    """Perform addition with query parameters a and b."""
    a = float(request.args.get('a',0))
    b = float(request.args.get('b',0))
    result = add(a,b)
    return str(result)

@app.route('/sub')
def subtraction():
    """Perform subtraction with query parameters a and b."""
    a = float(request.args.get('a',0))
    b = float(request.args.get('b',0))
    result = sub(a,b)
    return str(result)

@app.route('/mult')
def multiplication():
    """Perform multiplication with query parameters a and b."""
    a = float(request.args.get('a',1))
    b = float(request.args.get('b',1))
    result = mult(a,b)
    return str(result)

@app.route('/div')
def dividion():
    """Perform division with query parameters a and b."""
    a = float(request.args.get('a',1))
    b = float(request.args.get('b',1))

    if b == 0:
        return "Error: Division by zero is not allowed."
    
    result = div(a,b)
    return str(result)

if __name__=='__main__':
    app.run(debug=True)
'''

#Further Study
from flask import Flask, request, abort
from operations import add, sub, mult, div

app = Flask(__name__)

#Dictionary to map operation names to corresponding functions
operations_dict = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div,
}

@app.route('/math/<operation>')
def math_operation(operation):
    '''Perform math operations with query parameters a and b.'''
    # Check if the requested operation is valid
    if operation not in operations_dict:
        abort(404) #Operation not found

    # Get the function corresponding to the requested operation
    operation_function = operations_dict[operation]

    #Get values of a and b from query parameters with default values
    a = float(request.args.get('a',1))
    b = float(request.args.get('b',1))

    try:
        #perform the math operation and return the result
        result = operation_function(a,b)
        return str(result)
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)