import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("Falta la variable de entorno OPENAI_API_KEY. Agrégala al archivo .env o al entorno.")

llm = ChatOpenAI(
            model="gpt-4.1-mini",
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY")
            )

def generate_test_code(prompt: str, test_type: str) -> str:

    if test_type.lower() == "api":
        instruction = f"Escribe un test usando pytest y requests para: {prompt}"
    elif test_type.lower() == "web":
        instruction = f"Escribe un test usando pytest y selenium para: {prompt}"
    else:
        instruction = f"Escribe un test con pytest para: {prompt}"

    response = llm([HumanMessage(content=instruction)])
    full_text = response.content

    import re
    match = re.search(r"```(?:python)?\n(.*?)```", full_text, re.DOTALL)

    if match:
        return match.group(1).strip()
    else:
        return full_text.strip() 
