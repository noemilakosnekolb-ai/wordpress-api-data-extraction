# WordPress Categories Exporter

This Python project fetches categories from a WordPress site via its REST API and exports them to an Excel file. It demonstrates API integration, JSON parsing, data transformation, and Excel export using Pandas.

## Features

- Fetches categories from a WordPress site
- Parses JSON responses
- Creates a structured table with category names and IDs
- Exports the data to Excel using Pandas
- Easy to adapt to other WordPress sites


## Usage

Clone this repository:

git clone https://github.com/noemilakosnekolb-ai/wordpress-api-python.git
cd wordpress-api-python/src


Run the script:

python API_export_to_excel.py


After successful execution, the Excel file categories.xlsx will be created in the output folder.

Project Structure
wordpress-api-python/
├── README.md
├── src/
│   └── API_export_to_excel.py
├── output/
│   └── categories.xlsx (generated)
├── requirements.txt
└── .gitignore

## Notes

Currently configured for http://www.gmkitchen.hu WordPress site

Can be easily adapted to other WordPress sites by changing the url variable

Focuses on clean, reproducible, and well-documented code

## License

This project is licensed under the MIT License. See LICENSE for details.