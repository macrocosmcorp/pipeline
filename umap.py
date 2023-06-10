from nomic import atlas
import numpy as np
import pickle


def load_embedding(output_path):
    with open(output_path, 'rb') as f:
        return pickle.load(f)


output_path = './embeddings/ill_opinions.pkl'
data = load_embedding(output_path)
embeddings = [d[1] for d in data]
embeddings = np.array(embeddings)

project = atlas.map_embeddings(embeddings=embeddings)