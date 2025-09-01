seu_personagem = "Assistente"


from langchain.prompts import PromptTemplate

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


from pydantic import Field, BaseModel
from langchain_core.output_parsers import JsonOutputParser


class Tiros(BaseModel):
    pessoa_vai_levar_os_tiros: str = Field("pessoa que vai receber seus os tiros")
    total_tiros: str = Field("quantidade de tiros que você vai dar nessa pessoa")


load_dotenv()

parseador = JsonOutputParser(pydantic_object=Tiros)

templete_jogada = PromptTemplate(
    template="""Voce é um jogador do Jogo Bang Dice Game, seu personagem é o {seu_personagem}, voce acabou de rolar os dados e tirou 3 tiros de 1 distancia, em um dos seu lados está o Xerife e no outro lado um pessoa que ainda não jogou, responda apenas dizendo em quem você vai atirar e o total de tiros nessa pessoa.
    {formatacao_de_saida}
    """,
    input_variables=["seu_personagem"],
    partial_variables={"formatacao_de_saida": parseador.get_format_instructions()},
)


llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

cadeia_jogada = templete_jogada | llm | parseador


data = cadeia_jogada.invoke(seu_personagem)
print(data)
