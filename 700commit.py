import os
import subprocess
import time

# Replace these with your repository information
repository_path = "/home/sameeps/Desktop/Test-repo"
# Relative to the repository root
file_path = "/home/sameeps/Desktop/Test-repo/700commits.py"

# Change to the repository directory
os.chdir(repository_path)

# Create a Python file with initial content
initial_content = """import os
import subprocess
import time

# Replace these with your repository information
repository_path = "/home/sameeps/Desktop/Test-repo"
# Relative to the repository root
file_path = "/home/sameeps/Desktop/Test-repo/700commits.txt"

# Change to the repository directory
os.chdir(repository_path)

# Loop to create commits
for i in range(45, 699):
    # Read the current content of the file
    with open(file_path, "r") as file:
        content = file.read()

    # Add a new line of text for each commit
    new_line = f"Commit {i+1}: New line of text\\n"
    new_content = content + new_line

    # Write the new content to the file
    with open(file_path, "w") as file:
        file.write(new_content)

    # Stage and commit the changes using Git
    subprocess.run(["git", "add", file_path])
    subprocess.run(["git", "commit", "-m", f"Commit {i+1}: Add new line"])

    time.sleep(5)

print("Commits created successfully.")
"""

with open(file_path, "w") as file:
    file.write(initial_content)

# Initialize a Git repository if not already initialized
if not os.path.exists(os.path.join(repository_path, ".git")):
    subprocess.run(["git", "init"])

# Loop to create commits
for i in range(0, 20):  # Changed the range to create 700 commits
    # Read the current content of the file
    with open(file_path, "r") as file:
        content = file.read()

    # Add a new line of text for each commit
    new_line = f"# Commit {i+1}: New line of text\n"
    new_content = content + new_line

    # Write the new content to the file
    with open(file_path, "w") as file:
        file.write(new_content)

    # Stage and commit the changes using Git
    subprocess.run(["git", "add", file_path])
    subprocess.run(["git", "commit", "-m", f"Commit {i+1}: Add new line"])

    time.sleep(5)

print("Python file with 700 commits created successfully.")
