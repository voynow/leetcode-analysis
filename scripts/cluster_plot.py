import logging
import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE

plt.style.use("dark_background")

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_embeddings(filepath):
    logging.info(f"Loading embeddings from {filepath}")
    return pickle.load(open(filepath, "rb"))


def perform_clustering(embeddings, n_clusters=5):
    logging.info("Performing KMeans clustering")
    kmeans = KMeans(n_clusters=n_clusters, n_init=10)
    return kmeans.fit_predict(embeddings)


def reduce_dimensionality(embeddings):
    logging.info("Reducing dimensionality using t-SNE")
    tsne = TSNE(n_components=2, random_state=42)
    return tsne.fit_transform(embeddings)


def plot_clusters(reduced_embeddings, labels, file_names, figname, annotate=True):
    logging.info(f"Plotting clusters to {figname}.png")

    df = pd.DataFrame(
        {
            "x": reduced_embeddings[:, 0],
            "y": reduced_embeddings[:, 1],
            "labels": labels,
            "file_names": file_names,
        }
    )

    # Define unique labels and color palette
    unique_labels = sorted(list(set(labels)))
    colors = sns.color_palette("colorblind", len(unique_labels))

    fig, ax = plt.subplots(figsize=(12, 10))
    for label, color in zip(unique_labels, colors):
        idx = df["labels"] == label
        ax.scatter(
            df["x"][idx],
            df["y"][idx],
            c=[color],
            s=100,
            alpha=0.6,
            edgecolors="lightgrey",
            linewidth=0.5,
            label=f"Cluster {label}",
        )

        # Annotate points with filenames if annotate is True
        if annotate:
            for i, txt in enumerate(df["file_names"][idx]):
                ax.annotate(
                    txt,
                    (df["x"][idx].iloc[i], df["y"][idx].iloc[i]),
                    fontsize=8,
                    alpha=0.7,
                    color="w",
                    xytext=(5, 0),
                    textcoords="offset points",
                )

    ax.legend(title="Clusters")
    ax.set_title("Cluster Visualization", fontsize=16, fontweight="bold")
    ax.set_xlabel("Dimension 1")
    ax.set_ylabel("Dimension 2")
    plt.grid(False)
    plt.tight_layout()
    plt.savefig(f"data/{figname}.png")


def process_embeddings(filepath, figname, annotate=True):
    embeddings_dict = load_embeddings(filepath)
    embedding_list = [v["embedding"] for v in embeddings_dict.values()]
    file_names = list(embeddings_dict.keys())
    embedding_matrix = np.array(embedding_list)
    labels = perform_clustering(embedding_matrix)
    reduced_embeddings = reduce_dimensionality(embedding_matrix)
    plot_clusters(reduced_embeddings, labels, file_names, figname, annotate)


process_embeddings("data/embeddings.pkl", figname="cluster_plot")
process_embeddings("data/hf_embeddings.pkl", figname="hf_cluster_plot", annotate=False)
