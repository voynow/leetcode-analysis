import numpy as np
import pickle
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


embeddings = pickle.load(open('data/embeddings.pkl', 'rb'))
embedding_list = [v['embedding'] for v in embeddings.values()]
file_names = list(embeddings.keys())

# Convert to a numpy array for clustering
embedding_matrix = np.array(embedding_list)

# Perform K-Means clustering
n_clusters = 5
kmeans = KMeans(n_clusters=n_clusters)
labels = kmeans.fit_predict(embedding_matrix)

# Reduce dimensionality using t-SNE
tsne = TSNE(n_components=2, random_state=42)
reduced_embeddings = tsne.fit_transform(embedding_matrix)

# Plot the clusters with dark theme
plt.style.use('dark_background')
plt.figure(figsize=(15, 10))

# Scatter plot for each cluster
for cluster_id in range(n_clusters):
    cluster_embeddings = reduced_embeddings[labels == cluster_id]
    plt.scatter(cluster_embeddings[:, 0], cluster_embeddings[:, 1], label=f'Cluster {cluster_id}')

# Annotate the plot with filenames
for i, filename in enumerate(file_names):
    plt.annotate(filename, (reduced_embeddings[i, 0], reduced_embeddings[i, 1]), fontsize=8, alpha=0.7)

plt.title('Clusters of Python Files in Embedding Space')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.legend()
plt.savefig('data/clusters.png')

