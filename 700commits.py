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
# Commit 125: New line of text
# Commit 126: New line of text
# Commit 127: New line of text
# Commit 128: New line of text
# Commit 129: New line of text
# Commit 130: New line of text
# Commit 131: New line of text
# Commit 132: New line of text
# Commit 133: New line of text
# Commit 134: New line of text
# Commit 135: New line of text
# Commit 136: New line of text
# Commit 137: New line of text
# Commit 138: New line of text
# Commit 139: New line of text
# Commit 140: New line of text
# Commit 141: New line of text
# Commit 142: New line of text
# Commit 143: New line of text
# Commit 144: New line of text
# Commit 145: New line of text
# Commit 146: New line of text
# Commit 147: New line of text
# Commit 148: New line of text
# Commit 149: New line of text
# Commit 150: New line of text
# Commit 151: New line of text
# Commit 152: New line of text
# Commit 153: New line of text
# Commit 154: New line of text
# Commit 155: New line of text
# Commit 156: New line of text
# Commit 157: New line of text
# Commit 158: New line of text
# Commit 159: New line of text
# Commit 160: New line of text
# Commit 161: New line of text
# Commit 162: New line of text
# Commit 163: New line of text
# Commit 164: New line of text
# Commit 165: New line of text
# Commit 166: New line of text
# Commit 167: New line of text
# Commit 168: New line of text
# Commit 169: New line of text
# Commit 170: New line of text
# Commit 171: New line of text
# Commit 172: New line of text
# Commit 173: New line of text
# Commit 174: New line of text
# Commit 175: New line of text
# Commit 176: New line of text
# Commit 177: New line of text
# Commit 178: New line of text
# Commit 179: New line of text
# Commit 180: New line of text
# Commit 181: New line of text
# Commit 182: New line of text
# Commit 183: New line of text
# Commit 184: New line of text
# Commit 185: New line of text
# Commit 186: New line of text
# Commit 187: New line of text
# Commit 188: New line of text
# Commit 189: New line of text
# Commit 190: New line of text
# Commit 191: New line of text
# Commit 192: New line of text
# Commit 193: New line of text
# Commit 194: New line of text
# Commit 195: New line of text
# Commit 196: New line of text
# Commit 197: New line of text
# Commit 198: New line of text
# Commit 199: New line of text
# Commit 200: New line of text
# Commit 201: New line of text
# Commit 202: New line of text
# Commit 203: New line of text
# Commit 204: New line of text
# Commit 205: New line of text
# Commit 206: New line of text
# Commit 207: New line of text
# Commit 208: New line of text
# Commit 209: New line of text
# Commit 210: New line of text
# Commit 211: New line of text
# Commit 212: New line of text
# Commit 213: New line of text
# Commit 214: New line of text
# Commit 215: New line of text
# Commit 216: New line of text
# Commit 217: New line of text
# Commit 218: New line of text
# Commit 219: New line of text
# Commit 220: New line of text
# Commit 221: New line of text
# Commit 222: New line of text
# Commit 223: New line of text
# Commit 224: New line of text
# Commit 225: New line of text
# Commit 226: New line of text
# Commit 227: New line of text
# Commit 228: New line of text
# Commit 229: New line of text
# Commit 230: New line of text
# Commit 231: New line of text
# Commit 232: New line of text
# Commit 233: New line of text
# Commit 234: New line of text
# Commit 235: New line of text
# Commit 236: New line of text
# Commit 237: New line of text
# Commit 238: New line of text
# Commit 239: New line of text
# Commit 240: New line of text
# Commit 241: New line of text
# Commit 242: New line of text
# Commit 243: New line of text
# Commit 244: New line of text
