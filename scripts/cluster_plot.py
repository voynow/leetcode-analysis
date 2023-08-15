import numpy as np
import pickle
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def load_embeddings(filepath):
    """Load embeddings from a pickle file."""
    return pickle.load(open(filepath, "rb"))

def perform_clustering(embeddings, n_clusters=5):
    """Perform KMeans clustering on embeddings."""
    kmeans = KMeans(n_clusters=n_clusters)
    return kmeans.fit_predict(embeddings)

def reduce_dimensionality(embeddings):
    """Reduce dimensionality using t-SNE."""
    tsne = TSNE(n_components=2, random_state=42)
    return tsne.fit_transform(embeddings)

def plot_clusters(reduced_embeddings, labels, file_names):
    """Plot clusters with Matplotlib using a dark theme and color-blind friendly palette."""
    # Set dark background style
    plt.style.use('dark_background')

    # Create DataFrame for plotting
    df = pd.DataFrame({
        'x': reduced_embeddings[:, 0],
        'y': reduced_embeddings[:, 1],
        'labels': labels,
        'file_names': file_names
    })

    # Create figure and axes
    fig, ax = plt.subplots(figsize=(12, 10))

    # Define unique labels and color palette
    unique_labels = sorted(list(set(labels)))
    colors = sns.color_palette("colorblind", len(unique_labels))

    # Plot each cluster
    for label, color in zip(unique_labels, colors):
        idx = df['labels'] == label
        ax.scatter(df['x'][idx], df['y'][idx], c=[color], s=100, alpha=0.6, edgecolors='lightgrey', linewidth=0.5, label=f'Cluster {label}')
        for i, txt in enumerate(df['file_names'][idx]):
            ax.annotate(txt, (df['x'][idx].iloc[i], df['y'][idx].iloc[i]), fontsize=8, alpha=0.7, color='w', xytext=(5,0), textcoords='offset points')

    # Add legend and labels
    ax.legend(title="Clusters")
    ax.set_title('Cluster Visualization', fontsize=16, fontweight='bold')
    ax.set_xlabel('Dimension 1')
    ax.set_ylabel('Dimension 2')

    plt.grid(False)
    plt.tight_layout()
    plt.savefig("data/cluster_plot.png")

if __name__ == "__main__":
    embeddings_dict = load_embeddings("data/embeddings.pkl")
    embedding_list = [v["embedding"] for v in embeddings_dict.values()]
    file_names = list(embeddings_dict.keys())
    embedding_matrix = np.array(embedding_list)

    labels = perform_clustering(embedding_matrix)
    reduced_embeddings = reduce_dimensionality(embedding_matrix)

    plot_clusters(reduced_embeddings, labels, file_names)
