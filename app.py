from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Directory containing .log files
LOG_DIR = "logs"

# Helper function to get sorted list of log files
def get_log_files():
    return sorted([f for f in os.listdir(LOG_DIR) if f.endswith(".log")])

@app.route("/")
def index():
    # Get the list of log files
    log_files = get_log_files()

    # Get current index from query parameter, default to 0
    current_index = int(request.args.get("index", 0))

    # Ensure index is within bounds
    if current_index < 0:
        current_index = 0
    elif current_index >= len(log_files):
        current_index = len(log_files) - 1

    # Get the current log file name and content
    current_file = log_files[current_index]
    with open(os.path.join(LOG_DIR, current_file), "r") as file:
        content = file.read()

    # Calculate navigation indices
    prev_index = max(0, current_index - 1)
    next_index = min(len(log_files) - 1, current_index + 1)

    return render_template(
        "index.html",
        content=content,
        current_file=current_file,
        current_index=current_index,
        prev_index=prev_index,
        next_index=next_index,
        total_files=len(log_files),
    )

if __name__ == "__main__":
    app.run(debug=True)
