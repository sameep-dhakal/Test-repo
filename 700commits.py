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
# Commit 245: New line of text
# Commit 246: New line of text
# Commit 247: New line of text
# Commit 248: New line of text
# Commit 249: New line of text
# Commit 250: New line of text
# Commit 251: New line of text
# Commit 252: New line of text
# Commit 253: New line of text
# Commit 254: New line of text
# Commit 255: New line of text
# Commit 256: New line of text
# Commit 257: New line of text
# Commit 258: New line of text
# Commit 259: New line of text
# Commit 260: New line of text
# Commit 261: New line of text
# Commit 262: New line of text
# Commit 263: New line of text
# Commit 264: New line of text
# Commit 265: New line of text
# Commit 266: New line of text
# Commit 267: New line of text
# Commit 268: New line of text
# Commit 269: New line of text
# Commit 270: New line of text
# Commit 271: New line of text
# Commit 272: New line of text
# Commit 273: New line of text
# Commit 274: New line of text
# Commit 275: New line of text
# Commit 276: New line of text
# Commit 277: New line of text
# Commit 278: New line of text
# Commit 279: New line of text
# Commit 280: New line of text
# Commit 281: New line of text
# Commit 282: New line of text
# Commit 283: New line of text
# Commit 284: New line of text
# Commit 285: New line of text
# Commit 286: New line of text
# Commit 287: New line of text
# Commit 288: New line of text
# Commit 289: New line of text
# Commit 290: New line of text
# Commit 291: New line of text
# Commit 292: New line of text
# Commit 293: New line of text
# Commit 294: New line of text
# Commit 295: New line of text
# Commit 296: New line of text
# Commit 297: New line of text
# Commit 298: New line of text
# Commit 299: New line of text
# Commit 300: New line of text
# Commit 302: New line of text
# Commit 303: New line of text
# Commit 304: New line of text
# Commit 305: New line of text
# Commit 306: New line of text
# Commit 307: New line of text
# Commit 308: New line of text
# Commit 309: New line of text
# Commit 310: New line of text
# Commit 311: New line of text
# Commit 312: New line of text
# Commit 313: New line of text
# Commit 314: New line of text
# Commit 315: New line of text
# Commit 316: New line of text
# Commit 317: New line of text
# Commit 318: New line of text
# Commit 319: New line of text
# Commit 320: New line of text
# Commit 321: New line of text
# Commit 322: New line of text
# Commit 323: New line of text
# Commit 324: New line of text
# Commit 325: New line of text
# Commit 326: New line of text
# Commit 327: New line of text
# Commit 328: New line of text
# Commit 329: New line of text
# Commit 330: New line of text
# Commit 331: New line of text
# Commit 332: New line of text
# Commit 333: New line of text
# Commit 334: New line of text
# Commit 335: New line of text
# Commit 336: New line of text
# Commit 337: New line of text
# Commit 338: New line of text
# Commit 339: New line of text
# Commit 340: New line of text
# Commit 341: New line of text
# Commit 342: New line of text
# Commit 343: New line of text
# Commit 344: New line of text
# Commit 345: New line of text
# Commit 346: New line of text
# Commit 347: New line of text
# Commit 348: New line of text
# Commit 349: New line of text
# Commit 350: New line of text
# Commit 351: New line of text
# Commit 352: New line of text
# Commit 353: New line of text
# Commit 354: New line of text
# Commit 355: New line of text
# Commit 356: New line of text
# Commit 357: New line of text
# Commit 358: New line of text
# Commit 359: New line of text
# Commit 360: New line of text
# Commit 361: New line of text
# Commit 362: New line of text
# Commit 363: New line of text
# Commit 364: New line of text
# Commit 365: New line of text
# Commit 366: New line of text
# Commit 367: New line of text
# Commit 368: New line of text
# Commit 369: New line of text
# Commit 370: New line of text
# Commit 371: New line of text
# Commit 372: New line of text
# Commit 373: New line of text
# Commit 374: New line of text
# Commit 375: New line of text
# Commit 376: New line of text
# Commit 377: New line of text
# Commit 378: New line of text
# Commit 379: New line of text
# Commit 380: New line of text
# Commit 381: New line of text
# Commit 382: New line of text
# Commit 383: New line of text
# Commit 384: New line of text
# Commit 385: New line of text
# Commit 386: New line of text
# Commit 387: New line of text
# Commit 388: New line of text
# Commit 389: New line of text
# Commit 390: New line of text
# Commit 391: New line of text
# Commit 392: New line of text
# Commit 393: New line of text
# Commit 394: New line of text
# Commit 395: New line of text
# Commit 396: New line of text
# Commit 397: New line of text
# Commit 398: New line of text
# Commit 399: New line of text
# Commit 400: New line of text
# Commit 401: New line of text
# Commit 402: New line of text
# Commit 403: New line of text
# Commit 404: New line of text
# Commit 405: New line of text
# Commit 406: New line of text
# Commit 407: New line of text
# Commit 408: New line of text
# Commit 409: New line of text
# Commit 410: New line of text
# Commit 411: New line of text
# Commit 412: New line of text
# Commit 413: New line of text
# Commit 414: New line of text
# Commit 415: New line of text
# Commit 416: New line of text
# Commit 417: New line of text
# Commit 418: New line of text
# Commit 419: New line of text
# Commit 420: New line of text
# Commit 421: New line of text
# Commit 422: New line of text
# Commit 423: New line of text
# Commit 424: New line of text
# Commit 425: New line of text
# Commit 426: New line of text
# Commit 427: New line of text
# Commit 428: New line of text
# Commit 429: New line of text
# Commit 430: New line of text
# Commit 431: New line of text
# Commit 432: New line of text
# Commit 433: New line of text
# Commit 434: New line of text
# Commit 435: New line of text
# Commit 436: New line of text
# Commit 437: New line of text
# Commit 438: New line of text
# Commit 439: New line of text
# Commit 440: New line of text
# Commit 441: New line of text
# Commit 442: New line of text
# Commit 443: New line of text
# Commit 444: New line of text
# Commit 445: New line of text
# Commit 446: New line of text
# Commit 447: New line of text
# Commit 448: New line of text
# Commit 449: New line of text
# Commit 450: New line of text
# Commit 451: New line of text
# Commit 452: New line of text
# Commit 453: New line of text
# Commit 454: New line of text
# Commit 455: New line of text
# Commit 456: New line of text
# Commit 457: New line of text
# Commit 458: New line of text
# Commit 459: New line of text
# Commit 460: New line of text
# Commit 461: New line of text
# Commit 462: New line of text
# Commit 463: New line of text
# Commit 464: New line of text
# Commit 465: New line of text
# Commit 466: New line of text
# Commit 467: New line of text
# Commit 468: New line of text
# Commit 469: New line of text
# Commit 470: New line of text
# Commit 471: New line of text
# Commit 472: New line of text
# Commit 473: New line of text
# Commit 474: New line of text
# Commit 475: New line of text
# Commit 476: New line of text
# Commit 477: New line of text
# Commit 478: New line of text
# Commit 479: New line of text
# Commit 480: New line of text
# Commit 481: New line of text
# Commit 482: New line of text
# Commit 483: New line of text
# Commit 484: New line of text
# Commit 485: New line of text
# Commit 486: New line of text
# Commit 487: New line of text
# Commit 488: New line of text
# Commit 489: New line of text
# Commit 490: New line of text
# Commit 491: New line of text
# Commit 492: New line of text
# Commit 493: New line of text
# Commit 494: New line of text
# Commit 495: New line of text
# Commit 496: New line of text
# Commit 497: New line of text
# Commit 498: New line of text
# Commit 499: New line of text
# Commit 500: New line of text
# Commit 501: New line of text
# Commit 502: New line of text
# Commit 503: New line of text
# Commit 504: New line of text
# Commit 505: New line of text
# Commit 506: New line of text
# Commit 507: New line of text
# Commit 508: New line of text
# Commit 509: New line of text
# Commit 510: New line of text
# Commit 511: New line of text
# Commit 512: New line of text
# Commit 513: New line of text
# Commit 514: New line of text
# Commit 515: New line of text
# Commit 516: New line of text
# Commit 517: New line of text
# Commit 518: New line of text
# Commit 519: New line of text
# Commit 520: New line of text
# Commit 521: New line of text
# Commit 522: New line of text
# Commit 523: New line of text
# Commit 524: New line of text
# Commit 525: New line of text
# Commit 526: New line of text
# Commit 527: New line of text
# Commit 528: New line of text
# Commit 529: New line of text
# Commit 530: New line of text
# Commit 531: New line of text
# Commit 532: New line of text
# Commit 533: New line of text
# Commit 534: New line of text
# Commit 535: New line of text
# Commit 536: New line of text
# Commit 537: New line of text
# Commit 538: New line of text
# Commit 539: New line of text
# Commit 540: New line of text
# Commit 541: New line of text
# Commit 542: New line of text
# Commit 543: New line of text
# Commit 544: New line of text
# Commit 545: New line of text
# Commit 546: New line of text
# Commit 547: New line of text
# Commit 548: New line of text
# Commit 549: New line of text
# Commit 550: New line of text
# Commit 551: New line of text
# Commit 552: New line of text
# Commit 553: New line of text
# Commit 554: New line of text
# Commit 555: New line of text
# Commit 556: New line of text
# Commit 557: New line of text
# Commit 558: New line of text
# Commit 559: New line of text
# Commit 560: New line of text
# Commit 561: New line of text
# Commit 562: New line of text
# Commit 563: New line of text
# Commit 564: New line of text
# Commit 565: New line of text
# Commit 566: New line of text
# Commit 567: New line of text
# Commit 568: New line of text
# Commit 569: New line of text
# Commit 570: New line of text
# Commit 571: New line of text
# Commit 572: New line of text
# Commit 573: New line of text
# Commit 574: New line of text
# Commit 575: New line of text
# Commit 576: New line of text
# Commit 577: New line of text
# Commit 578: New line of text
# Commit 579: New line of text
# Commit 580: New line of text
# Commit 581: New line of text
# Commit 582: New line of text
# Commit 583: New line of text
# Commit 584: New line of text
# Commit 585: New line of text
# Commit 586: New line of text
# Commit 587: New line of text
# Commit 588: New line of text
# Commit 589: New line of text
# Commit 590: New line of text
# Commit 591: New line of text
# Commit 592: New line of text
# Commit 593: New line of text
# Commit 594: New line of text
# Commit 595: New line of text
# Commit 596: New line of text
# Commit 597: New line of text
# Commit 598: New line of text
# Commit 599: New line of text
# Commit 600: New line of text
# Commit 601: New line of text
# Commit 602: New line of text
# Commit 603: New line of text
# Commit 604: New line of text
# Commit 605: New line of text
# Commit 606: New line of text
# Commit 607: New line of text
# Commit 608: New line of text
# Commit 609: New line of text
# Commit 610: New line of text
# Commit 611: New line of text
# Commit 612: New line of text
# Commit 613: New line of text
# Commit 614: New line of text
# Commit 615: New line of text
# Commit 616: New line of text
# Commit 617: New line of text
# Commit 618: New line of text
# Commit 619: New line of text
# Commit 620: New line of text
# Commit 621: New line of text
# Commit 622: New line of text
# Commit 623: New line of text
# Commit 624: New line of text
# Commit 625: New line of text
# Commit 626: New line of text
# Commit 627: New line of text
# Commit 628: New line of text
# Commit 629: New line of text
# Commit 630: New line of text
# Commit 631: New line of text
# Commit 632: New line of text
# Commit 633: New line of text
# Commit 634: New line of text
# Commit 635: New line of text
# Commit 636: New line of text
# Commit 637: New line of text
# Commit 638: New line of text
