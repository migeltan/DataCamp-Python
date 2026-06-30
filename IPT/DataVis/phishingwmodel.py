import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ── Load Data ─────────────────────────────────────────────────────────────────
train = pd.read_csv("IPT\DataVis\TrainingSet.csv")
test  = pd.read_csv("IPT\DataVis\TestSet.csv")

features = [
    'IsHTTPS', 'HasObfuscation', 'NoOfSubDomain',
    'NoOfEqualsInURL', 'NoOfQMarkInURL', 'NoOfOtherSpecialCharsInURL',
    'TLDLegitimateProb', 'HasTitle', 'HasFavicon', 'Robots', 'IsResponsive',
    'HasDescription', 'HasExternalFormSubmit', 'HasSocialNet', 'HasSubmitButton',
    'HasPasswordField', 'HasCopyrightInfo'
]
target = 'label'

# ── Train Model ───────────────────────────────────────────────────────────────
model = BernoulliNB(alpha=1.0)
model.fit(train[features], train[target])

train_pred = model.predict(train[features])
test_pred  = model.predict(test[features])

train_acc = accuracy_score(train[target], train_pred) * 100
test_acc  = accuracy_score(test[target], test_pred)  * 100

plt.rcParams.update({'font.family': 'DejaVu Sans', 'axes.spines.top': False, 'axes.spines.right': False})

# ── Figure 4: Confusion Matrix ─────────────────────────────────────────────
cm = confusion_matrix(test[target], test_pred)
fig, ax = plt.subplots(figsize=(7, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', linewidths=1,
            linecolor='white', xticklabels=['Legitimate', 'Phishing'],
            yticklabels=['Legitimate', 'Phishing'],
            annot_kws={'size': 16, 'weight': 'bold'}, ax=ax,
            cbar_kws={'label': 'Count'})
ax.set_title('Figure 4. Confusion Matrix (Test Set)', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Predicted Label', fontsize=12)
ax.set_ylabel('Actual Label', fontsize=12)
plt.tight_layout()
plt.savefig('figure4_confusion_matrix.png', dpi=150, bbox_inches='tight')
plt.show()
print("Saved: figure4_confusion_matrix.png")

# ── Figure 5: Training vs Test Accuracy ───────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 5))
sets   = ['Training Set', 'Test Set']
accs   = [train_acc, test_acc]
colors = ['#4C9BE8', '#E8604C']
bars   = ax.bar(sets, accs, color=colors, width=0.4, edgecolor='white')

for bar, acc in zip(bars, accs):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() - 1.5,
            f'{acc:.2f}%',
            ha='center', va='top', fontsize=13, fontweight='bold', color='white')

ax.set_ylim(90, 100)
ax.set_title('Figure 5. Training vs Test Accuracy Comparison', fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel('Accuracy (%)', fontsize=12)
ax.set_xlabel('Dataset Split', fontsize=12)
plt.tight_layout()
plt.savefig('figure5_accuracy_comparison.png', dpi=150, bbox_inches='tight')
plt.show()
print("Saved: figure5_accuracy_comparison.png")

# ── Figure 6 Per-Class Classification Metrics ────────────────────────────
report    = classification_report(test[target], test_pred,
                                   target_names=['Legitimate', 'Phishing'],
                                   output_dict=True)
metrics   = ['Precision', 'Recall', 'F1-Score']
legit_val = [report['Legitimate']['precision'], report['Legitimate']['recall'], report['Legitimate']['f1-score']]
phish_val = [report['Phishing']['precision'],   report['Phishing']['recall'],   report['Phishing']['f1-score']]

x   = np.arange(len(metrics))
w   = 0.3
fig, ax = plt.subplots(figsize=(9, 6))
b1 = ax.bar(x - w/2, legit_val, w, label='Legitimate', color='#4C9BE8', edgecolor='white')
b2 = ax.bar(x + w/2, phish_val, w, label='Phishing',   color='#E8604C', edgecolor='white')

for bar in list(b1) + list(b2):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.002,
            f'{bar.get_height():.2f}',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_ylim(0.9, 1.02)
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=12)
ax.set_ylabel('Score', fontsize=12)
ax.set_title('Figure 6. Per-Class Classification Metrics (Test Set)', fontsize=14, fontweight='bold', pad=15)
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig('figure6_classification_metrics.png', dpi=150, bbox_inches='tight')
plt.show()
print("Saved: figure6_classification_metrics.png")

print("\nAll figures saved successfully.")