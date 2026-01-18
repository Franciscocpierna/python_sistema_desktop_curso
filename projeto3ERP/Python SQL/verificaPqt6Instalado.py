import sys
import os
import subprocess

def check_env():
    print("--- DIAGNÓSTICO DE AMBIENTE ---")
    print(f"Executável Python sendo usado:\n{sys.executable}")
    print(f"\nVersão do Python: {sys.version}")
    
    print("\nTentando localizar PyQt6...")
    try:
        import PyQt6
        print("SUCESSO: PyQt6 está instalado e acessível!")
        print(f"Caminho do PyQt6: {PyQt6.__file__}")
    except ImportError:
        print("ERRO: PyQt6 NÃO foi encontrado neste ambiente.")
        
        print("\nTentando listar pacotes instalados neste interpretador:")
        try:
            result = subprocess.check_output([sys.executable, "-m", "pip", "list"]).decode()
            if "PyQt6" in result:
                print("ESTRANHO: O pip diz que PyQt6 está na lista, mas o Python não o importa.")
            else:
                print("CONFIRMADO: PyQt6 não consta na lista de pacotes deste Python.")
                print("\nSUGESTÃO: Execute o comando abaixo no terminal:")
                print(f"{sys.executable} -m pip install PyQt6")
        except Exception as e:
            print(f"Não foi possível rodar o pip: {e}")

if __name__ == "__main__":
    check_env()