import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# ─────────────────────────────────────────────
# 1. Load the dataset
# ─────────────────────────────────────────────
df_raw = pd.read_csv(".\IPT\Finals\secret2a.csv", index_col="Transaction ID")

print("=" * 60)
print("         BATCH #2 – SET A  |  ASSOCIATION RULES MINING")
print("=" * 60)

print("\n[a] INITIAL DATASET (Six Transactions)\n")
print(df_raw.to_string())

# ─────────────────────────────────────────────
# 2. Convert to list-of-items format for TransactionEncoder
# ─────────────────────────────────────────────
items_list = []
for _, row in df_raw.iterrows():
    basket = [item for item, present in row.items() if present == 1]
    items_list.append(basket)

# ─────────────────────────────────────────────
# 3. Apply TransactionEncoder
# ─────────────────────────────────────────────
te = TransactionEncoder()
te_array = te.fit_transform(items_list)
df_encoded = pd.DataFrame(te_array, columns=te.columns_)
df_encoded.index = range(1, len(df_encoded) + 1)
df_encoded.index.name = "Transaction ID"

print("\n[b] TRANSACTION-ENCODED DATASET\n")
print(df_encoded.to_string())

# ─────────────────────────────────────────────
# 4. Mine frequent itemsets
# ─────────────────────────────────────────────
MIN_SUPPORT    = 0.20
MIN_CONFIDENCE = 0.50

frequent_itemsets = apriori(
    df_encoded,
    min_support=MIN_SUPPORT,
    use_colnames=True
)

# ─────────────────────────────────────────────
# 5. Generate association rules
# ─────────────────────────────────────────────
rules = association_rules(
    frequent_itemsets,
    metric="confidence",
    min_threshold=MIN_CONFIDENCE,
    num_itemsets=len(frequent_itemsets)
)

rules = rules.sort_values(["confidence", "lift"], ascending=False).reset_index(drop=True)

# ─────────────────────────────────────────────
# 6. Display results
# ─────────────────────────────────────────────
print("\n[c] ASSOCIATION RULES\n")
print(f"    Minimum Support    : {MIN_SUPPORT}")
print(f"    Minimum Confidence : {MIN_CONFIDENCE}")
print()

if rules.empty:
    print("  No rules met the minimum thresholds.")
else:
    display_cols = ["antecedents", "consequents", "support", "confidence", "lift", "conviction"]
    rules_display = rules[display_cols].copy()

    # Pretty-print frozensets
    rules_display["antecedents"] = rules_display["antecedents"].apply(
        lambda x: ", ".join(sorted(x))
    )
    rules_display["consequents"] = rules_display["consequents"].apply(
        lambda x: ", ".join(sorted(x))
    )

    rules_display.index = range(1, len(rules_display) + 1)
    rules_display.index.name = "Rule #"

    # Round for readability
    rules_display["support"]    = rules_display["support"].round(4)
    rules_display["confidence"] = rules_display["confidence"].round(4)
    rules_display["lift"]       = rules_display["lift"].round(4)
    rules_display["conviction"] = rules_display["conviction"].apply(
        lambda x: round(x, 4) if x != float("inf") else "∞"
    )

    print(rules_display.to_string())

print("\n" + "=" * 60)
print("                      END OF OUTPUT")
print("=" * 60)