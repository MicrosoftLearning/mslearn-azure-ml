# Import libraries
import argparse
import glob
import pandas as pd
import numpy as np
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import pickle
from pathlib import Path

# get parameters
parser = argparse.ArgumentParser("train")
parser.add_argument("--training_data", type=str, help="Path to training data")
parser.add_argument("--reg_rate", type=float, default=0.01)
parser.add_argument("--model_output", type=str, help="Path of output model")

args = parser.parse_args()

training_data = args.training_data

# load the prepared data file in the training folder
print("Loading Data...")
data_path = args.training_data
all_files = glob.glob(data_path + "/*.csv")
df = pd.concat((pd.read_csv(f) for f in all_files), sort=False)

# Separate features and labels
X, y = df[['Pregnancies','PlasmaGlucose','DiastolicBloodPressure','TricepsThickness','SerumInsulin','BMI','DiabetesPedigree','Age']].values, df['Diabetic'].values

# Split data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

# Train a logistic regression model
print('Training a logistic regression model...')
model = LogisticRegression(C=1/args.reg_rate, solver="liblinear").fit(X_train, y_train)

# calculate accuracy
y_pred = model.predict(X_test)
acc = np.average(y_pred == y_test)
mlflow.log_metric("Accuracy", np.float(acc))

# create confusion matrix
conf_matrix = confusion_matrix(y_true=y_test, y_pred=y_pred)
fig, ax = plt.subplots(figsize=(7.5, 7.5))
ax.matshow(conf_matrix, cmap=plt.cm.Blues, alpha=0.3)
for i in range(conf_matrix.shape[0]):
    for j in range(conf_matrix.shape[1]):
        ax.text(x=j, y=i,s=conf_matrix[i, j], va='center', ha='center', size='xx-large')

plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.savefig("ConfusionMatrix.png")
mlflow.log_artifact("ConfusionMatrix.png")

# Output the model and test data
pickle.dump(model, open((Path(args.model_output) / "model.sav"), "wb"))