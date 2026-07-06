from main import Hybrid,doc,all_dress_embeddings
import streamlit as sl

shop = Hybrid()
sl.title("My Fashion Recommender")
query = sl.text_input("What kind of clothes are you looking for?")
if sl.button("Find"):
    if query:
        with sl.spinner("Finding options"):
            tmwuw_embed = shop.create_embedding(query)

            result = shop.Fashion_HNSW(tmwuw_embed,all_dress_embeddings)
            for i in result:
                sl.write(doc["name"].iloc[i])
                sl.write(f"Price: ₹{int(doc['price'].iloc[i])}")
                sl.image(doc["img"].iloc[i])
    else:
        sl.write("Please enter the kind of clothes you want recommended")






