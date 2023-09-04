import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print(f"Formato inválido", file=sys.stderr)
        return []

    try:
        with open(path_file, "r", encoding="utf-8") as file:
            lines = file.read().split("\n")
        return lines
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []

# Exemplo de uso:
if __name__ == "__main__":
    arquivo_txt = "exemplo.txt"  # Substitua pelo caminho do seu arquivo TXT
    linhas = txt_importer(arquivo_txt)
    if linhas:
        for linha in linhas:
            print(linha)
