pip install minisom -q
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from minisom import MiniSom
data=load_iris().data
scaler=MinMaxScaler()
data_scaled=scaler.fit_transform(data)
som=MiniSom(
    x=7,
    y=7,
    input_len=data_scaled.shape[1],
    sigma=1.0,
    learning_rate=0.5,
    random_seed=42
)
som.random_weights_init(data_scaled)
som.train_random(data_scaled,num_iteration=1000)
print("Training is Completed Successfully")
plt.figure(figsize=(7,7))
plt.pcolor(som.distance_map().T)
plt.colorbar(label="Distance")
plt.title("SOM U-Matrix (Cluster Visualization)")
plt.show()
clusters=[som.winner(x) for x in data_scaled]
print("\n Sample Cluster Assignments:")
for i in range(5):
    x,y = clusters[i]
    print(f"Data Point {i+1}->Cluster({x},{y})")