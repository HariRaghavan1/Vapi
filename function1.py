#FIRST ITERATION: TWO OPERANDS
# from openai import OpenAI
# import json
# client = OpenAI()


# def compute_math_operation(operation, operand1, operand2):
    
#     """Compute the specified mathematical operation between two numbers"""
#     if "sum" in operation.lower():
#         return json.dumps({"operation": f"{operand1}+{operand2}", "answer": float(operand1)+float(operand2)})
#     elif "product" in operation.lower():
#         return json.dumps({"operation": f"{operand1}*{operand2}", "answer": float(operand1)*float(operand2)})
#     elif "quotient" in operation.lower():
#         return json.dumps({"operation": f"{operand1}/{operand2}", "answer": float(operand1)/float(operand2)})
#     else:
#         return json.dumps({"numbers": f"{operand1}, {operand2}", "operation": "unknown"})


# def run_conversation():
#     x=input("Enter an operation to calculate: ")

#     # Step 1: send the conversation and available functions to the model
#     messages = [{"role": "user", "content": x}]
    
#     tools = [
#         {
#             "type": "function",
#             "function": {
#                 "name": "compute_math_operation",
#                 "description": "Compute the specified mathematical operation between two numbers",
#                 "parameters": {
#                     "type": "object",
#                     "properties": {
#                         "operation": {
#                             "type": "string",
#                             "description": "Either addition, multiplication, or division. Do not default to calculating the operation if it is not one of these three",
#                         },
#                     "operand1": {
#                             "type": "string",
#                             "description": "The first operand for the operator",
#                         },
#                     "operand2": {
#                             "type": "string",
#                             "description": "The second operand for the operator",
#                         },        
#                     },
#                     "required": ["operation","operand1", "operand2"],
#                 },
#             },
#         }
#     ]
    
#     response = client.chat.completions.create(
#         model="gpt-4",
#         messages=messages,
#         tools=tools,
#         tool_choice="auto",  # auto is default, but we'll be explicit
#     )
#     response_message = response.choices[0].message
    
#     tool_calls = response_message.tool_calls
#     if not tool_calls:
#         return "Operation not supported."
#     # Step 2: check if the model wanted to call a function
#     if tool_calls:
#         # Step 3: call the function
#         available_functions = {
#             "compute_math_operation": compute_math_operation,
#         }
#         messages.append(response_message)  # extend conversation with assistant's reply
#         # Step 4: send the info for each function call and function response to the model
#         for tool_call in tool_calls:
#             function_name = tool_call.function.name
#             function_to_call = available_functions[function_name]
#             function_args = json.loads(tool_call.function.arguments)
#             function_response = function_to_call(
#                 operation=function_args.get("operation"),
#                 operand1=function_args.get("operand1"),
#                 operand2=function_args.get("operand2")
#             )
#             messages.append(
#                 {
#                     "tool_call_id": tool_call.id,
#                     "role": "tool",
#                     "name": function_name,
#                     "content": function_response,
#                 }
#             )  # extend conversation with function response
#         second_response = client.chat.completions.create(
#             model="gpt-4",
#             messages=messages,
#         )  # get a new response from the model where it can see the function response
#         #return second_response
#         final_message = second_response.choices[0].message
#         return final_message.content  # Access the content directly

        


# print(run_conversation())

#SECOND ITERATION: UNLIMITED OPERANDS BUT SUBTRACTION DOES NOT ALWAYS CORRECTLY FUNCTION

# from openai import OpenAI
# import json

# client = OpenAI()

# def compute_math_operation(operation, operands):
#     """Compute the specified mathematical operation between a list of numbers"""
#     if not operands or len(operands) < 2:
#         return json.dumps({"operation": "unknown", "result": "Insufficient operands"})

#     # Convert operands to floats
#     operands = [float(op) for op in operands]

#     # Perform the specified operation
#     #Interpret 'subtraction' as addition of a negative number.
#     if "sum" in operation.lower():
#         result = sum(operands)
#     elif "product" in operation.lower():
#         result = 1
#         for op in operands:
#             result *= op
#     elif "quotient" in operation.lower():
#         result = operands[0]
#         for op in operands[1:]:
#             if op == 0:
#                 return json.dumps({"operation": "division", "result": "Division by zero"})
#             result /= op
#     else:
#         return json.dumps({"operation": "unknown", "result": "Operation not supported"})

