import streamlit as st
import os
import subprocess
from agent.test_generator import generate_test_code

st.title("QA Agent Generator (LangChain + Pytest + OpenAI)")

user_prompt = st.text_input("Escribe lo que quieres probar (prompt):", "")

test_type = st.selectbox("Tipo de prueba", ["API", "Web"])

if st.button("Generar y Ejecutar Prueba", key="generate_and_run"):
    if not user_prompt.strip():
        st.warning("Por favor ingresa un prompt.")
    else:
        try:
            with st.spinner("Generando prueba con IA..."):
                test_code = generate_test_code(user_prompt, test_type)

                st.code(test_code, language="python")

                test_file_path = os.path.join("tests", "test_generated.py")
                os.makedirs("tests", exist_ok=True)
                with open(test_file_path, "w", encoding="utf-8") as f:
                    f.write(test_code)

                with st.spinner("Ejecutando prueba..."):
                    result = subprocess.run(
                        ["pytest", test_file_path, "-v"],
                        capture_output=True,
                        text=True
                    )

                st.subheader("Resultado de ejecución")
                st.text(result.stdout)

        except Exception as e:
            st.error(f"Ocurrió un error:\n\n{str(e)}")
