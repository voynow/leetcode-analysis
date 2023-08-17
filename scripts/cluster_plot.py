import logging
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE

plt.style.use("dark_background")

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Clustering:
    def __init__(self, filepath):
        self.embeddings_dict = self.load_embeddings(filepath)
        self.embedding_matrix = np.array([v["embedding"] for v in self.embeddings_dict.values()])
        self.labels = self.perform_clustering(self.embedding_matrix)
        self.reduced_embeddings = self.reduce_dimensionality(self.embedding_matrix)

    @staticmethod
    def load_embeddings(filepath):
        logging.info(f"Loading embeddings from {filepath}")
        return pickle.load(open(filepath, "rb"))

    @staticmethod
    def perform_clustering(embeddings, n_clusters=5):
        logging.info("Performing KMeans clustering")
        kmeans = KMeans(n_clusters=n_clusters, n_init=10)
        return kmeans.fit_predict(embeddings)

    @staticmethod
    def reduce_dimensionality(embeddings):
        logging.info("Reducing dimensionality using t-SNE")
        tsne = TSNE(n_components=2, random_state=42)
        return tsne.fit_transform(embeddings)

class Plotting:
    def __init__(self, cluster):
        self.cluster = cluster
        self.file_names = list(cluster.embeddings_dict.keys())

    def plot_clusters(self, figname, annotate=True, color_palette="colorblind"):
        logging.info(f"Plotting clusters to {figname}.png")
        self._plot(self.cluster.reduced_embeddings, self.cluster.labels, figname, annotate, color_palette)

    def plot_overlay_clusters(self, other_cluster, figname):
            logging.info(f"Plotting overlay clusters to {figname}.png")
            self._plot(self.cluster.reduced_embeddings, self.cluster.labels, figname, color="blue")
            self._plot(other_cluster.reduced_embeddings, other_cluster.labels, figname, legend_label="Master Clusters", color="red", append=True)

    def _plot(self, reduced_embeddings, labels, figname, annotate=True, color_palette="colorblind", append=False, legend_label=None, color=None):
        df = pd.DataFrame({
            "x": reduced_embeddings[:, 0],
            "y": reduced_embeddings[:, 1],
            "labels": labels,
        })

        # Define unique labels and color palette
        unique_labels = sorted(list(set(labels)))
        if color:
            colors = [color] * len(unique_labels)
        else:
            colors = sns.color_palette(color_palette, len(unique_labels))

        if append:
            fig, ax = plt.gcf(), plt.gca()
        else:
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
                label=legend_label if legend_label else f"Cluster {label}",
            )

            if annotate:
                for i, txt in enumerate(self.file_names):
                    ax.annotate(
                        txt,
                        (df["x"].iloc[i], df["y"].iloc[i]),
                        fontsize=8,
                        alpha=0.7,
                        color="w",
                        xytext=(5, 0),
                        textcoords="offset points",
                    )

        if not append:
            ax.legend(title="Clusters")
        else:
            handles, labels = ax.get_legend_handles_labels()
            ax.legend(handles=handles[:len(unique_labels)] + handles[len(unique_labels):], labels=[legend_label if legend_label else "My solutions", "Master Clusters"], title="Clusters")

        ax.set_title("Cluster Visualization", fontsize=16, fontweight="bold")
        ax.set_xlabel("Dimension 1")
        ax.set_ylabel("Dimension 2")
        plt.grid(False)
        plt.tight_layout()
        plt.savefig(f"plots/{figname}.png")


master_cluster = Clustering("data/hf_embeddings.pkl")
your_cluster = Clustering("data/embeddings.pkl")

master_plot = Plotting(master_cluster)
master_plot.plot_clusters("hf_cluster")

your_plot = Plotting(your_cluster)
your_plot.plot_clusters("cluster")

your_plot.plot_overlay_clusters(master_cluster, "overlay_cluster")
