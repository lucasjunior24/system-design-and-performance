import os
from langchain.chat_models import init_chat_model
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"


modelo_do_prompt = PromptTemplate.from_template(
    "Crie um roteiro de viagem de {dias} dias, para uma família com {criancas} crianças, que gostam de {atividade}."
)

prompt = modelo_do_prompt.format(
    dias=numero_de_dias, criancas=numero_de_criancas, atividade=atividade
)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# exemplo one
model = init_chat_model("llama3-8b-8192", model_provider="groq")

# exemplo two
response = model.invoke(prompt)
print(response.content)
