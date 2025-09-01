
from langchain.prompts import ChatPromptTemplate, PromptTemplate

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.globals import set_debug
from langchain_core.pydantic_v1 import Field, BaseModel
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser

class Destino(BaseModel):
    motivo = Field("motivo pelo qual é interessante visitar")
    cidade = Field('cidade a visitar')

set_debug(True)
load_dotenv()

parseador = JsonOutputParser(pydantic_object=Destino)

modelo_cidade = PromptTemplate(
    template="""Sugira uma cidade dado interesse por {interesse}.
    {formatacao_de_saida}
    """,
    input_variables=["interesse"],
    partial_variables={"formatacao_de_saida": parseador.get_format_instructions()},
)

modelo_restaurantes = ChatPromptTemplate.from_template(
    "Sugira restaurantes populares entre locais em {cidade}"
)

modelo_cultural = ChatPromptTemplate.from_template(
    "Sugira atividades e locais culturais em {cidade}"
)
llm = init_chat_model("llama3-8b-8192", model_provider="groq")



parte1 = modelo_cidade | llm | parseador
parte2 = modelo_restaurantes | llm | StrOutputParser()
parte3 = modelo_cultural | llm | StrOutputParser()

cadeia = (parte1, parte2, parte3)
data = cadeia.invoke('praias')
print(data['output'])
