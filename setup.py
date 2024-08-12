from cx_Freeze import setup, Executable
import sys

# O código a ser convertido para executável
script = "Main1.py"

# Configuração para incluir as dependências necessárias
build_exe_options = {
    "packages": ["tkinter", "customtkinter"],  # Inclua os pacotes necessários
    "include_files": [],  # Arquivos adicionais que precisam ser incluídos
}

# Configuração para o executável
executables = [
    Executable(script, base="Win32GUI" if sys.platform == "win32" else None)
]

# Configuração do setup
setup(
    name="MeuSelectorDeCores",
    version="1.0",
    description="Um selector de cores simples usando tkinter e customtkinter",
    options={"build_exe": build_exe_options},
    executables=executables
)
