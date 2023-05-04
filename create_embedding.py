from langchain.document_loaders import UnstructuredEPubLoader
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

load_dotenv()

def main():
    # Can use other loaders here https://python.langchain.com/en/latest/modules/indexes/document_loaders.html
    loader = UnstructuredEPubLoader("vol01.epub", mode="elements")
    data = loader.load()
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(data)
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(documents=docs, embedding=embeddings, persist_directory="db")
    db.persist()

if __name__ == "__main__":
    main()