#     return json.dumps({"operation": operation, "result": result})

# def run_conversation():
#     x = input("Enter an operation to calculate: ")

#     # Step 1: send the conversation and available functions to the model
#     messages = [{"role": "user", "content": x}]
    
#     tools = [
#         {
#             "type": "function",
#             "function": {
#                 "name": "compute_math_operation",
#                 "description": "Compute the specified mathematical operation between a list of numbers",
#                 "parameters": {
#                     "type": "object",
#                     "properties": {
#                         "operation": {
#                             "type": "string",
#                             "description": "Either addition, multiplication, or division or subtraction, where subtraction is considered addition of a negative value. Do not default to calculating the operation if it is not one of these four.",
#                         },
#                         "operands": {
#                             "type": "array",
#                             "items": {
#                                 "type": "string",
#                                 "description": "The operands for the operation"
#                             },
#                             "description": "The list of operands for the operation",
#                             "minItems": 2
#                         },
#                     },
#                     "required": ["operation", "operands"],
#                 },
#             },
#         }
#     ]
    
#     response = client.chat.completions.create(
#         model="gpt-4",
#         messages=messages,
#         tools=tools,
#         tool_choice="auto",  # auto is default, but we'll be explicit
#     )
    
#     response_message = response.choices[0].message
    
#     tool_calls = response_message.tool_calls
#     if not tool_calls:
#         return "Operation not supported."

#     # Step 2: check if the model wanted to call a function
#     if tool_calls:
#         # Step 3: call the function
#         available_functions = {
#             "compute_math_operation": compute_math_operation,
#         }
#         messages.append(response_message)  # extend conversation with assistant's reply
#         # Step 4: send the info for each function call and function response to the model
#         for tool_call in tool_calls:
#             function_name = tool_call.function.name
#             function_to_call = available_functions[function_name]
#             function_args = json.loads(tool_call.function.arguments)
#             function_response = function_to_call(
#                 operation=function_args.get("operation"),
#                 operands=function_args.get("operands")
#             )
#             messages.append(
#                 {
#                     "tool_call_id": tool_call.id,
#                     "role": "tool",
#                     "name": function_name,
#                     "content": function_response,
#                 }
#             )
        
#         second_response = client.chat.completions.create(
#             model="gpt-4",
#             messages=messages,
#         )
        
#         # Extract and return the final response
#         reply_content = second_response.choices[0].message.content
#         return reply_content

# print(run_conversation())

#THIRD ITERATION: UNLIMITED OPERANDS, AND MANY DIFFERENT MATHEMATICAL OPERATIONS CAN BE PERFORMED


# from openai import OpenAI
# import json
# import re
# from math import factorial

# client = OpenAI()

# def compute_math_operation(operation, operands):
#     """Compute the specified mathematical operation between a list of numbers"""
#     print("compute_math_operation function called")
    
#     if operation.lower() == 'evaluate':
#         # Join operands into a single expression string
#         expression = ''.join(operands)

#         # Check and replace any factorial operations in the expression
#         if '!' in expression:
#             expression = re.sub(r'(\d+)!', lambda match: str(factorial(int(match.group(1)))), expression)

#         try:
#             # Safely evaluate the expression
#             result = eval(expression)
#             return json.dumps({"expression": expression, "result": result})
#         except Exception as e:
#             return json.dumps({"error": str(e)})
#     else:
#         return json.dumps({"error": "Unsupported operation"})

# def run_conversation():
#     x = input("Enter an operation to calculate: ")
    
#     # Step 1: send the conversation and available functions to the model
#     messages = [{"role": "user", "content": x}]
    
#     tools = [
#         {
#             "type": "function",
#             "function": {
#                 "name": "compute_math_operation",
#                 "description": "Compute any mathematical expression, including operations like addition, subtraction, multiplication, division, and factorial (e.g., 10!).",
#                 "parameters": {
#                     "type": "object",
#                     "properties": {
#                         "operation": {
#                             "type": "string",
#                             "description": "Specify 'evaluate' for evaluating a mathematical expression.",
#                         },
#                         "operands": {
#                             "type": "array",
#                             "description": "A list of numbers and operators forming the mathematical expression.",
#                             "items": {
#                                 "type": "string"
#                             }
#                         }
#                     },
#                     "required": ["operation", "operands"],
#                 },
#             },
#         }
#     ]
    
