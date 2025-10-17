from langchain.prompts import PromptTemplate

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


from pydantic import Field, BaseModel
from langchain_core.output_parsers import JsonOutputParser


class Destino(BaseModel):
    cidade: str = Field("cidade a visitar")
    estado: str = Field("estado a visitar")


# set_debug(True)
load_dotenv()

parseador = JsonOutputParser(pydantic_object=Destino)

modelo_cidade = PromptTemplate(
    template="""Sugira uma cidade e estado dado interesse por {interesse}.
    {formatacao_de_saida}
    """,
    input_variables=["interesse"],
    partial_variables={"formatacao_de_saida": parseador.get_format_instructions()},
)


llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

cadeia_cidade = modelo_cidade | llm | parseador


data = cadeia_cidade.invoke("praias")
print(data)
