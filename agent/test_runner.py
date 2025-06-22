import subprocess

def run_pytest(filepath):
    try:
        result = subprocess.run(
            ["pytest", filepath, "--tb=short", "-q"],
            capture_output=True,
            text=True,
            timeout=60
        )
        return result.stdout
    except subprocess.TimeoutExpired:
        return "⏱ Tiempo excedido al ejecutar la prueba"