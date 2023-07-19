import tensorflow_hub as hub
from tensorflow_text import SentencepieceTokenizer
import tensorflow as tf
import tensorflow_hub as hub
from mteb.tasks import STS22CrosslingualSTS
from mteb import MTEB

url = "https://tfhub.dev/google/universal-sentence-encoder-multilingual/3"
# url = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual-large/3")
# url = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
# url = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")

embedder=hub.load(url)

model_name = url.split('/')[-2] + '-' + url.split('/')[-1]

print(model_name)

TASK_LIST_STS = [
    "STS22"
]

TASK_LIST = TASK_LIST_STS

class USE():
    def encode(self, sentences, **kwargs):
        embeddings = []
        for _, sentence in enumerate(sentences):
            embedding = embedder(sentence)
            embeddings.extend(embedding)
        return embeddings

model = USE()

def start_eval():
    for task in TASK_LIST:
        print("Running task: ", task)
        model = USE()
        evaluation = MTEB(tasks=[STS22CrosslingualSTS(langs=['tr'])])
        evaluation.run(model, 
        output_folder=f"./results/{model_name}", 
        batch_size=1, 
        corpus_chunk_size = 10000)

start_eval()
