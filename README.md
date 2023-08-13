# LeetCode Progress Tracker and Analysis

![GitHub stars](https://img.shields.io/github/stars/your_username/your_repo_name?style=social)
![PyPI](https://img.shields.io/pypi/v/your_package_name)

This repository is designed to track and showcase your progress on LeetCode while also providing a unique data analysis on the problems and solutions. It uses OpenAI's API to generate embeddings for Python code and visualizes these embeddings using PCA. 

## 🚀 Why Use This Repo?

If you are a LeetCode enthusiast and want to track your progress in a fun and interactive way, this repository is for you. It allows you to:

- Track your progress on LeetCode
- Analyze your solutions
- Visualize the embeddings of your Python code
- Understand the structure and style of your code

## 📂 Repo Structure

```bash
.
├── .gitignore
├── requirements.txt
├── scripts
│   ├── code_to_embeddings.py
│   └── embeddings_viz.py
└── solutions
    ├── add_two_numbers.py
    ├── best_time_to_buy_and_sell_stock.py
    ├── binary_tree_inorder_traversal.py
    ├── climbing_stairs.py
    ├── convert_sorted_array_to_height_balanced_bst.py
    ├── diameter_of_binary_tree.py
    ├── find_all_numbers_disappeared_in_an_array.py
    ├── find_the_index_of_the_first_occurance_in_a_string.py
    └── fizz_buzz.py
```

## 📝 Requirements

The `requirements.txt` file lists the Python libraries that your project depends on. You can install them using:

```bash
pip install -r requirements.txt
```

## 💻 Usage

Here is an example of how to use the `code_to_embeddings.py` script to generate embeddings for your Python code:

```python
from dotenv import load_dotenv
import openai
import os
import pickle

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

EMBEDDINGS_MODEL = "text-embedding-ada-002"

folder_path = 'solutions'
texts = extract_texts_from_folder(folder_path)
embeddings = get_embeddings(texts)
pickle.dump(embeddings, open('embeddings.pkl', 'wb'))
```

## 📈 Visualization

The `embeddings_viz.py` script uses PCA to reduce the dimensionality of the embeddings and visualizes them in a 2D scatter plot. Here is an example of how to use it:

```python
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

# Apply PCA for dimensionality reduction
logging.info('Applying PCA for dimensionality reduction...')
pca = PCA(n_components=2)
reduced_embeddings = pca.fit_transform(embeddings)

# Plot the 2D embeddings
logging.info('Plotting the 2D embeddings...')
plt.figure(figsize=(12, 10))
plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1], s=100)

# Export the plot to a file
plot_filename = 'data/embeddings_plot.png'
plt.savefig(plot_filename, format='png', dpi=300)
logging.info(f'Plot saved to {plot_filename}')
```

## 📚 Solutions

The `solutions` directory contains Python solutions to various LeetCode problems. Each solution is contained in a separate `.py` file. For example, the `add_two_numbers.py` file contains a solution to the "Add Two Numbers" problem on LeetCode.

## 📝 Note

Please replace `your_username`, `your_repo_name`, and `your_package_name` with your actual GitHub username, repository name, and package name respectively in the badges at the top of this README.