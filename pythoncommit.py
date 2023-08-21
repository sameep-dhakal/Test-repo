import os
import subprocess

# Replace these with your repository information
repository_path = "/home/sameeps/Desktop/Object-Oriented-Programming"
# Relative to the repository root
file_path = "/home/sameeps/Desktop/Object-Oriented-Programming/1000commits.txt"

# Change to the repository directory
os.chdir(repository_path)

# Read the original content of the file
with open(file_path, "r") as file:
    original_content = file.read()

# Loop to create commits
for i in range(1000):
    # Modify the content of the file for each commit
    new_content = f"Commit {i+1}"

    # Write the new content to the file
    with open(file_path, "w") as file:
        file.write(new_content)

    # Stage and commit the changes using Git
    subprocess.run(["git", "add", file_path])
    subprocess.run(["git", "commit", "-m", f"Commit {i+1}"])

print("Commits created successfully.")
