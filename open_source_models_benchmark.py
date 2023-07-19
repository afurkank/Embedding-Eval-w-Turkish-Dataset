from mteb import MTEB
from mteb.tasks import STS22CrosslingualSTS
from sentence_transformers import SentenceTransformer

# Define the sentence-transformers model name

# MODELS:
""" # all-distilroberta-v1
# allenai-specter
# all-MiniLM-L6-v2
# all-MiniLM-L12-v2
# all-mpnet-base-v2
# average-word-embeddings-komninos
# bert-base-nli-mean-tokens
# distilbert-base-nli-mean-tokens
# distilbert-base-nli-stsb-mean-tokens
# distiluse-base-multilingual-cased
# distiluse-base-multilingual-cased-v1
# distiluse-base-multilingual-cased-v2
# LaBSE
# msmarco-bert-base-dot-v5
# msmarco-distilbert-base-dot-prod-v3
# msmarco-distilbert-base-tas-b
# msmarco-distilbert-base-v4
# msmarco-MiniLM-L-12-v3
# multi-qa-MiniLM-L6-cos-v1
# multi-qa-mpnet-base-cos-v1
# multi-qa-mpnet-base-dot-v1
# nli-mpnet-base-v2
# paraphrased-MiniLM-L3-v2
# paraphrase-MiniLM-L6-v2
# paraphrase-mpnet-base-v2
# paraphrase-multilingual-MiniLM-L12-v2
# paraphrase-multilingual-mpnet-base-v2
# paraphrase-xlm-r-multilingual-v1
# sentence-t5-base
# stsb-xlm-r-multilingual
# xlm-r-100langs-bert-base-nli-stsb-mean-tokens """

model_name = "all-distilroberta-v1"

model = SentenceTransformer(model_name)

evaluation = MTEB(tasks=[STS22CrosslingualSTS(langs=['tr'])])

evaluation.run(model, eval_splits=["test"], output_folder=f"results/{model_name}")