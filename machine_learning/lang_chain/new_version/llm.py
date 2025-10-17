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


from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

# Define a new graph
workflow = StateGraph(state_schema=MessagesState)


# Define the function that calls the model
def call_model(state: MessagesState):
    response = llm.invoke(state["messages"])
    # Update message history with response:
    return {"messages": response}


print()

# Define the (single) node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)
config = {"configurable": {"thread_id": "abc123"}}
query = "Hi! I'm Bob."

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
# output["messages"][-1].pretty_print()  # output contains all messages in state
# print(output["messages"])
for m in output["messages"]:
    print(m)
    print()

cadeia_2 = "Quais é meu nome mesmo?" | app

output2 = cadeia_2.invoke(
    {"messages": input_messages},
)
for m in output2["messages"]:
    print(m)
    print()
