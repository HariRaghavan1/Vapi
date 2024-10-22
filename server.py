# server.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import re
from math import factorial

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

def compute_math_operation(operation, operands):
    print("compute_math_operation function called")
    print(f"Operation: {operation}")
    print(f"Operands: {operands}")

    if operation.lower() == 'evaluate':
        # Join operands into a single expression string
        expression = ''.join(operands)
        print(f"Expression before factorial handling: {expression}")
        if '!' in expression:
            # Handle factorials
            expression = re.sub(r'(\d+)!', lambda match: str(factorial(int(match.group(1)))), expression)
            print(f"Expression after factorial handling: {expression}")
        try:
            # Safely evaluate the expression
            result = eval(expression)
            print(f"Evaluating expression: {expression}")
            print(f"Computation result: {result}")
            return {"expression": expression, "result": result}
        except Exception as e:
            print(f"Error in computation: {str(e)}")
            return {"error": str(e)}
    else:
        print("Unsupported operation")
        return {"error": "Unsupported operation"}

@app.route('/process', methods=['POST'])
def process():
    print("Received a request to /process")
    data = request.json
    print(f"Request JSON data: {data}")
    operation = data.get('operation', '')
    operands = data.get('operands', [])
    result = compute_math_operation(operation, operands)
    print(f"Returning result: {result}")
    return jsonify(result)

# Explicitly handle OPTIONS requests
@app.route('/process', methods=['OPTIONS'])
def handle_options():
    return '', 200

if __name__ == '__main__':
    app.run(port=5000)
