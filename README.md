# Seaborn Tutorial – Advanced Programming Project

**Author:** Karen Alderete Romo  
**Library:** [Seaborn](https://seaborn.pydata.org/)  
**Course:** Advanced Programming  
**Topic:** Why Would a Data Scientist Use This?

### Overview

Seaborn is a powerful Python data visualization library built on top of Matplotlib. It provides a high-level API for creating attractive and informative statistical graphics with minimal code. Designed for ease of use and beautiful default styles, it’s especially useful for data scientists performing quick exploratory data analysis (EDA).

### Why Use Seaborn?

- Seamless integration with pandas DataFrames
- Simple syntax for complex visualizations
- Built-in themes and color palettes
- Statistical plots like boxplots, histograms, heatmaps, and regression lines
- Excellent for EDA and data storytelling

### Installation

-Make sure you have Python installed, then install Seaborn using:
pip install seaborn 

-The library is also included as part of the Anaconda distribution, and it can be installed with conda:
conda install seaborn

### Dependencies
Supported Python versions
Python 3.8+

### Mandatory dependencies
numpy
pandas
matplotlib

### Optional dependencies
statsmodels, for advanced regression plots
scipy, for clustering matrices and some advanced options
fastcluster, faster clustering of large matrices

### Once you have seaborn installed, you’re ready to get started. To test it out, you could load and plot one of the example datasets:
import seaborn as sns
df = sns.load_dataset("penguins")
sns.pairplot(df, hue="species")

### If you’re working in a Jupyter notebook or an IPython terminal with matplotlib mode enabled, you should immediately see the plot. Otherwise, you may need to explicitly call matplotlib.pyplot.show()

### While you can get pretty far with only seaborn imported, having access to matplotlib functions is often useful. The tutorials and API documentation typically assume the following imports:

import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import seaborn.objects as so

### What you'll Learn in my Tutorial

- How to use Seaborn with real data
- How to build:
  - Histograms with KDE
  - Boxplots by category
  - Regression scatterplots
  - Heatmaps and pivoted data
  - Pairplots across numeric features
- How to apply styling with themes and palettes

# Project Contents

| File                       | Description                                       |
|--------------------------- |---------------------------------------------------|
| `seaborn_tutorial.ipynb`   | Main tutorial notebook with code and plots        |
| `README.md`                | This project overview file                        |
| `Seaborn_Presentation.pptx`| Slide deck covering key features and examples     |       

### Skills Demonstrated

- Clean, modular Python code (PEP-8)
- Statistical data visualization
- Exploratory Data Analysis (EDA)
- Use of built-in Seaborn datasets
- Effective documentation

### Resources

- [Seaborn Documentation](https://seaborn.pydata.org/)
- [PEP-8 Style Guide](https://peps.python.org/pep-0008/)

