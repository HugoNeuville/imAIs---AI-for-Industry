#rag_assistant.py

from pathlib import Path
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
import os

OPENAI_API_KEY = "OPENAI_API_KEY"

docs_path = Path(
    r"C:\Users\ugolu\OneDrive\Bureau\imAIs\Scripts\maintenance_docs"
)

print("Folder exists:", docs_path.exists())
print("TXT files:", list(docs_path.glob("*.txt")))


documents = []

for file_path in docs_path.glob("*.txt"):
    text = file_path.read_text(encoding="utf-8")
    documents.append(
        Document(
            page_content=text,
            metadata={"source": file_path.name}
        )
    )

print("Documents loaded:", len(documents))

for doc in documents:
    print(doc.metadata["source"], len(doc.page_content))

text_splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

texts = text_splitter.split_documents(documents)

print("Chunks created:", len(texts))

embeddings = OpenAIEmbeddings(
    openai_api_key = OPENAI_API_KEY
)

vector_db = Chroma.from_documents(
    texts,
    embeddings,
    persist_directory="chroma_db"
)

llm = ChatOpenAI(
    temperature=0,
    openai_api_key = OPENAI_API_KEY
)


def ask_maintenance_assistant(question, chat_history=None):
    docs = vector_db.similarity_search(question, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])

    sources = list(set([doc.metadata.get("source", "unknown") for doc in docs]))

    history_text = ""
    if chat_history:
        for message in chat_history[-6:]:
            history_text += f"{message['role']}: {message['content']}\n"

    prompt = f"""
You are an industrial maintenance assistant.

Use the maintenance documentation and conversation history to answer the operator question.
If the documentation does not contain enough information, say so.

Maintenance documentation:
{context}

Conversation history:
{history_text}

Operator question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content, sources

question = "What should I do if vibration is increasing?"
response = ask_maintenance_assistant(question)
print(response)