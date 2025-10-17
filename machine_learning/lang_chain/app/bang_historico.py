seu_personagem = "Assistente"


from langchain.prompts import PromptTemplate

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


from pydantic import Field, BaseModel
from langchain_core.output_parsers import JsonOutputParser


class Tiros(BaseModel):
    user_name: str = Field("Nome de quem vai receber os tiros")
    shoots: str = Field("Quantidade de tiros que você vai dar nesse jogador")


load_dotenv()
initial_message = "Voçê é um agente especialista em no Jogo Bang Dice Game. A partida vai começar agora e tem 5 jogadores, sendo eles: Pedro que é o Xerife, seguindo a ordem vem o Lucas, Murilo, Aragão e o Roberto. "


def format_message_execution(
    personagem: str,
    user_name: str,
    dice: str,
    dices_total: str,
    playes_one: list[str],
    playes_two: list[str],
):
    m = "Voçê acabou de rolar os dados e tirou "
    if dice == "1":
        m += f"{dices_total} tiros de {dice} distancia, e pode atirar ou no {playes_one[0]} ou no {playes_one[1]}."
        if dice == "2":
            m = (
                +f"e {dice} tiros de {dice} distancia, e pode atirar ao no {playes_two[0]} ou no {playes_two[1]}"
            )
    elif dice == "2":
        m += f"{dice} tiros de {dice} distancia, e pode atirar ao no {playes_two[0]} ou no {playes_two[1]}"

    message = f"Voce é o jogador {user_name} do Jogo Bang Dice Game, seu personagem é o {personagem}. {m} Responda apenas dizendo em quem vai ser o tiro e o total de tiros."

    return message


message_tese = format_message_execution(
    dice="1",
    dices_total=str(3),
    personagem="Assistente",
    playes_one=["Pedro", "Aragão"],
    user_name="Roberto",
    playes_two=[],
)

messagemsss = initial_message + message_tese
print(messagemsss)

parseador = JsonOutputParser(pydantic_object=Tiros)

templete_jogada = PromptTemplate(
    template="""{messagemsss}.
    {formatacao_de_saida}
    """,
    # metadata={{"role": "system", "content": initial_message}},
    partial_variables={"formatacao_de_saida": parseador.get_format_instructions()},
)


llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

cadeia_jogada = templete_jogada | llm | parseador


data = cadeia_jogada.invoke("")
print(data)
