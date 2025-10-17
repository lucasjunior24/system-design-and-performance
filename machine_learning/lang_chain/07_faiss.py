from langchain_core.documents import Document

jogador_one = {
    "user_id": "1",
    "identidade": "Xefire",
    "tiros_executados": {"total_tiros": "2", "user_id_que_levou_tiro": "2"},
}
jogador_two = {
    "user_id": "2",
    "identidade": "",
    "tiros_executados": {"total_tiros": "2", "user_id_que_levou_tiro": "1"},
}
jogador_three = {
    "user_id": "3",
    "identidade": "",
    "tiros_executados": {"total_tiros": "2", "user_id_que_levou_tiro": "1"},
}
jogador_four = {
    "user_id": "4",
    "identidade": "assistente",
}
page_one = f"user_id: {jogador_one["user_id"]}. Identidade: {jogador_one["identidade"]}. Total de tiros executados por esse usuario: {jogador_one["tiros_executados"]["total_tiros"]}. user_id de quem levou os tiros: {jogador_one["tiros_executados"]["user_id_que_levou_tiro"]}"
page_two = f"user_id: {jogador_two["user_id"]}. Identidade: {jogador_two["identidade"]}. Total de tiros executados por esse usuario: {jogador_two["tiros_executados"]["total_tiros"]}. user_id de quem levou os tiros: {jogador_two["tiros_executados"]["user_id_que_levou_tiro"]}"
page_three = f"user_id: {jogador_three["user_id"]}. Identidade: {jogador_three["identidade"]}. Total de tiros executados por esse usuario: {jogador_three["tiros_executados"]["total_tiros"]}. user_id de quem levou os tiros: {jogador_three["tiros_executados"]["user_id_que_levou_tiro"]}"
page_four = f"user_id: {jogador_four["user_id"]}. Identidade: {jogador_four["identidade"]}. Total de tiros executados por esse usuario: {jogador_four["tiros_executados"]["total_tiros"]}. user_id de quem levou os tiros: {jogador_four["tiros_executados"]["user_id_que_levou_tiro"]}"

document_one = Document(
    page_content=page_one,
    metadata={
        "source": "users",
        "user_id": jogador_one["user_id"],
        "identidade": jogador_one["identidade"],
        "tiros_executados": jogador_one["tiros_executados"],
    },
)
document_two = Document(
    page_content=page_two,
    metadata={
        "source": "users",
        "user_id": jogador_two["user_id"],
        "identidade": jogador_two["identidade"],
        "tiros_executados": jogador_two["tiros_executados"],
    },
)
document_three = Document(
    page_content=page_three,
    metadata={
        "source": "users",
        "user_id": jogador_three["user_id"],
        "identidade": jogador_three["identidade"],
        "tiros_executados": jogador_three["tiros_executados"],
    },
)

document_four = Document(
    page_content=page_four,
    metadata={
        "source": "users",
        "user_id": jogador_four["user_id"],
        "identidade": jogador_four["identidade"],
        "tiros_executados": jogador_four["tiros_executados"],
    },
)
list_docs = [document_one, document_two, document_three, document_four]



from langchain_community.vectorstores import FAISS
import faiss

d = 768
index_hnsw = faiss.IndexHNSWFlat(d, 32)
faiss_db = FAISS.from_documents(list_docs)


pergunta = "quem atirou no Xerife?"
resultados = faiss_db.similarity_search(pergunta, k=2)

print(f"\n Pergunta: {pergunta}")
print(f"\n Documentos mais relevantes (FAISS):")
for doc in resultados:
    print(f"- {doc.page_content}")
    print(f"(Metadados: {doc.metadata})")