import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
iris=load_iris()
X=pd.DataFrame(iris.data, columns=iris.feature_names)
print(X)
print("\n")
#raw data (before clustering)
plt.scatter(X.iloc[:,2],X.iloc[:,3],c='green',s=40,alpha=0.6)
plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[3])
plt.title(" Before Clustering(Raw Data)") 
plt.show()
k=3
kmeans=KMeans(n_clusters=k,random_state=42)
kmeans.fit(X)
plt.scatter(X.iloc[:,2],X.iloc[:,3],c=kmeans.labels_,cmap='viridis',s=40,alpha=0.6)
plt.scatter(kmeans.cluster_centers_[:,2],kmeans.cluster_centers_[:,3],c='red',marker='X',s=200,label='Centroids')
plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[3])
plt.title(" After Clustering (K Means)") 
plt.legend()
plt.show()