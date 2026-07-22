# Omitting the validation set and splitting the dataset into train/test with ratio 60:40

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Loading the default wine dataset
data = load_wine()
X = data.data
y = data.target

# Splitting data into train (60%) and test (40%)sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state = 42, stratify = y)

# Fitting the logistic regression model
model = LogisticRegression(max_iter = 2900, random_state = 42)
model.fit(X_train, y_train)

# Evaluating the test set
test_preds = model.predict(X_test)
test_accuracy = accuracy_score(y_test, test_preds)
print(f"Test Accuracy: {test_accuracy:.4f}")

# Detailed classification report on test set
print("\nClassification Report on Test Set:")
print(classification_report(y_test, test_preds, target_names=data.target_names))

```OUTPUT:
Test Accuracy: 0.9583

Classification Report on Test Set:
              precision    recall  f1-score   support

     class_0       0.96      1.00      0.98        24
     class_1       0.93      0.97      0.95        29
     class_2       1.00      0.89      0.94        19

    accuracy                           0.96        72
   macro avg       0.96      0.95      0.96        72
weighted avg       0.96      0.96      0.96        72
```
