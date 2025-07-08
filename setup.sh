#!/bin/bash

ENV_NAME="qa-agent"
ENV_DIR=".venv"

echo " Detectando entorno..."


if command -v conda &> /dev/null; then
    echo "Conda detectado. Creando entorno '$ENV_NAME'..."

    conda create -n $ENV_NAME python=3.11 -y
    conda activate $ENV_NAME || source activate $ENV_NAME

    echo "Instalando dependencias con pip..."
    pip install -r requirements.txt

else
    echo "Conda no detectado. Usando entorno virtual con venv..."

    python3 -m venv $ENV_DIR

    source $ENV_DIR/bin/activate 2>/dev/null || source $ENV_DIR/Scripts/activate

    echo "Instalando dependencias con pip..."
    pip install --upgrade pip
    pip install -r requirements.txt
fi


if [ ! -f .env ]; then
    echo "Creando archivo .env desde .env.example"
    cp .env.example .env
else
    echo "Archivo .env ya existe."
fi

echo ""
echo "Instalación completa."

if command -v conda &> /dev/null; then
    echo "➡️  Para ejecutar la app:"
    echo "   conda activate $ENV_NAME"
else
    echo "➡️  Para ejecutar la app:"
    echo "   source $ENV_DIR/bin/activate (o $ENV_DIR\\Scripts\\activate en Windows)"
fi

echo "   streamlit run app.py"
