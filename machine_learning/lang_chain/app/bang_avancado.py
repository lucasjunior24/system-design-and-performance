seu_personagem = "Assistente"


from langchain.prompts import PromptTemplate

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


from pydantic import Field, BaseModel
from langchain_core.output_parsers import JsonOutputParser


class Tiros(BaseModel):
    pessoa_vai_levar_os_tiros: str = Field("pessoa que vai receber seus os tiros")
    total_tiros: str = Field("quantidade de tiros que você vai dar nessa pessoa")


class TirosDistancias(BaseModel):
    distancias: str = Field(
        "distancia dos tiros podem ser de 1 ou 2, e quem estiver nessa distancia, vai tomar tiros de vc"
    )
    tiros: str = Field("quantidade de tiros que você vai dar nessa pessoa")


class SuasInformacoes(BaseModel):
    seu_personagem: str = Field(
        "a identidade do seu personagem, voce pode ser o Xerife, o Assistente, o renegado ou um fora da lei"
    )
    seus_dados: list[TirosDistancias] = Field(
        "Voce rolou os dados e neles veio os tiros, voce só pode atirar em quem tiver perto de voce",
    )


tiro_distancia = TirosDistancias(distancias="1", tiros="3")
suas_informaces = SuasInformacoes(
    seu_personagem=seu_personagem, seus_dados=[tiro_distancia]
)


# set_debug(True)
load_dotenv()

parseador = JsonOutputParser(pydantic_object=Tiros)
suas_informaces_parse = JsonOutputParser(pydantic_object=SuasInformacoes)

llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")
templete_jogada = PromptTemplate(
    template="""Voce é um jogador do Jogo Bang Dice Game, seu personagem é o {seu_personagem}, voce acabou de rolar os dados e tirou 3 tiros de 1 distancia, em um dos seu lados está o Xerife e no outro lado um pessoa que ainda não jogou, responda apenas dizendo em quem você vai atirar e o total de tiros nessa pessoa.
    {formatacao_de_saida}
    """,
    input_variables=["suas_informaces"],
    partial_variables={"formatacao_de_saida": parseador.get_format_instructions()},
)


cadeia_jogada = templete_jogada | llm | parseador


data = cadeia_jogada.invoke({"suas_informaces": suas_informaces})
print(data)
