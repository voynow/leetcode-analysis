import logging
import pickle

import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA

plt.style.use('seaborn')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load embeddings
logging.info('Loading embeddings from file...')
with open('data/embeddings.pkl', 'rb') as file:
    embeddings_data = pickle.load(file)

# Extract embeddings and filenames
logging.info('Extracting embeddings and filenames...')
embeddings = [data['embedding'] for data in embeddings_data.values()]
filenames = [filename for filename in embeddings_data.keys()]

# Convert embeddings to NumPy array
embeddings = np.array(embeddings)

# Apply PCA for dimensionality reduction
logging.info('Applying PCA for dimensionality reduction...')
pca = PCA(n_components=2)
reduced_embeddings = pca.fit_transform(embeddings)

# Plot the 2D embeddings
logging.info('Plotting the 2D embeddings...')
plt.figure(figsize=(12, 10))
plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1], s=100)

# Annotate the points with filenames
for i, filename in enumerate(filenames):
    plt.annotate(filename, (reduced_embeddings[i, 0], reduced_embeddings[i, 1]))

plt.xlabel('Principal Component 1', fontsize=14)
plt.ylabel('Principal Component 2', fontsize=14)
plt.title('2D Visualization of Python File Embeddings', fontsize=16)

# Export the plot to a file
plot_filename = 'data/embeddings_plot.png'
plt.savefig(plot_filename, format='png', dpi=300)
logging.info(f'Plot saved to {plot_filename}')