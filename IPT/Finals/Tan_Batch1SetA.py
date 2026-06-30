import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules


data_sets = pd.read_csv(".\IPT\Finals\Batch1.csv")
print("\n")
print("a. Initial Dataset")
print(data_sets.to_string(index=False))

waw = [
    ["Hamburger", "French Fries", "Soda", "Spaghetti"],
    ["Hamburger", "Soda",         "Spaghetti"],
    ["Soda",      "Spaghetti"],
    ["French Fries"],
    ["Hamburger", "French Fries", "Soda",  "Spaghetti"],
    ["Hamburger", "French Fries", "Spaghetti"],
]


te   = TransactionEncoder()
item = te.fit(waw).transform(waw)
df   = pd.DataFrame(item, columns=te.columns_)

num_records = len(df)
print("\nnumber of records in dataframe", num_records)
print("b. Converted to Dataframe \n", df.to_string(index=False))

frequent_itemsets = apriori(df, min_support=0.20, use_colnames=True, max_len=3)
print("\nfrequent itemsets\n", frequent_itemsets.to_string(index=False))

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.50, num_itemsets=len(frequent_itemsets))

display_cols = ["antecedents", "consequents", "support", "confidence", "lift", "conviction"]
rules = rules[display_cols].copy()

rules["antecedents"] = rules["antecedents"].apply(lambda x: "{" + ", ".join(sorted(x)) + "}")
rules["consequents"] = rules["consequents"].apply(lambda x: "{" + ", ".join(sorted(x)) + "}")

for col in ["support", "confidence", "lift", "conviction"]:
    rules[col] = rules[col].apply(lambda x: f"{x:.4f}" if x != float("inf") else "inf")

col_widths = {col: max(len(col), rules[col].astype(str).map(len).max())
              for col in display_cols}

header = "|" + "|".join(f" {c:<{col_widths[c]}} " for c in display_cols) + "|"

print("\nc. Association Rules (min_support=0.20 | min_confidence=0.50)\n")
print(header)
for _, row in rules.iterrows():
    line = "|" + "|".join(f" {str(row[c]):<{col_widths[c]}} " for c in display_cols) + "|"
    print(line)
