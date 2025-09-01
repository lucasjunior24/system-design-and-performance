from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain.prompts import PromptTemplate

from pydantic import Field, BaseModel
from langchain_core.output_parsers import JsonOutputParser

# Initialize in-memory chat history

from langchain.chat_models import init_chat_model

seu_personagem = "Assistente"


class Tiros(BaseModel):
    pessoa_vai_levar_os_tiros: str = Field(
        "user_id da pessoa que vai receber seus os tiros"
    )
    total_tiros: str = Field("quantidade de tiros que você vai dar nessa pessoa")


from dotenv import load_dotenv


jogador_one = {
    "user_id": "1",
    "identidade": "Xefire",
    "tiros": {"total_tiros": "2", "user_id_que_levou_tiro": "2"},
}
jogador_two = {
    "user_id": "2",
    "identidade": "",
    "tiros": {"total_tiros": "2", "user_id_que_levou_tiro": "1"},
}
jogador_three = {
    "user_id": "3",
    "identidade": "",
    "tiros": {"total_tiros": "2", "user_id_que_levou_tiro": "1"},
}
jogador_four = {
    "user_id": "4",
    "identidade": "assistente",
}
# mensagens = [jogador_one, jogador_two, jogador_three]


# memory.chat_memory.aadd_messages(jogador_one)
# memory.chat_memory.aadd_messages(jogador_two)
# memory.chat_memory.aadd_messages(jogador_three)
load_dotenv()

parseador = JsonOutputParser(pydantic_object=Tiros)


llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

templete = """Voce é um jogador do Jogo Bang Dice Game, seu user_id é o 4 e sua identidade é de Assistente, voce acabou de rolar os dados e tirou 3 tiros de 1 distancia, em um dos seu lados está o Xerife e no outro lado um pessoa que ainda não jogou, responda apenas dizendo em quem você vai atirar e o total de tiros nessa pessoa.
    {formatacao_de_saida}
    """
templete_jogada = PromptTemplate(
    template="""Voce é um jogador do Jogo Bang Dice Game, seu user_id é o 4 e sua identidade é de Assistente, voce acabou de rolar os dados e tirou 3 tiros de 1 distancia, em um dos seu lados está o Xerife e no outro lado um pessoa que ainda não jogou, responda apenas dizendo em quem você vai atirar e o total de tiros nessa pessoa.
    {formatacao_de_saida}
    """,
    input_variables=["suas_informaces"],
    partial_variables={"formatacao_de_saida": parseador.get_format_instructions()},
)


# conversation = ConversationChain(
#     llm=llm,
#     verbose=True,
#     memory=memory,
# )


from langchain_core.output_parsers import JsonOutputParser


core_runnable = templete_jogada | llm | parseador


from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

# In-memory history for demonstration

# memory.chat_memory.aadd_messages(jogador_one)
# memory.chat_memory.aadd_messages(jogador_two)
# memory.chat_memory.aadd_messages(jogador_three)
store = {}
store["1"] = jogador_one
store["2"] = jogador_two
store["3"] = jogador_three
memory = ChatMessageHistory()
memory.chat_memory.aadd_messages(jogador_one)
memory.chat_memory.aadd_messages(jogador_two)
memory.chat_memory.aadd_messages(jogador_three)


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


with_history = RunnableWithMessageHistory(
    core_runnable,
    memory,
    input_messages_key="input",  # Key for input messages in the runnable
    history_messages_key="history",  # Key for historical messages in the runnable
)
config = {"configurable": {"session_id": "4"}}
result = with_history.invoke({"input": seu_personagem}, config=config)
print(result)
