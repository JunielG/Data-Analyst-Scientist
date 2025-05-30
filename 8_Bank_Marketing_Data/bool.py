# Method 1: Using map (most concise)
df['credit_default'] = df['credit_default'].map({'yes': 1, 'no': 0}).astype(bool)

# Method 2: Using np.where (NumPy, efficient for large DataFrames)
import numpy as np
df['credit_default'] = np.where(df['credit_default'] == 'yes', True, False).astype(bool)

# Method 3: Using replace (Pandas, also efficient)
df['credit_default'] = df['credit_default'].replace({'yes': True, 'no': False}).astype(bool)

# Method 4: Using apply (less efficient, but more flexible for complex logic)
def convert_to_bool(value):
    if value == 'yes':
        return True
    elif value == 'no':
        return False
    else:  # Handle other cases (e.g., missing values, different strings)
        return False  # Or another appropriate default value
df['credit_default'] = df['credit_default'].apply(convert_to_bool).astype(bool)

# Method 5: Using a simple if/else in a list comprehension (less efficient)
df['credit_default'] = [True if x == 'yes' else False for x in df['credit_default']].astype(bool)

# Check the data type:
print(df['credit_default'].dtype)  # Output: bool

#Verify the values:
print(df['credit_default'].unique()) #Should print [True, False]