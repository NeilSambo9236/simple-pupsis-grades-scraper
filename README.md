# Simple PUPSIS Grades Scraper

**Technologies:** Python, Playwright, Pandas

## Requirements

* Python 3.14.2
* A valid PUPSIS account
* The dependencies listed in `requirements.txt`

## Background

PUPSIS requires students to log in manually to check their grades. During grade release periods, repeatedly logging in just to check whether a grade has been posted can be inconvenient.

This project automates that process by retrieving grade information directly from the PUPSIS grades section.

## What It Is For

This project is a simple web scraper that:

* Logs into PUPSIS
* Navigates to the grades section
* Extracts grade records from the available tables
* Converts the extracted data into a Pandas DataFrame
* Displays the relevant grade information in the terminal

The displayed information includes:

* Subject Code
* Description
* Faculty Name
* Sect Code
* Final Grade
* Grade Status

## How to Use It

### 1. Install the dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the program

```bash
python main.py
```

### 3. Enter your PUPSIS credentials

Use your own valid PUPSIS account when prompted by the program.

## Notes

* This project is intended for personal use and educational purposes.
* The scraper depends on the current structure of the PUPSIS website. Changes to the website may require updates to the scraper.
* Do not share or commit your PUPSIS credentials to the repository.