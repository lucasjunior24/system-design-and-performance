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
    pessoa_vai_levar_os_tiros: str = Field("pessoa que vai receber seus os tiros")
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


memory = ConversationBufferMemory()

memory.chat_memory.aadd_messages(jogador_one)
memory.chat_memory.aadd_messages(jogador_two)
memory.chat_memory.aadd_messages(jogador_three)
load_dotenv()

parseador = JsonOutputParser(pydantic_object=Tiros)
llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

templete = """Voce é um jogador do Jogo Bang Dice Game, seu user_id é o 4 e sua identidade é de Assistente, voce acabou de rolar os dados e tirou 3 tiros de 1 distancia, em um dos seu lados está o Xerife e no outro lado um pessoa que ainda não jogou, responda apenas dizendo em quem você vai atirar e o total de tiros nessa pessoa.
    {formatacao_de_saida}
    """
templete_jogada = PromptTemplate(
    template=templete,
    # input_variables=["suas_informaces"],
    partial_variables={"formatacao_de_saida": parseador.get_format_instructions()},
)


conversation = ConversationChain(
    llm=llm,
    # verbose=True,
    memory=memory,
)

resposta = conversation.predict(input=templete)
print(resposta)
print()
print(memory.buffer)
