# Gomarble-ai-reviews-fetching-
Overview

This project is a Python-based tool for fetching product reviews from e-commerce websites. The tool scrapes reviews from online platforms and saves them for analysis or further processing.

Features

Scrape product reviews from e-commerce websites.

Save reviews to a local file for further use.

Prerequisites

Ensure you have the following installed and set up:

Python 3.8 or higher

pip (Python package manager)

Required Python libraries (listed in requirements.txt)

Installation

1. Clone the Repository
  git clone https://github.com/Dharshanpatil/Gomarble-ai-reviews-fetching.git
  cd Gomarble-ai-reviews-fetching
2. Install Dependencies

Install the required Python libraries:
pip install -r requirements.txt
Usage

Run the Script

Execute the main script to fetch reviews:

python main.py

Provide Inputs

Enter the product URL to fetch reviews.

The tool will scrape reviews and save them to a file.

Output

Results will be saved in the specified format (e.g., JSON or CSV) in the output/ directory.

Configuration

Modify the following settings in the config.py file (if applicable):

Scraping Settings: Configure scraping parameters (e.g., number of reviews to fetch).

Output Settings: Set file formats for output (JSON/CSV).

Example

Input

Product URL: https://example.com/product/12345

Output
 [
  {
    "review": "Great product, highly recommend!",
    "rating": 5,
    "author": "John Doe",
    "date": "2025-01-01"
  },
  {
    "review": "Not satisfied with the quality.",
    "rating": 2,
    "author": "Jane Smith",
    "date": "2025-01-02"
  }
]

Dependencies

The project uses the following Python libraries:

requests: For HTTP requests during web scraping.

beautifulsoup4: For parsing HTML content.

pandas: For data handling and exporting.

