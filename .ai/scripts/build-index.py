import os
import glob
import chromadb
from chromadb.utils import embedding_functions

# Configuration
VAULT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CHROMA_DB_PATH = os.path.join(os.getcwd(), ".ai", "vector_db")
COLLECTION_NAME = "gracia_vault"
EMBEDDING_MODEL = "nomic-embed-text"

def build_index():
    print(f"Initializing ChromaDB at {CHROMA_DB_PATH}...")
    client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    
    # Using Ollama embedding function
    ollama_ef = embedding_functions.OllamaEmbeddingFunction(
        model_name=EMBEDDING_MODEL,
        url="http://localhost:11434/api/embeddings",
    )
    
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=ollama_ef
    )

    print(f"Scanning for Markdown files in {VAULT_PATH}...")
    # Recursive globbing for .md files
    md_files = glob.glob(os.path.join(VAULT_PATH, "**", "*.md"), recursive=True)
    
    print(f"Found {len(md_files)} files. Starting indexing...")
    
    for file_path in md_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if not content.strip():
                continue
                
            # Use relative path as ID for consistency
            rel_path = os.path.relpath(file_path, VAULT_PATH)
            
            # Upsert into collection
            collection.upsert(
                documents=[content],
                metadatas=[{"path": file_path, "filename": os.path.basename(file_path)}],
                ids=[rel_path]
            )
            print(f"Indexed: {rel_path}")
        except Exception as e:
            print(f"Error indexing {file_path}: {e}")

    print("Indexing complete.")

if __name__ == "__main__":
    build_index()
