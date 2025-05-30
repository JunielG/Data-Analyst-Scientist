# First, let's examine the structure of your data
print("Unique values in 'num_effects':")
print(drug_safety["num_effects"].value_counts().sort_index())
print("\nUnique values in 'trx':")
print(drug_safety["trx"].value_counts())

# Check the current contingency table shape
contingency_table = pd.crosstab(drug_safety["num_effects"], drug_safety["trx"])
print(f"\nCurrent contingency table shape: {contingency_table.shape}")
print("Current contingency table:")
print(contingency_table)

# Solution 1: Convert num_effects to binary (0 effects vs 1+ effects)
drug_safety["has_effects"] = (drug_safety["num_effects"] > 0).astype(int)
contingency_table_binary = pd.crosstab(drug_safety["has_effects"], drug_safety["trx"])
print(f"\nBinary contingency table shape: {contingency_table_binary.shape}")
print("Binary contingency table (0=No effects, 1=Has effects):")
print(contingency_table_binary)

# Solution 2: If you want to compare specific effect counts (e.g., 0 vs 1 effects only)
# Filter data to include only rows with 0 or 1 effects
filtered_data = drug_safety[drug_safety["num_effects"].isin([0, 1])]
if len(filtered_data) > 0:
    contingency_table_filtered = pd.crosstab(filtered_data["num_effects"], filtered_data["trx"])
    print(f"\nFiltered contingency table shape (0 vs 1 effects only): {contingency_table_filtered.shape}")
    print("Filtered contingency table:")
    print(contingency_table_filtered)

# Solution 3: Create specific categories for num_effects
def categorize_effects(num_effects):
    if num_effects == 0:
        return "No effects"
    elif num_effects <= 2:
        return "Few effects (1-2)"
    else:
        return "Many effects (3+)"

drug_safety["effect_category"] = drug_safety["num_effects"].apply(categorize_effects)
print(f"\nEffect categories:")
print(drug_safety["effect_category"].value_counts())

# Create 2x2 table by combining categories if needed
drug_safety["effect_binary"] = drug_safety["num_effects"].apply(
    lambda x: "No effects" if x == 0 else "Has effects"
)
contingency_table_final = pd.crosstab(drug_safety["effect_binary"], drug_safety["trx"])
print(f"\nFinal 2x2 contingency table shape: {contingency_table_final.shape}")
print("Final 2x2 contingency table:")
print(contingency_table_final)

# If you need the table as a numpy array for statistical tests
contingency_array = contingency_table_final.values
print(f"\nAs numpy array shape: {contingency_array.shape}")
print("Array:")
print(contingency_array)


# For chi-square test
from scipy.stats import chi2_contingency
chi2, p_value, dof, expected = chi2_contingency(contingency_table_final)

# For Fisher's exact test (if small sample sizes)
from scipy.stats import fisher_exact
odds_ratio, p_value = fisher_exact(contingency_table_final)