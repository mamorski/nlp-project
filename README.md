**This repository is a part of the submission of final project for the NLP course, Reichman University**
---

This repository comprises multiple Jupyter notebooks, each of which showcases our outcomes for the evaluation of different models using varying truncation parameter settings.

The code is splitted into different notebooks as a result of the long running time of the training process and due to resource constraints. Each notebook contains the evaluation of a different model. The models are described in the report.


## Notebooks
1. `binary-with-neutral.ipynb` - This notebook contains the evaluation of the binary classification model with the neutral class. As explained in the report, neutral class is the label 3 that was merged with negative labels.

2. `binary-without-neutral-and-bert-uncased.ipynb` - This notebook contains the evaluation of the binary classification model without the neutral class. As explained in the report, neutral class is the label 3 and in this approach it was omitted.


## Datasets
1. `train.csv` - The training dataset of the `amazon_multilingual_dataset`.
2. `test.csv` - The test dataset of the `amazon_multilingual_dataset`.
3. `valid.csv` - The validation dataset of the `amazon_multilingual_dataset`.
4. `amazon_translated_body_and_title_with_originals_all_stars.csv` - The dataset of the `amazon_multilingual_dataset` with the original labels and the translated reviews.
5. `IMDB Dataset.csv` - The dataset of the `IMDB Dataset`.

