from flask import Flask, render_template, request
import os
import re

app = Flask(__name__)

# Directory containing .log files
LOG_DIR = "logs"

# Helper function to get sorted list of log files
def get_log_files():
    return sorted([f for f in os.listdir(LOG_DIR) if f.endswith(".log")])

# Helper function to search for log files based on a number in the filename
def search_log_files_by_number(log_files, number):
    # Iterate over the log files with their index and filename
    for index, filename in enumerate(log_files):
        if re.search(str(number), filename):
            return index  # Return the index of the first matching file
    return -1  # Return -1 if no matching file is found

@app.route("/")
def index():
    # Get the list of log files
    log_files = get_log_files()

    # Get the search number from query parameter
    search_number = request.args.get("search", type=int)

    # Get current index from query parameter, default to 0
    current_index = int(request.args.get("index", 0))

    # Filter log files based on the search number
    if search_number is not None:
        searched_index = search_log_files_by_number(log_files, search_number)
    else:
        searched_index = -1

    # Ensure index is within bounds and set current_index appropriately
    if searched_index >= 0:
        current_index = searched_index

    # Clear the search number when viewing the file list (not searching)
    search_number = None

    # Get the current file to display
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
        search=search_number  # Pass `None` here if it's reset
    )


if __name__ == "__main__":
    app.run(debug=True)
