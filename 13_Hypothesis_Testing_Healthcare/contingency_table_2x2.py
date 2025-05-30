import pandas as pd
import numpy as np

# Assume 'drug_safety' is your DataFrame
# Let's create a sample DataFrame for demonstration
data = {'num_effects': np.random.randint(0, 3, 100),
        'trx': np.random.choice(['A', 'B', 'C'], 100)}
drug_safety = pd.DataFrame(data)

# Create the initial contingency table
contingency_table_original = pd.crosstab(drug_safety["num_effects"], drug_safety["trx"])
print("Original Contingency Table:\n", contingency_table_original)

# Dichotomize 'num_effects': Let's say 0 effects is 'No Effect', and 1 or more is 'Effect'
drug_safety['has_effect'] = drug_safety['num_effects'].apply(lambda x: 'Yes' if x > 0 else 'No')

# Dichotomize 'trx': Let's say 'A' is the treatment of interest, and 'B' and 'C' are the control
drug_safety['treatment_vs_control'] = drug_safety['trx'].apply(lambda x: 'Treatment' if x == 'A' else 'Control')

# Create the 2x2 contingency table
contingency_table_2x2 = pd.crosstab(drug_safety["has_effect"], drug_safety["treatment_vs_control"])
print("\n2x2 Contingency Table:\n", contingency_table_2x2)