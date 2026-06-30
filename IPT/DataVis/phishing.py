import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import numpy as np

# ── Config ─────────────────────────────────────────────────────────────────
CSV_PATH       = "IPT\DataVis\w-url.csv"
TRAIN_CSV_PATH = "IPT\DataVis\TrainingSet.csv"
TEST_CSV_PATH  = "IPT\DataVis\TestSet.csv"
LABEL_COL      = "label"
PALETTE        = {0: "#4C9BE8", 1: "#E8604C"}
plt.rcParams.update({"font.family": "DejaVu Sans",
                     "axes.spines.top": False, "axes.spines.right": False})

df    = pd.read_csv(CSV_PATH)
train = pd.read_csv(TRAIN_CSV_PATH)
test  = pd.read_csv(TEST_CSV_PATH)

# ── Figure 1. Class Distribution Bar Chart ─────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 5))
counts = df[LABEL_COL].value_counts().sort_index()
labels = ["Legitimate (0)", "Phishing (1)"]
bars   = ax.bar(labels, counts.values,
                color=[PALETTE[0], PALETTE[1]], width=0.5, edgecolor="white")
for bar, count in zip(bars, counts.values):
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + counts.max() * 0.01,
            f"{count:,}\n({count/len(df)*100:.1f}%)",
            ha="center", va="bottom", fontsize=11, fontweight="bold")
ax.set_title("Figure 1. Class Distribution of the Dataset",
             fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Class Label", fontsize=12)
ax.set_ylabel("Number of Samples", fontsize=12)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
ax.set_ylim(0, counts.max() * 1.15)
plt.tight_layout()
plt.savefig("figure1_class_distribution.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: figure1_class_distribution.png")

# ── Figure 3. Correlation Heatmap (URLSimilarityIndex & IsDomainIP removed) ─
DROP_COLS = ["URLSimilarityIndex", "IsDomainIP", "URL"]
df_corr   = df.drop(columns=[c for c in DROP_COLS if c in df.columns])
corr      = df_corr.corr(numeric_only=True)
mask      = pd.DataFrame(False, index=corr.index, columns=corr.columns)
mask[np.triu(np.ones(corr.shape), k=1).astype(bool)] = True

fig, ax = plt.subplots(figsize=(14, 11))
sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap="coolwarm",
            center=0, linewidths=0.5, linecolor="#e0e0e0",
            annot_kws={"size": 8},
            cbar_kws={"shrink": 0.8, "label": "Pearson Correlation"}, ax=ax)
ax.set_title("Figure 3. Feature Correlation Heatmap\n"
             "(Lower triangle — Pearson r; darker red = stronger positive, "
             "darker blue = stronger negative)",
             fontsize=13, fontweight="bold", pad=15)
ax.tick_params(axis="x", rotation=45, labelsize=9)
ax.tick_params(axis="y", rotation=0,  labelsize=9)

# ── Fix: force tick positions to cell centers ──────────────────────────────
n = len(corr)
ax.set_xticks(np.arange(n) + 0.5)
ax.set_xticklabels(corr.columns, rotation=45, ha="right", fontsize=9)
ax.set_yticks(np.arange(n) + 0.5)
ax.set_yticklabels(corr.index, rotation=0, fontsize=9)

plt.tight_layout()
plt.savefig("figure3_correlation_heatmap.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: figure3_correlation_heatmap.png")

# ── Figure 2. Train vs Test — Grouped Column Chart ─────────────────────────
train_counts = train[LABEL_COL].value_counts().sort_index()
test_counts  = test[LABEL_COL].value_counts().sort_index()

x  = np.arange(2)
w  = 0.35
fig, ax = plt.subplots(figsize=(8, 6))
b1 = ax.bar(x - w/2, train_counts.values, w,
            label="Training Set", color="#4C9BE8", edgecolor="white")
b2 = ax.bar(x + w/2, test_counts.values,  w,
            label="Test Set",     color="#E8604C", edgecolor="white")

for bar in list(b1) + list(b2):
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 30,
            f"{int(bar.get_height()):,}",
            ha="center", va="bottom", fontsize=11, fontweight="bold")

ax.set_title("Figure 2. Class Distribution Across Training and Test Sets",
             fontsize=14, fontweight="bold", pad=15)
ax.set_xticks(x)
ax.set_xticklabels(["Legitimate (0)", "Phishing (1)"], fontsize=12)
ax.set_ylabel("Number of Samples", fontsize=12)
ax.set_xlabel("Class Label", fontsize=12)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
ax.set_ylim(0, max(train_counts.max(), test_counts.max()) * 1.2)
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig("figure2_train_test_distribution.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: figure2_train_test_distribution.png")

print(df.groupby('label')[['HasSocialNet', 'HasCopyrightInfo', 'HasDescription', 'NoOfOtherSpecialCharsInURL']].mean())

print("\nAll figures saved successfully.")