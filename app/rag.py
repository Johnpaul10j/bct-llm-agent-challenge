# app/core/rag.py
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

# Initialize embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Sample Nigerian-themed reviews
sample_docs = [
    Document(page_content="I bought this phone last month. Battery lasts very long even when watching Premier League matches all day. Camera is sharp for taking pictures at parties.", metadata={"domain": "tech"}),
    Document(page_content="The jollof rice here is excellent, very well seasoned just like home. The service is also fast.", metadata={"domain": "food"}),
    Document(page_content="This Ankara outfit is beautiful. The material is high quality and the design is modern yet traditional.", metadata={"domain": "fashion"}),
    Document(page_content="This movie was very entertaining. The story was strong and the acting was top notch like most Nollywood films.", metadata={"domain": "entertainment"}),
]

vectorstore = FAISS.from_documents(sample_docs, embeddings)

def get_rag_context(query: str, k: int = 3):
    """Retrieve relevant context for RAG"""
    docs = vectorstore.similarity_search(query, k=k)
    return "\n\n".join([doc.page_content for doc in docs])