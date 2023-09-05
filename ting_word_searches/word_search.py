def exists_word(word, instance):
    return search_word_in_files(word, instance, content=False)


def search_by_word(word, instance):
    return search_word_in_files(word, instance, content=True)


def search_word_in_files(word, instance, content):
    word_results = []

    for file in instance.items:
        occurrences = generate_occurrences(word, file, content)

        if occurrences:
            word_results.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences,
            })

    return word_results


def generate_occurrences(word, file, content):
    occurrences = []

    for line_number, sentence in enumerate(file["linhas_do_arquivo"], start=1):
        if word.lower() in sentence.lower():
            occurrence = {"linha": line_number}
            if content:
                occurrence["conteudo"] = sentence
            occurrences.append(occurrence)

    return occurrences
