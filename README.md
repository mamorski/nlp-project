**This repository is a part of the submission of final project for the NLP course, Reichman University**
---

This repository comprises multiple Jupyter notebooks, each of which showcases our outcomes for the evaluation of different models using varying truncation parameter settings.

The code is splitted into different notebooks as a result of the long running time of the training process and due to resource constraints. Each notebook contains the evaluation of a different model. The models are described in the report.


## Notebooks
1. `binary-with-neutral.ipynb` - This notebook contains the evaluation of the binary classification model with the neutral class. As explained in the report, neutral class is the label 3 that was merged with negative labels.

2. `binary-without-neutral-and-bert-uncased.ipynb` - This notebook contains the evaluation of the binary classification model without the neutral class. As explained in the report, neutral class is the label 3 and in this approach it was omitted.

3. `final_results_imdb_amazon_five_labels_amazon_two_labels_with_neutral_without_neutral_test_amazon_on_imdb_multilingual.ipynb` - as its name suggests, it contains all final results for imdb, amazon five labels, amazon two labels w(with/without Neutral) and also models trained on Amazon dataset (with/without Neutral) and tested on IMDB test set.


## Datasets
1. `train.csv` - The training dataset of the `amazon_multilingual_dataset`.
2. `test.csv` - The test dataset of the `amazon_multilingual_dataset`.
3. `valid.csv` - The validation dataset of the `amazon_multilingual_dataset`.
4. `amazon_translated_body_and_title_with_originals_all_stars.csv` - The dataset of the `amazon_multilingual_dataset` with the original labels and the translated reviews.
5. `IMDB Dataset.csv` - The dataset of the `IMDB Dataset`.


## Results Table (Full)
1. `results.csv`


## Convert Results Table to Latex (by best models)

1. `ConvertTableToLatex.py`