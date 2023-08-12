from dotenv import load_dotenv
import openai
import os

def extract_texts_from_folder(folder_path):
    texts = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.py'):
            with open(os.path.join(folder_path, filename), 'r') as file:
                texts[filename] = file.read()
    return texts

folder_path = 'solutions'
texts = extract_texts_from_folder(folder_path)

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.Embedding.create(
  input="Educative answers section is helpful",
  model="text-embedding-ada-002"
)

embeddings = response['data'][0]['embedding']