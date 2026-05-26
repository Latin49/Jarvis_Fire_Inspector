def build_context(results):

    documents = results["documents"][0]

    context = "\n\n".join(documents)

    return context