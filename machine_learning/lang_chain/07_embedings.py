from langchain.globals import set_debug
from langchain_openai import OpenAIEmbeddings
from langchain.memory import ConversationSummaryMemory
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter
import os
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import RetrievalQA

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()
llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")


carregador = TextLoader("GTB_gold_Nov23.txt", encoding="utf-8")
documentos = carregador.load()


quebrador = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
textos = quebrador.split_documents(documentos)
# print(textos)
from langchain_community.embeddings import LlamaCppEmbeddings

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(textos, embeddings)

qa_chain = RetrievalQA.from_chain_type(llm, retriever=db.as_retriever())

pergunta = "Como devo proceder caso tenha um item comprado roubado"
resultado = qa_chain.invoke({"query": pergunta})
print(resultado)
