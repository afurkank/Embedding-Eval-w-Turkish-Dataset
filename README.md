# Embedding-Eval-w-Turkish-Data

The project makes use of the Massive Text Embedding Benchmark (MTEB) and utilizes the MTEB library to assess various embedding models'(both custom and open source) capabilities for STS(Sentence to sentence) tasks and in the Turkish language.

Github repo of MTEB: https://github.com/embeddings-benchmark/mteb

Paper of MTEB: https://github.com/embeddings-benchmark/mteb

You can refer to the repo to create custom model evaluation scripts.

This repo contains scripts for the evaluation of Google's and OpenAI's embedding models, along with the most popular open-source embedding models.

You can find the open-source models here: https://huggingface.co/sentence-transformers?sort_models=downloads#models

Note that you need an API key to evaluate OpenAI's embedding models.

# Results

None of the open-source models could surpass OpenAI's "text-embedding-ada-002" model, which is their most up-to-date and best embedding model.
However, Google's "universal-sentence-encoder-multilingual-3" embedding model is pretty close and even surpasses ada-002 on some of the criteria.

Here is the output of the "find_best.py" script:
```
The model with the highest cos_sim-pearson score is: universal-sentence-encoder-multilingual-3
The highest cos_sim-pearson score is: 0.5956748719530833

The model with the highest cos_sim_spearman score is: text-embedding-ada-002
The highest cos_sim_spearman score is: 0.64498311459473

The model with the highest euclidean_pearson score is: universal-sentence-encoder-multilingual-3
The highest euclidean_pearson score is: 0.6238730506002852

The model with the highest euclidean_spearman score is: text-embedding-ada-002
The highest euclidean_spearman score is: 0.64498311459473

The model with the highest manhattan_pearson score is: text-embedding-ada-002
The highest manhattan_pearson score is: 0.6068273748824454

The model with the highest manhattan_spearman score is: text-embedding-ada-002
The highest manhattan_spearman score is: 0.6441179836604591

The model with the best score among all criteria is: text-embedding-ada-002
The best score is: 0.6188848263684004
```

Note that the "find_best.py" script uses the "benchmark_results.json" file to obtain the best results.

Every time you evaluate a new model, make sure to save the results in the "STS22_tr.json" file and then run the "json_cleaner.py" script to obtain the updated "benchmark_results.json" file. You can then again run the "find_best.py" script to get the best model.

# Citation of MTEB

```
@article{muennighoff2022mteb,
  doi = {10.48550/ARXIV.2210.07316},
  url = {https://arxiv.org/abs/2210.07316},
  author = {Muennighoff, Niklas and Tazi, Nouamane and Magne, Lo{\"\i}c and Reimers, Nils},
  title = {MTEB: Massive Text Embedding Benchmark},
  publisher = {arXiv},
  journal={arXiv preprint arXiv:2210.07316},  
  year = {2022}
}
```
