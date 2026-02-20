# Embeddings (forma correta e atual)
from langchain_openai import OpenAIEmbeddings

# Vector Store
from langchain_community.vectorstores import Chroma

# Cria o retriever para busca semântica
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 4} # Número de chunks retornados
)

# Inicializa o modelo de linguagem
llm = ChatOpenAI(
    model="gpt-4o-mini",
)

# Cria a cadeia RAG
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)