import xgboost as xgb
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset (Breast Cancer dataset as an example)
data = load_breast_cancer()
X, y = data.data, data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert data to DMatrix format (XGBoost's internal data structure)
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

# Set XGBoost parameters
params = {
    'objective': 'binary:logistic',  # for binary classification
    'eval_metric': 'error',  # evaluation metric
    'seed': 42
}

# Train the model
num_round = 100  # number of boosting iterations
xgb_classifier = xgb.train(params, dtrain, num_boost_round=num_round)

# Make predictions on the test set
y_pred = xgb_classifier.predict(dtest)
y_pred_binary = [1 if pred > 0.5 else 0 for pred in y_pred]  # Convert probabilities to binary labels

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred_binary)
print(f"Accuracy: {accuracy:.2f}")
