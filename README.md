# LeetCode Progress Tracker & Analysis


This repository is designed to track and showcase your progress on LeetCode while also providing a unique data analysis on the problems and solutions. It uses OpenAI to generate embeddings for Python code and visualizes them using PCA. 

## 🚀 Why Use This Repo?

If you're a LeetCode enthusiast who wants to track your progress in a visually appealing way, this repo is for you! It not only helps you keep track of the problems you've solved but also provides an interesting data analysis of your solutions. 

### Progress: 37/150 Problems Solved
![25%](https://progress-bar.dev/25)

## 📂 Repo Structure

```
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
    ├── fizz_buzz.py
    └── ...
```

## 📝 Requirements

- openai
- scikit-learn
- matplotlib
- seaborn
- adjustText

Install the required packages using `pip install -r requirements.txt`.

## 📖 Usage

Here is an example of how to use the `code_to_embeddings.py` script:

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

This script extracts the text from Python files in the specified folder, gets the embeddings for each file using OpenAI, and saves the embeddings to a pickle file.

## 🎉 Conclusion

This repo is a fun and interactive way to track your LeetCode progress and analyze your solutions. Happy coding!