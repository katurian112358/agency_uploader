# Agency Uploader

A Python tool to:

- Read Excel files with enrollment data
- Map and transform the data
- Upload to AgencySmart API

## Excel Merging Utility

The `merge_excel.py` script can merge multiple Excel spreadsheets into a
single master workbook. Use it when you have a central repository file
and you want to pull in data from additional sheets.

### Usage

```bash
python merge_excel.py CENTRAL.xlsx OTHER1.xlsx OTHER2.xlsx -k ID_COLUMN -o OUTPUT.xlsx
```

- `CENTRAL.xlsx` is the main file that will be updated.
- `OTHER*.xlsx` are additional files to merge.
- `-k` optionally specifies a column that acts as a unique key for merging
  rows. When provided, matching rows are updated and new rows are appended.
- `-o` specifies the output path for the merged file. If omitted, the central
  file is overwritten.

🚀 First commit: repo now live!
