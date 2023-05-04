from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.callbacks import get_openai_callback

load_dotenv()

def create_store(llm):
    embeddings = OpenAIEmbeddings()
    db = Chroma(embedding_function=embeddings, persist_directory="db")
    return RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

def create_agent(retriever, llm):
    tools = [
                Tool(
                    name = "Volume 1 QA System",
                    func=retriever.run,
                    description="useful for when you need to answer questions about the first volume of In Another World With My Smartphone. Input should be a fully formed question.",
                )
            ]
    return initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False, return_intermediate_steps=True)

def main():
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    store = create_store(llm)
    agent = create_agent(store, llm)
    with get_openai_callback() as cb:
        agent({"input":"Who is Yae? Can you give further detail of her?"})
        print(cb)
    

if __name__ == "__main__":
    main()