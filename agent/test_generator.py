import os
from dotenv import load_dotenv
from langchain.llms import OpenAI

load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("Falta la variable de entorno OPENAI_API_KEY. Agrégala al archivo .env o al entorno.")

llm = OpenAI(temperature=0,
            model="gpt-4.1-mini",
            openai_api_key=os.getenv("OPENAI_API_KEY")
            )

def generate_test_code(prompt, test_type="web"):
    if test_type == "api":
        instruction = (
            "Eres un generador de pruebas API con Pytest y la librería requests.\n"
            "Genera una prueba basada en esta descripción:\n"
            f"{prompt}\n"
            "Debe contener una función test_* que haga al menos un assert."
        )
    else:
        instruction = (
            "Eres un generador de pruebas automatizadas UI con Pytest y Selenium.\n"
            "Genera una prueba basada en esta descripción:\n"
            f"{prompt}\n"
            "Debe contener una función test_*, usar Chrome y validar un elemento visible."
        )
    return llm(instruction)