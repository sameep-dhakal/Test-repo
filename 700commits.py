import os
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
    new_line = f"Commit {i+1}: New line of text\n"
    new_content = content + new_line

    # Write the new content to the file
    with open(file_path, "w") as file:
        file.write(new_content)

    # Stage and commit the changes using Git
    subprocess.run(["git", "add", file_path])
    subprocess.run(["git", "commit", "-m", f"Commit {i+1}: Add new line"])

    time.sleep(5)

print("Commits created successfully.")
# Commit 21: New line of text
# Commit 22: New line of text
# Commit 23: New line of text
# Commit 24: New line of text
# Commit 25: New line of text
# Commit 26: New line of text
# Commit 27: New line of text
# Commit 28: New line of text
# Commit 29: New line of text
# Commit 30: New line of text
# Commit 31: New line of text
# Commit 32: New line of text
# Commit 33: New line of text
# Commit 34: New line of text
# Commit 35: New line of text
# Commit 36: New line of text
# Commit 37: New line of text
# Commit 38: New line of text
# Commit 39: New line of text
# Commit 40: New line of text
# Commit 41: New line of text
# Commit 42: New line of text
# Commit 43: New line of text
# Commit 44: New line of text
# Commit 45: New line of text
# Commit 46: New line of text
# Commit 47: New line of text