Sidecar_Project
==============================

# Creating Meaningful Business Labels and Descriptions from Technical Labels
![wordcloud](https://user-images.githubusercontent.com/94742221/156773336-c4d37efb-72f4-418f-b6a0-8e1fd11c1ddc.png)
[Marlies Monch](https://www.linkedin.com/in/marlies-monch/), [Dae-Jin Rhee](https://www.linkedin.com/in/dae-jin-rhee/)
------
### About The Project
This project was our capstone project at the Data Science Bootcamp at SIT Academy. 

### Motivation
Nowadays working with metadata is invaluable for any company working with large quantities of data.
But managing them can be a costly and time intensive endeavor, especially naming each data entry
manually.
With this project we aim to automate the process of generating meaningful business labels for companies
looking to manage their data efficiently.

### Methodology Used
Python:
1. Exploratory Data Analysis in Google Colab 
2. LDA Topic Modelling of the Business Descriptions
3. Look-up Dictionary for Labels
4. Word-level Sequence to Sequence Model to generate Business Names
5. Character-level Sequence to Sequence Model to generate Business Names
6. GPT-2 for generation of Business Descriptions

### Our approach
A NLP model is best suited for this project. 
As a benchmark, we first use a simple model to test out our approach and from there
use more complex NLP models for generating the Business Labels.

### Results 
Using a Language Translation model for generating Business names from auto-generated Technical names
yielding accurate results.
The Text Generation model for generating Business descriptions from Business names however were not
as accurate. 

### Next Steps
More data is required for the generation of Business descriptions. Trying a different model should 
produce better results.


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
