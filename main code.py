import pandas as pd
fashion_file = pd.read_excel("C:\\Users\\ashii\\OneDrive\\Documents\\Fashion Dataset.xlsx")
print(fashion_file.head())
print(fashion_file.columns)
print(list(fashion_file.columns))
print(type(fashion_file["price"]))
fashion_file['combined_text']= fashion_file["name"] + " "+ fashion_file["price"] + " "+ fashion_file["colour"]+" " + fashion_file["brand"]+ fashion_file["description"]
print(fashion_file['combined_text'])