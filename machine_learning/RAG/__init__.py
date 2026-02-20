# Importa o módulo para manipulação de variáveis de ambiente
import os

# Loader responsável por ler arquivos PDF
from langchain.document_loaders import PyPDFLoader

# Responsável por dividir textos grandes em chunks menores
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Classe que transforma texto em embeddings vetoriais
from langchain.embeddings import OpenAIEmbeddings

# Banco vetorial para armazenamento e busca semântica
from langchain.vectorstores import Chroma

# Modelo de linguagem conversacional
from langchain.chat_models import ChatOpenAI

# Cadeia pronta de Perguntas e Respostas com RAG
from langchain.chains import RetrievalQA

# Lista com os caminhos dos arquivos PDF das bulas
caminhos_bulas = [
    "dipirona.pdf",
    "paracetamol.pdf"
]

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
len(documentos)