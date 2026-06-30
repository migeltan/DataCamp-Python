import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

df = pd.read_csv(".\IPT\Finals\Batch1.csv")
print("\na. Six Transactions:")
print(df.to_string(index=False))

waw = ["Hamburger", "French Fries", "Soda", "Spaghetti"]

transactions = []
for _, row in df.iterrows():
    basket = [waw for waw in waw if row[waw] == 1]
    transactions.append(basket)

te = TransactionEncoder()
te_array = te.fit(transactions).transform(transactions)
df_encoded = pd.DataFrame(te_array, columns=te.columns_)

print("\nb. Converted Datafile Using Transaction Encoder:")
print(df_encoded.to_string(index=False))

min_support    = 0.20
min_confidence = 0.50

frequent_itemsets = apriori(df_encoded,
                            min_support=min_support,
                            use_colnames=True)
frequent_itemsets["support"] = frequent_itemsets["support"].round(4)

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence,
                          num_itemsets=len(frequent_itemsets))

rules = rules[["antecedents", "consequents",
               "support", "confidence", "lift", "conviction"]]
rules = rules.round(4)

print("\c. Association Rules (min_support=0.20, min_confidence=0.50):")
print("-" * 90)

for _, row in rules.iterrows():
    ant = ", ".join(list(row["antecedents"]))
    con = ", ".join(list(row["consequents"]))
    print(f"  Rule      : {{{ant}}} => {{{con}}}")
    print(f"  Support   : {row['support']}")
    print(f"  Confidence: {row['confidence']}")
    print(f"  Lift      : {row['lift']}")
    conviction_str = (f"{row['conviction']}"
                      if row['conviction'] != float('inf')
                      else "inf")
    print(f"  Conviction: {conviction_str}")
