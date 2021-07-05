import pandas as pd

labels = pd.read_csv("Mirai_labels.csv", sep=",")
data = pd.read_csv("Mirai_dataset.csv", sep=",")

data['attack'] = labels

data.to_csv("Mirai_dataset.csv", index=False)