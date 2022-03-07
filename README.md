# An Analysis Of The Causal Relations Between Physical Measurements and Age of Abalone

## Description
This repository contains files that use the [causal-learn package](https://github.com/cmu-phil/causal-learn) to generate graphs that display the underlying causal relations of variables in the [Abalone dataset](http://archive.ics.uci.edu/ml/datasets/Abalone). For more information, please refer to [this paper](https://docs.google.com/document/d/1oqQMY6S2G05iiuzMhJ_pMmzAkpM-igoqgnsbFRlrRY4/edit?usp=sharing).

## Dependencies and Usage
The file parse.py is a script that automates the removal of missing data and representation of categorical variables in the Abalone dataset as integers. This script can be used by specifying the name of the file to be processed within the file and running
```
py parse.py
```
The file test.py stores and calls a series of functions that generate 3 causal graphs using the Peter-Clark (PC) algorithm, Fast Causal Inference (FCI) algorithm and Greedy Equivalence Search (GES). It uses functions from the causal-learn package, which can be obtained by cloning [this repository](https://github.com/cmu-phil/causal-learn) into the same directory as the file test.py.

This script can be run by specifying the file path to the data file to be processed within the file and running
```
py test.py
```