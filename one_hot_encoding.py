# Read files from csv file and encode the one hot features
# and save the encoded data to a new csv file
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Step 1: Read the Excel file
df = pd.read_excel('./Behältertypen.xlsx')

# Step 2: Select the columns to be encoded
columns_to_encode = df.columns[2:5]  # Columns C to E

# Step 3: Initialize the OneHotEncoder
encoder = OneHotEncoder()

# Step 4: Fit and transform the selected columns
encoded_columns = encoder.fit_transform(df[columns_to_encode])

# Convert the csr_matrix to a DataFrame
encoded_df = pd.DataFrame(encoded_columns.toarray(), columns=encoder.get_feature_names_out(columns_to_encode))

# Step 5: Replace the original columns with the encoded ones
df = pd.concat([df, encoded_df], axis=1)

# Step 6: Save the encoded data to a new Excel file
df.to_excel('One_Hot_Behältertypen.xlsx', index=False)
