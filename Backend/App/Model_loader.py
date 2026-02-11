from llama_cpp import Llama

llm = None

def load_model(path: str):
    global llm
    llm = Llama(model_path=path, n_ctx=4096)
    return llm
