# BookBot

**BookBot** is a simple Python CLI tool that analyses the text of a book or text file. It counts total words and the frequency of each letter, and then prints a formatted summary.

---

## Features

- Counts total words in a text file  
- Calculates and sorts letter frequencies 
- Prints a clean, readable summary to the terminal

---

## Example Output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 74893 total words
--------- Character Count -------
a: 4567
b: 1234
...
============= END ===============
```

---

## How to Use

### 1. Clone the repository

```bash
git clone https://github.com/philip-hargreaves/bookbot
cd bookbot
```

### 2. Run the program

```bash
python3 main.py books/frankenstein.txt
```

> Replace `books/frankenstein.txt` with the path to any `.txt` file.

---

## Project Structure

```
bookbot/
├── main.py                 # Entry point
├── stats.py                # Functions for counting/sorting
├── books/                  # Folder for book files (optional)
├── .gitignore
└── README.md
```

---

## Requirements

- Python 3.10 or newer (tested with Python 3.12)
- No external libraries or dependencies

---

## .gitignore

The project includes a `.gitignore` to exclude Python bytecode and cache files:

```gitignore
__pycache__/
*.pyc
```

---

## License

MIT License 
