import pandas as pd
import os


def combine_data_files(file_list, output_filename):
    """
    Reads multiple CSV data files, combines them into a single DataFrame,
    and saves the result to a new CSV file. Skips the first row of each file
    to handle extra title headers.

    Args:
        file_list (list): A list of filenames to combine.
        output_filename (str): The name for the output combined CSV file.
    """
    # A list to hold all the dataframes from each file
    all_dataframes = []

    print("Starting to process files...")

    # Loop through each file in the provided list
    for filename in file_list:
        if os.path.exists(filename):
            try:
                # Read the CSV file, skipping the first row which contains a title.
                # The actual headers are in the second row, which pandas will now use.
                df = pd.read_csv(filename, skiprows=1)

                # Add the dataframe to our list
                all_dataframes.append(df)

                print(
                    f"Successfully read and added '{filename}'. It has {len(df)} rows."
                )
            except Exception as e:
                print(f"Could not read file '{filename}'. Error: {e}")
        else:
            print(f"Warning: File '{filename}' not found. Skipping.")

    # Check if we have any dataframes to combine
    if not all_dataframes:
        print("No dataframes were loaded. Cannot create an output file.")
        return

    # Concatenate all the dataframes in the list into one single dataframe
    print("\nCombining all dataframes...")
    combined_df = pd.concat(all_dataframes, ignore_index=True)

    # Save the combined dataframe to a new CSV file
    try:
        combined_df.to_csv(output_filename, index=False)
        print(
            f"\nSuccessfully combined {len(file_list)} files into '{output_filename}'."
        )
        print(f"The combined file has a total of {len(combined_df)} rows.")
    except Exception as e:
        print(f"Could not save the combined file. Error: {e}")


if __name__ == "__main__":
    # List of the new CSV files you want to combine
    files_to_combine = [
        "Agmarknet_Price_Report_Bajra_2015-2019.csv",
        "Agmarknet_Price_Report_Bajra_2019-2022.xls.csv",
        "Agmarknet_Price_Report_Bajra_2022-2025.xls.csv",
    ]

    # The name of the final, merged CSV file
    output_file = "Combined_Bajra_Prices_2015-2025.csv"

    # Run the function
    combine_data_files(files_to_combine, output_file)
