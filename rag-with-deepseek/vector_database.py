from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

# Constants data

pdfs_directory = "/pdfs"
file_path = "eng.pdf"
ollama_model_name = "deepseek-r1"


# Step : Upload & Load row PDF(s)

def upload_pdf(file):
    with open(pdfs_directory + file.name, 'wb') as f:
        f.write(file.getbuffer())


def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()
    return documents
  
documents = load_pdf(file_path)
# print(len(documents))

# Step : Create chunks

def create_chunks(documents):
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        add_start_index = True
    )
    text_chunks = text_splitter.split_documents(documents)
    
    return text_chunks

text_chunks = create_chunks(documents)
# print("Chunks count : ", len(text_chunks))

# Step : Setup Embeddings Model (Use DeepSeek R1 with Ollama)

def get_embedding_modal(ollama_model_name):
    embeddings = OllamaEmbeddings(model=ollama_model_name)
    return embeddings


# Step : Index documents Store embeddings in FAISS (vector store)

FAISS_DB_PATH = "vectorstore/db_faiss"
faiss_db = FAISS.from_documents(text_chunks, get_embedding_modal(ollama_model_name))
faiss_db.save_local(FAISS_DB_PATH)