# Fashion-Recommendation-System-with-OpenAI

A semantic fashion recommendation system that understands the meaning of your search, not just keywords. Built with OpenAI embeddings, FAISS vector search, and a Streamlit UI. This is version 1 of the project with only 5000 projects.
## What It Does
Traditional fashion search returns results based on exact keyword matches. This system uses semantic search — so searching "shiny festive outfit" finds sequinned and embroidered kurtas, even if those exact words aren't in the product name.
## How It Works
1. Product descriptions are converted into embeddings using OpenAI's text-embedding-3-small model
2. Embeddings are stored in a FAISS HNSW index for fast similarity search
3. When you search, your query is embedded and compared against all products
4. The 5 most semantically similar products are returned with images and prices

## Tech Stack
- OpenAI — text embeddings
- FAISS — fast vector similarity search with HNSW index
- Streamlit — web UI
- Pandas — data handling
- Pickle — embedding persistence

## Setup
1. Clone the repository
2. Install dependencies: pip install openai faiss-cpu pandas openpyxl streamlit numpy python-dotenv
3. Download the Myntra Fashion Dataset from Kaggle and place it as Fashion Dataset.xlsx in the project root
4. Create a .env file with: My_API_Key=your_openai_api_key_here
5. Run main.py once to generate embeddings
6. Run: streamlit run app.py

## Known Limitations
- Colour matching is approximate — embeddings capture overall meaning, not precise colour
- Regional style terms may not always map to specific regional styles
- Dataset is kurta-focused — works best for Indian ethnic wear
- A fashion-specific embedding model would improve precision

## Built By
Ashrita R — transitioning into AI/ML engineering, building real projects to understand every component from first principles
