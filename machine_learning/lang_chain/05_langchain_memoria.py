from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory


from langchain.chat_models import init_chat_model


from dotenv import load_dotenv

mensagens = [
    "Quero visitar um lugar no Brasil famoso por suas praias e cultura. Pode me recomendar?",
    "Qual é o melhor período do ano para visitar em termos de clima?",
    "Quais tipos de atividades ao ar livre estão disponíveis?",
    "Alguma sugestão de acomodação eco-friendly por lá?",
    "Cite outras 20 cidades com características semelhantes às que descrevemos até agora. Rankeie por mais interessante, incluindo no meio ai a que você já sugeriu.",
    "Na primeira cidade que você sugeriu lá atrás, quero saber 5 restaurantes para visitar. Responda somente o nome da cidade e o nome dos restaurantes.",
]


load_dotenv()
llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")


memory = ConversationBufferMemory()

conversation = ConversationChain(llm=llm, verbose=True, memory=memory)


for mensagem in mensagens:
    resposta = conversation.predict(input=mensagem)
    print(resposta)
