1.Check the contingency table
First, examine the actual frequencies to understand the data distribution:

# Create contingency table to see the actual counts
contingency_table = pd.crosstab(drug_safety['num_effects'], drug_safety['trx'])
print("Contingency Table:")
print(contingency_table)

# Check expected frequencies
from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(contingency_table)
print("\nExpected frequencies:")
print(expected)

2.Consider alternative approaches
Option A: Use Fisher's exact test (if 2x2 table)

from scipy.stats import fisher_exact
# Only works for 2x2 tables
if contingency_table.shape == (2, 2):
    odds_ratio, p_value = fisher_exact(contingency_table)
    print(f"Fisher's exact test p-value: {p_value}")

Option B: Use Monte Carlo simulation

from scipy.stats import chi2_contingency
chi2, p_mc, dof, expected = chi2_contingency(contingency_table, lambda_="log-likelihood")
print(f"Monte Carlo p-value: {p_mc}")

Option C: Combine categories (if appropriate)
# If you have multiple categories with low counts, consider combining them
# This depends on your specific research question and data