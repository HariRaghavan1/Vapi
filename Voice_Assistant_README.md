
# Voice Assistant with Vapi Web SDK and Python Backend

This project implements a **voice assistant** that uses the **Vapi Web SDK** for natural language processing and a **Flask backend** (Python) to compute mathematical operations. The assistant can interact via voice commands, process mathematical expressions, and return results.

## Features
- **Voice Interaction**: Powered by Vapi Web SDK and 11Labs voice services.
- **Math Computation**: Accepts and evaluates mathematical expressions via a Python backend.
- **Frontend**: Built with **Vite** to provide a fast development experience and optimized production build.
- **Backend**: Simple Flask server that handles requests from the assistant and returns the result of mathematical operations.

## Table of Contents
1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [API Endpoints](#api-endpoints)
6. [Links](#links)
7. [Contributing](#contributing)
8. [License](#license)

## Installation

### Prerequisites
- **Node.js** and **npm** (for Vite)
- **Python 3** (for Flask backend)
- **Vapi Web SDK** account ([Vapi.ai](https://vapi.ai/))
- **11Labs API key** for voice services ([11labs](https://11labs.io/))

### Clone the Repository
```bash
git clone https://github.com/yourusername/voice-assistant-vapi.git
cd voice-assistant-vapi
```

### Frontend Setup (Vite)

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Run Vite development server**:
   ```bash
   npm run dev
   ```

3. **Build for production** (optional):
   ```bash
   npm run build
   ```

### Backend Setup (Python Flask)

1. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install flask
   ```

3. **Run the Flask server**:
   ```bash
   python server.py
   ```

## Configuration

### Vapi Web SDK Configuration

1. **Set up your Vapi Web SDK**:
   In `main.js`, replace `'YOUR_API_KEY'` with your actual Vapi API key:
   ```js
   const vapi = new Vapi('YOUR_API_KEY');
   ```

2. **Set up 11Labs voice**:
   In `main.js`, replace `'burt'` with your preferred 11Labs voice and ensure you have an API key set up in the 11Labs service.

### Flask Server Configuration
No specific configurations are needed for the Flask server in this simple setup. You can adjust the port in `server.py` if necessary:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

## Usage

1. Start the Vite development server:
   ```bash
   npm run dev
   ```

2. Start the Flask backend:
   ```bash
   python server.py
   ```

3. Open your browser and navigate to `http://localhost:3000`. Click the **"Start Assistant"** button to interact with the voice assistant. When you ask a mathematical question, the assistant will evaluate it using the backend server.

## Project Structure

```plaintext
vite-project/
│
├── public/                     # Public assets (optional)
├── src/
│   ├── index.html              # Main HTML file
│   ├── style.css               # Styling for the web page
│   ├── main.js                 # Main JavaScript file, Vapi Web SDK initialized here
│   ├── counter.js              # Example counter (not directly used for the assistant)
│
├── server.py                   # Flask backend server to handle math operation requests
├── function1.py                # Python voice agent (optional, used for local Python execution)
│
├── node_modules/               # Auto-generated folder for npm packages
├── package.json                # Project metadata for Vite/NPM
├── package-lock.json           # Auto-generated dependencies lock file
├── README.md                   # This file
```

### Relevant Files
- **index.html**: Defines the structure of the app.
- **style.css**: Provides styles for the page.
- **main.js**: Initializes the Vapi Web SDK and handles communication between the assistant and backend.
- **server.py**: A Flask server that computes the results of mathematical expressions.
- **function1.py**: A Python script (for local use) that might run the assistant outside of the web version.

## API Endpoints

- **POST** `/process`: This endpoint receives the `operation` and `operands` from the front-end, evaluates the mathematical expression, and returns the result.
  - **Request Body**:
    ```json
    {
      "operation": "evaluate",
      "operands": ["2", "+", "2"]
    }
    ```
  - **Response**:
    ```json
    {
      "result": 4
    }
    ```

## Links

- **Vapi Web SDK Documentation**: [Vapi Web SDK Docs](https://vapi.ai/docs/web)
- **Vapi Python SDK Documentation**: [Vapi Python SDK Docs](https://vapi.ai/docs/python)
- **Vite Documentation**: [Vite Docs](https://vitejs.dev/guide/)
- **Flask Documentation**: [Flask Docs](https://flask.palletsprojects.com/en/2.0.x/)

## Contributing
Feel free to submit issues or pull requests to improve this project. Contributions are always welcome!
