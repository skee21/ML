import csv
with open ("data.csv", 'r') as file:
    reader = csv.reader(file)
    print("Input Training Dataset")
    num_attributes = 6
    training_data = []
    for row in reader:
        training_data.append(row)
        print(row)
print("Applying Find-S Algorithm")
print("Initial Hypothesis")
hypothesis = ['0'] * num_attributes
print(hypothesis)
for i in range(len(training_data)):
    if training_data[i][num_attributes] == "Yes":
        for j in range(num_attributes):
            if (hypothesis[j] == '0') or hypothesis[j] == training_data[i][j]:
                hypothesis[j] = training_data[i][j]
            else:
                hypothesis[j] = '?'
print(hypothesis)
print(f"After applying FindS Algorithm {hypothesis}")
