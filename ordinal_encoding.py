# Read files from csv file and encode the ordinal features
# and save the encoded data to a new csv file
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# Step 1: Read the Excel file
df = pd.read_excel('./Behältertypen.xlsx')

# Step 2: Select the columns to be encoded
columns_to_encode = df.columns[2:5]  # Columns C to E

# Step 3: Initialize the OrdinalEncoder
encoder = OrdinalEncoder()

# Step 4: Fit and transform the selected columns
encoded_columns = encoder.fit_transform(df[columns_to_encode])

# Step 5: Replace the original columns with the encoded ones
df[columns_to_encode] = encoded_columns

# Now df has the encoded columns# Save the encoded data to a new Excel file
df.to_excel('Ordinal_Behältertypen.xlsx', index=False)
