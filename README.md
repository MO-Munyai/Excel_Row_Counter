# excel file row conter - scan.py

This script counts the number of rows in an Excel file that contain at least one non-empty value.

## How It Works

- Loads an Excel file using pandas.
- Drops rows where all values are empty.
- Prints the count of remaining rows.

## Usage

1. Place your Excel file in the same directory as the script.
2. Rename your Excel file to `file_name.xlsx` or update the script with your file's name.
3. Run the script:

    ```sh
    python scan.py
    ```

4. The number of non-empty rows will be printed to the console.

## Requirements

- Python 3.x
- pandas
- openpyxl (for .xlsx files)

Install dependencies:

```sh
pip install pandas openpyxl
```

## Notes

- Only rows with at least one non-empty cell are counted.
- The script expects an `.xlsx` file by default.
