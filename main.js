// main.js

import './style.css';
import javascriptLogo from './javascript.svg';
import viteLogo from '/vite.svg';
import { setupCounter } from './counter.js';
import Vapi from '@vapi-ai/web';

document.querySelector('#app').innerHTML = `
  <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="${viteLogo}" class="logo" alt="Vite logo" />
    </a>
    <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
      <img src="${javascriptLogo}" class="logo vanilla" alt="JavaScript logo" />
    </a>
    <h1>Math Assistant</h1>
    <div class="card">
      <button id="counter" type="button">Start Assistant</button>
    </div>
    <p class="read-the-docs">
      Click on the button to interact with the math assistant.
    </p>
  </div>
`;

setupCounter(document.querySelector('#counter'));

// Initialize Vapi
const vapi = new Vapi('Your API key');
vapi.start({
  model: {
    provider: "openai",
    model: "gpt-3.5-turbo-0613", // Ensure function calling support
    messages: [
      {
        role: "system",
        content: "You are a helpful math assistant. When the user asks a mathematical question, use the compute_math_operation function to compute the result. Do not compute the result yourself.",
      },
    ],
    functions: [
      {
        name: "compute_math_operation",
        description: "Compute any mathematical expression, including operations like addition, subtraction, multiplication, division, and factorial (e.g., 10!).",
        parameters: {
          type: "object",
          properties: {
            operation: {
              type: "string",
              description: "Specify 'evaluate' for evaluating a mathematical expression.",
            },
            operands: {
              type: "array",
              description: "A list of numbers and operators forming the mathematical expression.",
              items: {
                type: "string",
              },
            },
          },
          required: ["operation", "operands"],
        },
      },
    ],
  },
  voice: {
    provider: "11labs",
    voiceId: "burt",
  },
});

// Event listeners for Vapi
vapi.on('message', async (message) => {
  console.log('Received message:', message);

  // Check if the assistant wants to call a function
  if (message.function_call && message.function_call.name === 'compute_math_operation') {
    console.log('Assistant requested function call:', message.function_call);

    const functionArgs = JSON.parse(message.function_call.arguments);
    const operation = functionArgs.operation;
    const operands = functionArgs.operands;

    console.log('Function arguments:', functionArgs);

    // Fetch the result from compute_math_operation
    console.log('Sending request to backend with operation:', operation, 'and operands:', operands);
    fetch('http://localhost:5000/process', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ operation: operation, operands: operands }),
    })
      .then((response) => response.json())
      .then(async (data) => {
        console.log('Backend response:', data);

        // Send the computation result back to the assistant
        console.log('Sending function result back to assistant:', data);
        const finalResponse = await vapi.send({
          type: 'add-message',
          message: {
            role: 'function',
            name: 'compute_math_operation',
            content: JSON.stringify(data),
          },
        });

        console.log('Assistant final response:', finalResponse);
      })
      .catch((error) => {
        console.error('Error sending to backend:', error);
      });
  } else if (message.role === 'assistant') {
    // Handle the assistant's reply
    console.log('Assistant says:', message.content);
    // Optionally, have the assistant speak the content
    vapi.say(message.content);
  }
});

vapi.on('error', (e) => {
  console.error('Error occurred:', e);
});

console.log('Vapi assistant started.');

