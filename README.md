# Log Viewer Web App

This project is a simple web application built with Flask that allows you to view `.log` files from a specific directory. The app displays one `.log` file at a time and provides navigation arrows to move between files.

## Features

- Displays contents of `.log` files from a specified directory
- Provides Previous/Next navigation to move between files
- Easy deployment with Docker

## Prerequisites

- **Python**: 3.9
- **Flask**: Install with `pip install flask`
- **Docker** (optional, if you prefer to run using Docker)

## Project Structure

```
your_project/
├── app.py              # Main application code
├── Dockerfile          # Dockerfile for containerizing the app
├── docker-compose.yml  # Docker Compose configuration
├── templates/
│   └── index.html      # HTML template for displaying log content
└── logs/               # Directory containing .log files
    ├── example1.log
    ├── example2.log
    └── ...
```

## Getting Started

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/log-viewer-web-app.git
cd log-viewer-web-app
```

### Step 2: Set Up `.log` Files

Place your `.log` files in the `logs` directory. Each `.log` file will be accessible through the web interface.

### Step 3: Run the App

#### Option 1: Run Locally with Python

1. Install Flask:

    ```bash
    pip install flask
    ```

2. Start the Flask server:

    ```bash
    python app.py
    ```

3. Open your browser and go to `http://127.0.0.1:5000` to view the app.

#### Option 2: Run with Docker

1. Build the Docker image:

    ```bash
    docker-compose build
    ```

2. Run the Docker container:

    ```bash
    docker-compose up
    ```

3. Open your browser and go to `http://localhost:5000` to access the app.

4. To stop the Docker container, use:

    ```bash
    docker-compose down
    ```

## Usage

1. Go to the app in your browser (`http://127.0.0.1:5000` or `http://localhost:5000` when using Docker).
2. The app displays the content of the first `.log` file.
3. Use the **Previous** and **Next** buttons to navigate between `.log` files.
4. The current file name and position (e.g., "2 of 5") are displayed above the log content.

## Configuration

- **Log Directory**: By default, the app reads `.log` files from the `logs` directory in the project root.
- **Port**: The app runs on port 5000. You can change this in the `docker-compose.yml` file if needed.

---

This web app is created by ChatGPT