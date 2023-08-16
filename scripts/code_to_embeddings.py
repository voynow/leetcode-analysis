from datasets import load_dataset
from dotenv import load_dotenv
import openai
import os
import pickle


load_dotenv()
if not os.environ.get("OPENAI_API_KEY"):
    raise ValueError("Set your OPENAI_API_KEY via export OPENAI_API_KEY=... or in a .env file")
openai.api_key = os.environ["OPENAI_API_KEY"]

EMBEDDINGS_MODEL = "text-embedding-ada-002"


def extract_texts_from_folder(folder_path):
    texts = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.py'):
            with open(os.path.join(folder_path, filename), 'r') as file:
                texts[filename] = file.read()
    return texts


def get_embeddings(texts):
    embeddings_data = {}
    for filename, text in texts.items():
        print(f'Getting embedding for {filename}')
        response = openai.Embedding.create(input=text, model=EMBEDDINGS_MODEL)
        embedding = response['data'][0]['embedding']
        embeddings_data[filename] = {
            'embedding': embedding, 'text': text
        }
    return embeddings_data


# my solutions
folder_path = 'solutions'
texts = extract_texts_from_folder(folder_path)
embeddings = get_embeddings(texts)
pickle.dump(embeddings, open('data/embeddings.pkl', 'wb'))

# huggingface solutions dataset
dataset = load_dataset('mhhmm/leetcode-solutions-python')
df = dataset['train'].to_pandas()
df['code_with_problem']
texts = df['code_with_problem'].to_dict()
embeddings_data = get_embeddings(texts)
pickle.dump(embeddings, open('data/hf_embeddings.pkl', 'wb'))