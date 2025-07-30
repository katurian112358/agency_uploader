import argparse
import pandas as pd


def merge_excels(central_path, other_paths, key=None, output=None):
    """Merge multiple Excel files into a central repository.

    Parameters
    ----------
    central_path : str
        Path to the central Excel file which will be updated.
    other_paths : list[str]
        Paths to other Excel files to merge into the central file.
    key : str, optional
        Column name to use as a unique identifier for merging rows. If
        provided, matching rows will be updated and new rows appended.
        If omitted, rows from all sheets will simply be concatenated.
    output : str, optional
        Path to save the merged file. By default the central file will
        be overwritten with the merged result.
    """

    # Read the central file
    central_df = pd.read_excel(central_path)

    for path in other_paths:
        df = pd.read_excel(path)

        if key:
            # Set the key as index for both dataframes for easier merging
            central_df = central_df.set_index(key)
            df = df.set_index(key)

            # Update existing rows
            central_df.update(df)

            # Append rows that are not already in the central dataframe
            new_rows = df.loc[~df.index.isin(central_df.index)]
            central_df = pd.concat([central_df, new_rows])

            # Reset index back to a column
            central_df = central_df.reset_index()
        else:
            # If no key specified, just concatenate the data
            central_df = pd.concat([central_df, df], ignore_index=True)

    output_path = output or central_path
    central_df.to_excel(output_path, index=False)


def main():
    parser = argparse.ArgumentParser(
        description="Merge Excel sheets into a central repository of information",
    )
    parser.add_argument(
        "central", help="Path to the central Excel file that will be updated"
    )
    parser.add_argument(
        "others",
        nargs="+",
        help="Paths to additional Excel files that will be merged into the central file",
    )
    parser.add_argument(
        "-k",
        "--key",
        help="Optional column name that acts as a unique key for merging rows",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Optional output path for the merged Excel file. Defaults to overwriting the central file",
    )

    args = parser.parse_args()
    merge_excels(args.central, args.others, key=args.key, output=args.output)


if __name__ == "__main__":
    main()
