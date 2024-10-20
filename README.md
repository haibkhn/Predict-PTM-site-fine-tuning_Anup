# Prediction of dephosphorylation sites using fine-tuned protein large models and integrate it as a Galaxy tool

Using fine-tuned transformer-based architecture (ProtTrans - short for Protein Transformer) to predict dephosphorylation sites and integrating it as a galaxy tool.

## Getting started

```bash
cd conda_requirements/
conda env create -f environment.yml
conda activate finetune-dephos
```
Remember to change the prefix if you want to install the environment in a different location.

## Datasets

Datasets are in fasta format and can be found src/input_datasets. Original datasets can be found here https://github.com/dukkakc/DTLDephos/tree/main/dataset

## Project Organization

```plaintext

├── README.md
├── Notebooks                               <- Jupyter notebooks
    ├── optuna.ipynb                        <- Notebook for hyperparameter optimization using optuna
    ├── smac.ipync                          <- Notebook for hyperparameter optimization using smac3
├── conda_requirements
    └── environment.yml                     <- The file necessary to recreate the analysis of requirements for the environment
├── Galaxy_tool                             <- XML tool and python script for running the tool in galaxy 
    ├── optuna_tool.xml                   
    ├── optuna_tool.py
├── input_datasets                          <- Datasets in fasta format
```

