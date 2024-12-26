# FP-growth-Algorithm
Here's a concise README file for your FP-Growth algorithm project:

---

# FP-Growth Algorithm with Python and Tkinter

**FP-Growth** is a Python-based GUI application designed to find frequent patterns in transactional data. It is built using the `pyfpgrowth` library for pattern mining and `tkinter` for a user-friendly graphical interface.

## Features

- Input transactional data in a text field (comma-separated items per transaction).
- Set a custom minimum support threshold.
- Identify frequent item patterns using the FP-Growth algorithm.
- Results are displayed in a scrollable output window.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://Trickybutshruti/FP-growth-Algorithm
   cd FP-growth-Algorithm
   ```

2. **Install dependencies:**

   Ensure you have Python installed. Then, install the required libraries:

   ```bash
   pip install pyfpgrowth
   ```

3. **Run the application:**

   ```bash
   python fp_growth_tkinter.py
   ```

## Usage

1. Open the application.
2. Input transactions in the text area. Each line should represent a transaction, with items separated by commas (e.g., `milk,bread,eggs`).
3. Enter a minimum support value (e.g., `0.5` for 50%).
4. Click the **Run FP-Growth** button to find frequent patterns.
5. View the results in the output window.

## Requirements

- Python 3.x
- Libraries: `tkinter` (built-in), `pyfpgrowth`

## Project Structure

- **fp_growth_tkinter.py**: The main script containing the application code.
