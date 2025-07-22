import pandas as pd
import io
import os

# Step 1: Load the uploaded Excel files into pandas DataFrames
# NOTE: The file paths used here are placeholders. You will need to replace them
# with the actual paths to your files on your local system or environment.

try:
    # Load the first file
    str1 = r"C:\Users\siddh\OneDrive\Documents\Agricultural Datasets\Agmarknet_Price_Report_Bajra_2015-2019.xls"
    str2 = r"C:\Users\siddh\OneDrive\Documents\Agricultural Datasets\Agmarknet_Price_Report_Bajra_2019-2022.xls"
    str3 = r"C:\Users\siddh\OneDrive\Documents\Agricultural Datasets\Agmarknet_Price_Report_Bajra_2022-2025.xls"
    df1 = pd.read_excel(str1, engine='openpyxl')
    # Load the second file
    df2 = pd.read_excel(str2, engine='openpyxl')
    # Load the third file
    df3 = pd.read_excel(str3, engine='openpyxl')

    # Step 2: Combine the three DataFrames into one
    # The ignore_index=True argument re-indexes the new combined DataFrame
    bajra_df = pd.concat([df1, df2, df3], ignore_index=True)

    # --- Step 3: Data Cleaning and Pre-processing ---

    # Rename columns for clarity and ease of use
    bajra_df.rename(columns={
        'Sl no.': 'serial_number',
        'District Name': 'district_name',
        'Market Name': 'market_name',
        'Commodity': 'commodity',
        'Variety': 'variety',
        'Grade': 'grade',
        'Min Price (Rs./Quintal)': 'min_price',
        'Max Price (Rs./Quintal)': 'max_price',
        'Modal Price (Rs./Quintal)': 'modal_price',
        'Price Date': 'date'
    }, inplace=True)

    # Convert the 'date' column to datetime objects
    # This is critical for any time-series analysis or sorting by date
    bajra_df['date'] = pd.to_datetime(bajra_df['date'])

    # Ensure all price columns are numeric, converting any errors to NaN (Not a Number)
    price_cols = ['min_price', 'max_price', 'modal_price']
    for col in price_cols:
        bajra_df[col] = pd.to_numeric(bajra_df[col], errors='coerce')

    # Handle missing values - a simple approach is to drop rows with any missing prices
    bajra_df.dropna(subset=price_cols, inplace=True)
    
    # Remove any potential duplicate rows
    bajra_df.drop_duplicates(inplace=True)

    # Sort the entire dataset by date
    bajra_df.sort_values(by='date', inplace=True)


    # --- Step 4: Feature Engineering (Optional but Recommended) ---

    # Extract year, month, and day from the date for easier analysis
    bajra_df['year'] = bajra_df['date'].dt.year
    bajra_df['month'] = bajra_df['date'].dt.month
    bajra_df['day'] = bajra_df['date'].dt.day


    # --- Final Output ---
    print("✅ Data combined and cleaned successfully!")
    print("\nTotal number of rows in the combined dataset:", len(bajra_df))
    print("\nFirst 5 rows of the cleaned data:")
    print(bajra_df.head().to_markdown(index=False))
    
    print("\nLast 5 rows of the cleaned data:")
    print(bajra_df.tail().to_markdown(index=False))

    print("\nBasic information about the cleaned dataset:")
    # Using a string buffer to capture the info output to print it
    buffer = io.StringIO()
    bajra_df.info(buf=buffer)
    print(buffer.getvalue())

except FileNotFoundError as e:
    print(f"❌ Error: {e}. Please make sure the file paths are correct.")