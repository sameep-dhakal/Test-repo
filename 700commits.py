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
# Commit 48: New line of text
# Commit 49: New line of text
# Commit 50: New line of text
# Commit 51: New line of text
# Commit 52: New line of text
# Commit 53: New line of text
# Commit 54: New line of text
# Commit 55: New line of text
# Commit 56: New line of text
# Commit 57: New line of text
# Commit 58: New line of text
# Commit 59: New line of text
# Commit 60: New line of text
# Commit 61: New line of text
# Commit 62: New line of text
# Commit 63: New line of text
# Commit 64: New line of text
# Commit 65: New line of text
# Commit 66: New line of text
# Commit 67: New line of text
# Commit 68: New line of text
# Commit 69: New line of text
# Commit 70: New line of text
# Commit 71: New line of text
# Commit 72: New line of text
# Commit 73: New line of text
# Commit 74: New line of text
# Commit 75: New line of text
# Commit 76: New line of text
# Commit 77: New line of text
# Commit 78: New line of text
# Commit 79: New line of text
# Commit 80: New line of text
# Commit 81: New line of text
# Commit 82: New line of text
# Commit 83: New line of text
# Commit 84: New line of text
# Commit 85: New line of text
# Commit 86: New line of text
# Commit 87: New line of text
# Commit 88: New line of text
# Commit 89: New line of text
# Commit 90: New line of text
# Commit 91: New line of text
# Commit 92: New line of text
# Commit 93: New line of text
# Commit 94: New line of text
# Commit 95: New line of text
# Commit 96: New line of text
# Commit 97: New line of text
# Commit 98: New line of text
# Commit 99: New line of text
# Commit 100: New line of text
# Commit 101: New line of text
# Commit 102: New line of text
# Commit 103: New line of text
# Commit 104: New line of text
# Commit 105: New line of text
# Commit 106: New line of text
# Commit 107: New line of text
# Commit 108: New line of text
# Commit 109: New line of text
# Commit 110: New line of text
# Commit 111: New line of text
# Commit 112: New line of text
# Commit 113: New line of text
# Commit 114: New line of text
# Commit 115: New line of text
# Commit 116: New line of text
# Commit 117: New line of text
# Commit 118: New line of text
# Commit 119: New line of text
# Commit 120: New line of text
# Commit 121: New line of text
# Commit 122: New line of text
# Commit 123: New line of text
# Commit 124: New line of text
