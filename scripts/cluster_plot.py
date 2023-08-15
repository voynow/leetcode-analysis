import numpy as np
import pickle
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

def load_embeddings(filepath):
    return pickle.load(open(filepath, 'rb'))

def perform_clustering(embeddings, n_clusters=5):
    kmeans = KMeans(n_clusters=n_clusters)
    return kmeans.fit_predict(embeddings)

def reduce_dimensionality(embeddings):
    tsne = TSNE(n_components=2, random_state=42)
    return tsne.fit_transform(embeddings)

def plot_clusters(reduced_embeddings, labels, filenames, n_clusters):
    plt.style.use('dark_background')
    plt.figure(figsize=(15, 10))

    # Scatter plot for each cluster
    for cluster_id in range(n_clusters):
        cluster_embeddings = reduced_embeddings[labels == cluster_id]
        plt.scatter(cluster_embeddings[:, 0], cluster_embeddings[:, 1], label=f'Cluster {cluster_id}')

    # Annotate the plot with filenames
    for i, filename in enumerate(filenames):
        plt.annotate(filename, (reduced_embeddings[i, 0], reduced_embeddings[i, 1]), fontsize=8, alpha=0.7)

    plt.title('Clusters of Python Files in Embedding Space')
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.legend()
    plt.savefig('data/clusters.png')

if __name__ == "__main__":
    embeddings_dict = load_embeddings('data/embeddings.pkl')
    embedding_list = [v['embedding'] for v in embeddings_dict.values()]
    file_names = list(embeddings_dict.keys())
    embedding_matrix = np.array(embedding_list)

    labels = perform_clustering(embedding_matrix)
    reduced_embeddings = reduce_dimensionality(embedding_matrix)
    plot_clusters(reduced_embeddings, labels, file_names, n_clusters=5)
