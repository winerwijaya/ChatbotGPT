import pandas as pd
import csv
import json

dataset_path = 'dataset/Mental_Health_FAQ_2.csv'

dataset = pd.read_csv(dataset_path, delimiter=';')

# print(dataset['Answers'][0])

# print(dataset.shape)
n = 0
for i in range(80):
    if ('â€™' in dataset['Answers'][i]):
        # print('test' + str(i))
        n += 1
        dataset['Answers'][i] = dataset['Answers'][i].replace("â€™", "\'")


dataset = dataset.drop(['Question_ID'], axis=1)
dataset.to_csv('dataset/Mental_Health_FAQ_3.csv', index=False, sep=',')

with open('dataset/Mental_Health_FAQ_3.csv', 'r', encoding="utf-8") as f:
    data = list(csv.reader(f))
    headers = data[0]
    data = data[1:]

faq_data = []
for question, answer in data:
    prompt = f"{question}\n"
    completion = f"Answer: {answer}\n"
    faq_data.append({"prompt": prompt, "completion": completion})

with open('dataset/prompt_completion_faq.json', 'w', encoding="utf-8") as f:
    json.dump(faq_data, f)
