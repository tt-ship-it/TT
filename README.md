# Simple Web Server Example

This project demonstrates a basic web server implemented in Python using the built-in `http.server` module.

## Project Structure

```
.
├── simple_web_server/
│   ├── index.html       # The main HTML page served
│   └── server.py        # The Python script to run the web server
└── README.md            # This file
```

## How to Run

1.  **Navigate to the `simple_web_server` directory:**
    ```bash
    cd simple_web_server
    ```

2.  **Run the Python server script:**
    ```bash
    python server.py
    ```
    Or, if you're using Python 3:
    ```bash
    python3 server.py
    ```

3.  **Open your web browser:**
    Navigate to `http://localhost:8000/` to see the `index.html` page.

The server will print messages to the console indicating it's running and from where it's serving files. You can stop the server by pressing `Ctrl+C` in the terminal.
