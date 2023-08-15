import numpy as np
import pickle
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd


def load_embeddings(filepath):
    return pickle.load(open(filepath, "rb"))


def perform_clustering(embeddings, n_clusters=5):
    kmeans = KMeans(n_clusters=n_clusters)
    return kmeans.fit_predict(embeddings)


def reduce_dimensionality(embeddings):
    tsne = TSNE(n_components=2, random_state=42)
    return tsne.fit_transform(embeddings)


def plot_clusters(reduced_embeddings, labels, filenames, n_clusters):
    df = pd.DataFrame(reduced_embeddings, columns=['Dimension 1', 'Dimension 2'])
    df['Cluster'] = labels

    fig = px.scatter(df, x='Dimension 1', y='Dimension 2', color='Cluster',
                     title='Clusters of Python Files in Embedding Space',
                     template='plotly_dark')

    fig.show()


if __name__ == "__main__":
    embeddings_dict = load_embeddings("data/embeddings.pkl")
    embedding_list = [v["embedding"] for v in embeddings_dict.values()]
    file_names = list(embeddings_dict.keys())
    embedding_matrix = np.array(embedding_list)

    labels = perform_clustering(embedding_matrix)
    reduced_embeddings = reduce_dimensionality(embedding_matrix)
    plot_clusters(reduced_embeddings, labels, file_names, n_clusters=5)
