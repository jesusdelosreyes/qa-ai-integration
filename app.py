import streamlit as st
from agent.test_generator import generate_test_code
from agent.test_runner import run_pytest

st.title("🤖 QA Agent Generator with Pytest")

user_prompt = st.text_area("Describe tu prueba (Web o API):", height=150)

test_type = st.selectbox("Tipo de prueba:", ["web", "api"])

if st.button("Generar y Ejecutar Prueba", key=f"run_button_{test_type}"):
    with st.spinner("Generando prueba..."):
        test_code = generate_test_code(user_prompt, test_type)
        st.code(test_code, language="python")

        filename = f"tests/test_temp_{test_type}.py"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(test_code)

    with st.spinner("Ejecutando prueba..."):
        result = run_pytest(filename)
        st.success("Resultado de la prueba:")
        st.text(result)

    
