import pandas as pd
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score, classification_report

# Load separate train and test sets
train_data = pd.read_csv("./IPT/DataVis/TrainingSet.csv")
test_data  = pd.read_csv("./IPT/DataVis/TestSet.csv")

print("Training set shape:", train_data.shape)
print("Testing set shape: ", test_data.shape)

features = [
    "IsHTTPS", "HasObfuscation", "NoOfSubDomain",
    "NoOfEqualsInURL", "NoOfQMarkInURL", "NoOfOtherSpecialCharsInURL",
    "TLDLegitimateProb", "HasTitle", "HasFavicon", "Robots", "IsResponsive", 
    "HasDescription", "HasExternalFormSubmit", "HasSocialNet", "HasSubmitButton", 
    "HasPasswordField", "HasCopyrightInfo"
]
target = "label"

features_train = train_data[features]
target_train   = train_data[target]

features_test  = test_data[features]
target_test    = test_data[target]

# Train the model
# BernoulliNB is used instead of GaussianNB because all features here are
# binary (0/1) flags, not continuous values. alpha=1.0 applies Laplace
# smoothing (the "+1" smoothing), matching the Laplace=1 assumption in the
# spreadsheet's likelihood tables.
model = BernoulliNB(alpha=1.0)
model.fit(features_train, target_train)

# --- Training set evaluation (to check for overfitting) ---
train_pred = model.predict(features_train)
train_accuracy = accuracy_score(target_train, train_pred)
print(f"\nTraining Accuracy = {train_accuracy * 100:.2f}%")

# Predict and evaluate on test set
pred = model.predict(features_test)

accuracy = accuracy_score(target_test, pred)
print(f"Test Accuracy     = {accuracy * 100:.2f}%")

# Compare the two to check for overfitting
gap = (train_accuracy - accuracy) * 100
print(f"Train-Test Gap    = {gap:.2f} percentage points")

print("\nClassification Report (Test Set):")
print(classification_report(target_test, pred, target_names=["Legitimate", "Phishing"]))

# --- Example prediction --- 
sample = pd.DataFrame([[1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1]], columns=features)
answer = model.predict(sample)

print("\n--- Example Prediction ---")
if answer[0] == 1:
    print(1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1)
    print("Result: PHISHING site")
else:
    print(1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1)
    print("Result: LEGITIMATE site")

print("\n\n--- Example 20 URLs ---\n")
sample_20 = test_data.sample(20, random_state=42).copy()
sample_20["Predicted"] = model.predict(sample_20[features])
sample_20["Actual"] = sample_20["label"]
print(sample_20[["URL", "Actual", "Predicted"]])