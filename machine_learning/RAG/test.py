# Importa o módulo para manipulação de variáveis de ambiente
import os

# Loader responsável por ler arquivos PDF
from langchain_community.document_loaders import PyPDFLoader
# Responsável por dividir textos grandes em chunks menores
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Classe que transforma texto em embeddings vetoriais
# from langchain.embeddings import OpenAIEmbeddings

# Banco vetorial para armazenamento e busca semântica
# from langchain.vectorstores import Chroma

# Modelo de linguagem conversacional
# from langchain.chat_models import ChatOpenAI

# # Cadeia pronta de Perguntas e Respostas com RAG
# from langchain.chains import RetrievalQA

# Lista com os caminhos dos arquivos PDF das bulas
caminhos_bulas = [
    "dipirona.pdf",
    "paracetamol.pdf"
]
print('caminhos_bulas: ')
# Lista que armazenará todos os documentos carregados
documentos = []

# Percorre cada bula
for caminho in caminhos_bulas:
    
    # Cria o loader de PDF
    loader = PyPDFLoader(caminho)

    # Carrega o conteúdo do PDF
    docs = loader.load()
    
    # Adiciona o nome do medicamento como metadado
    for doc in docs:
        doc.metadata["medicamento"] = caminho.split('/')[0].replace(".pdf", "")
        
    # Adiciona os documentos à lista principal
    documentos.extend(docs)
    
# Exibe a quantidade total de páginas carregadas
print(len(documentos))


# Cria o objeto responsável pelo chunking
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=600,       # Tamanho máximo de cada chunk
    chunk_overlap=150     # Sobreposição entre chunks
)

# Divide os documentos em chunks
chunks = text_splitter.split_documents(documentos)

# Quantidade total de chunks gerados

print(len(chunks))


# Percorre cada chunk para classificar semanticamente seu conteúdo
for chunk in chunks:

    # Normaliza o texto para facilitar as verificações
    texto = chunk.page_content.lower()

    # Identificação do medicamento
    if "identificação do medicamento" in texto or "composição" in texto:
        chunk.metadata["categoria"] = "identificacao"

    # Indicações terapêuticas
    elif "indicação" in texto or "para que este medicamento é indicado" in texto:
        chunk.metadata["categoria"] = "indicacao"

    # Funcionamento do medicamento
    elif "como este medicamento funciona" in texto or "ação" in texto:
        chunk.metadata["categoria"] = "como_funciona"

    # Contraindicações
    elif "contraindicação" in texto or "quando não devo usar" in texto:
        chunk.metadata["categoria"] = "contraindicacao"

    # Advertências e precauções
    elif "advertência" in texto or "precaução" in texto or "o que devo saber antes de usar" in texto:
        chunk.metadata["categoria"] = "advertencias_precaucoes"

    # Interações medicamentosas
    elif "interação" in texto or "interações medicamentosas" in texto:
        chunk.metadata["categoria"] = "interacoes"

    # Posologia e modo de uso
    elif "dose" in texto or "posologia" in texto or "como devo usar" in texto:
        chunk.metadata["categoria"] = "posologia_modo_uso"

    # Reações adversas
    elif "reações adversas" in texto or "quais os males" in texto:
        chunk.metadata["categoria"] = "reacoes_adversas"

    # Armazenamento
    elif "onde, como e por quanto tempo posso guardar" in texto or "armazenar" in texto:
        chunk.metadata["categoria"] = "armazenamento"

    # Superdosagem
    elif "quantidade maior do que a indicada" in texto or "superdosagem" in texto:
        chunk.metadata["categoria"] = "superdosagem"

    # Conteúdo geral / administrativo
    else:
        chunk.metadata["categoria"] = "geral"



import random

# Seleciona dois chunks aleatórios
chunks_aleatorios = random.sample(chunks, 2)

# Imprime os metadados e um trecho do conteúdo
for i, chunk in enumerate(chunks_aleatorios, start=1):
    print(f"\n--- Chunk Aleatório {i} ---")
    print(f"Metadados: {chunk.metadata}")
    print("\nConteúdo (início):")
    print(chunk.page_content[:300])



# Embeddings (forma correta e atual)
# from langchain_openai import OpenAIEmbeddings

# Vector Store
from langchain_community.vectorstores import Chroma

# Inicializa o modelo de embeddings (forma atual)
# embeddings = OpenAIEmbeddings(
#     model="text-embedding-3-small" # opcional, mas recomendado
# )
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
embedding_model_name = "sentence-transformers/all-MiniLM-L6-v2"


embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)

# Cria o banco vetorial com os chunks
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_bulas"
)