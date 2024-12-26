# FP-Growth Algorithm with Python and Tkinter

The **FP-Growth Algorithm with Python and Tkinter** is a graphical user interface (GUI) application that simplifies the process of discovering frequent patterns in transactional datasets. Built using the `pyfpgrowth` library, it leverages the FP-Growth algorithm—an efficient and scalable approach to frequent pattern mining that avoids generating candidate sets. The application provides a user-friendly interface powered by `tkinter`, allowing users to input transactions, specify a minimum support threshold, and instantly view the results in a clear, organized format. This tool is ideal for those who need a simple yet powerful way to analyze transactional data without delving into complex coding or command-line operations. 

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
