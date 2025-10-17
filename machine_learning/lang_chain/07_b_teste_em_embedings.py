import os

from langchain.prompts import ChatPromptTemplate

# Initialize the embedding model (e.g., OpenAIEmbeddings)
# Ensure OPENAI_API_KEY is set in your environment
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama


from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,  # Optional: Controls randomness of output
    max_retries=2,  # Optional: Max number of retries for requests
    api_key=groq_api_key,  # Optional: If not set as environment variable
)
print(groq_api_key)


# llm = ChatGroq(groq_api_key=groq_api_key, model="llama-3.3-70b-versatile")
# llm = ChatGroq(groq_api_key=groq_api_key, model="Llama3-8b-8192")
# llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")


# embeddings = OpenAIEmbeddings()
modelo_cidade = ChatPromptTemplate.from_template(
    "Sugira uma cidade dado meu interesse por {interesse}"
)
cadeia = modelo_cidade | llm
# Generate embeddings for a piece of text
# data = cadeia.invoke("praias")
# print(data.content)

from langchain_openai import OpenAIEmbeddings

# Ensure OPENAI_API_KEY is set if using OpenAI embeddings
# os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
print(embeddings.embed_query("Me diga algo"))
