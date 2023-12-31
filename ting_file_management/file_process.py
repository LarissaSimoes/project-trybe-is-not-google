from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)
    informations = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    if not any(
        item["nome_do_arquivo"] == path_file
        for item in instance.items
    ):
        instance.enqueue(informations)
        sys.stdout.write(f"{informations}\n")


def remove(instance):
    if len(instance) > 0:
        item = instance.dequeue()
        sys.stdout.write(
            f"Arquivo {item['nome_do_arquivo']} removido com sucesso\n"
        )
    else:
        sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    if position >= 0 and position < len(instance):
        item = instance.search(position)
        sys.stdout.write(f"{item}\n")
    else:
        sys.stderr.write("Posição inválida\n")