#     response = client.chat.completions.create(
#         model="gpt-4",
#         messages=messages,
#         tools=tools,
#         tool_choice="auto",  # auto is default, but we'll be explicit
#     )
    
#     response_message = response.choices[0].message
    
#     tool_calls = response_message.tool_calls
#     if not tool_calls:
#         return "Operation not supported."
    
#     # Step 2: check if the model wanted to call a function
#     if tool_calls:
#         # Step 3: call the function
#         available_functions = {
#             "compute_math_operation": compute_math_operation,
#         }
#         messages.append(response_message)  # extend conversation with assistant's reply
#         # Step 4: send the info for each function call and function response to the model
#         for tool_call in tool_calls:
#             function_name = tool_call.function.name
#             function_to_call = available_functions[function_name]
#             function_args = json.loads(tool_call.function.arguments)
#             function_response = function_to_call(
#                 operation=function_args.get("operation"),
#                 operands=function_args.get("operands", [])
#             )
#             messages.append(
#                 {
#                     "tool_call_id": tool_call.id,
#                     "role": "tool",
#                     "name": function_name,
#                     "content": function_response,
#                 }
#             )  # extend conversation with function response
#         second_response = client.chat.completions.create(
#             model="gpt-4",
#             messages=messages,
#         )  # get a new response from the model where it can see the function response
        
#         # Extract and print the result
#         reply_content = second_response.choices[0].message.content
#         return reply_content

# print(run_conversation())
from openai import OpenAI
import json
import re
from math import factorial
from vapi_python import Vapi
vapi = Vapi(api_key='6ed49c62-97a4-41ba-ae7e-01f17ba0ce0f')


client = OpenAI()

def compute_math_operation(operation, operands):
    """Compute the specified mathematical operation between a list of numbers"""
    print("compute_math_operation function called")
    
    if operation.lower() == 'evaluate':
        # Join operands into a single expression string
        expression = ''.join(operands)

        # Check and replace any factorial operations in the expression
        if '!' in expression:
            expression = re.sub(r'(\d+)!', lambda match: str(factorial(int(match.group(1)))), expression)

        try:
            # Safely evaluate the expression
            result = eval(expression)
            return json.dumps({"expression": expression, "result": result})
        except Exception as e:
            return json.dumps({"error": str(e)})
    else:
        return json.dumps({"error": "Unsupported operation"})

def run_conversation():
    x = input("Enter an operation to calculate: ")
    
    # Step 1: send the conversation and available functions to the model
    messages = [{"role": "user", "content": x}]
    
    tools = [
        {
            "type": "function",
            "function": {
                "name": "compute_math_operation",
                "description": "Compute any mathematical expression, including operations like addition, subtraction, multiplication, division, and factorial (e.g., 10!).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "operation": {
                            "type": "string",
                            "description": "Specify 'evaluate' for evaluating a mathematical expression.",
                        },
                        "operands": {
                            "type": "array",
                            "description": "A list of numbers and operators forming the mathematical expression.",
                            "items": {
                                "type": "string"
                            }
                        }
                    },
                    "required": ["operation", "operands"],
                },
            },
        }
    ]
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        tools=tools,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    
    response_message = response.choices[0].message
    
    tool_calls = response_message.tool_calls
    if not tool_calls:
        return "Operation not supported."
    
    # Step 2: check if the model wanted to call a function
    if tool_calls:
        # Step 3: call the function
        available_functions = {
            "compute_math_operation": compute_math_operation,
        }
        messages.append(response_message)  # extend conversation with assistant's reply
        # Step 4: send the info for each function call and function response to the model
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                operation=function_args.get("operation"),
                operands=function_args.get("operands", [])
            )
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )  # extend conversation with function response
        second_response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
        )  # get a new response from the model where it can see the function response
        
        # Extract and print the result
        reply_content = second_response.choices[0].message.content
        return reply_content
assistant = {
  "model": {
    "provider": "openai",
    "model": "gpt-4",
    "messages": [
      {
          "role": "system",
          "content": "You are a math operation solver. The user will provide you with a mathematical operation. You will utilize the Python function compute_math_operation and relay the result of that function. DO NOT COMPUTE ANY MATHEMATICAL OPERATIONS YOURSELF."
      }
    ]
  }
}
vapi.start(assistant=assistant)
vapi.say(run_conversation())












