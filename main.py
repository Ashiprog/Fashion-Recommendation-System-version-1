import os
import pickle

import pandas as pda
from openai import OpenAI
from dotenv import load_dotenv
import numpy
import faiss

load_dotenv()
client = OpenAI(api_key=os.environ["My_API_Key"])
doc_1 = pda.read_excel("C:\\Users\\ashii\\OneDrive\\Documents\\Fashion Dataset.xlsx")

doc= doc_1.head(500)
doc["combined_name"]= doc["p_id"].astype(str) +" " + doc["name"].astype(str) +" "+ doc["price"].astype(str)+ " "+ doc["colour"].astype(str)+" "+ doc["brand"].astype(str)+ "" + doc["description"].astype(str)+ doc["name"].astype(str)


class Hybrid():
    def create_embedding(self,input_text):
        embed= client.embeddings.create(model="text-embedding-3-small",input=input_text)
        only_embed = embed.data[0].embedding
        return only_embed
    def Fashion_HNSW(self,tmwuw_embedding,all_dress_embedding):
        numpy_all_dress_embeddings = numpy.array(all_dress_embedding).astype("float32")
        dimension = len(all_dress_embedding[0])
        number_of_neighbours = 3
        index = faiss.IndexHNSWFlat(dimension,number_of_neighbours)
        index.add(numpy_all_dress_embeddings)
        numpy_tmwuw = numpy.array(tmwuw_embedding).astype("float32")
        distance,indices = index.search(numpy_tmwuw.reshape(1,-1),5)
        return indices[0]


if not os.path.exists("all_dress_embeddings_file"):
    shop=Hybrid()
    all_dress_embeddings=[]
    doc_combined_no_nan= doc["combined_name"].fillna("")
    for dress_combine in doc_combined_no_nan:
        e = shop.create_embedding(dress_combine)
        all_dress_embeddings.append(e)
    with open("all_dress_embeddings_file","wb") as f:
        pickle.dump(all_dress_embeddings,f)
else:
    with open("all_dress_embeddings_file", "rb") as f:
        all_dress_embeddings = pickle.load(f)


