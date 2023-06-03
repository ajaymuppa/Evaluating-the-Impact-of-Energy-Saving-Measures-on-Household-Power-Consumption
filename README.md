# Evaluating-the-Impact-of-Energy-Saving-Measures-on-Household-Power-Consumption
Electricity sector in India. India is the world's third largest producer and third largest consumer of electricity. The gross electricity consumption in 2018-19 was 1,181 kWh per capita. Energy use can be viewed as a function of total GDP, structure of the economy and technology. The increase in household energy consumption is more significant than that in the industrial sector. To achieve reduction in electricity consumption, it is vital to have current information about household electricity use. This Guided Project mainly focuses on applying a machine-learning algorithm to calculate the power consumed by all appliances.  This will help you track the power consumed on regular intervals for all kinds of appliances which use heavy loads such as Air Conditioners, Oven or a washing machine etc.
## Project Objectives
By the end of this project:

    You’ll be able to understand the problem to classify if it is a regression or a classification kind of problem.
    You will be able to know how to pre-process/clean the data using different data pre-processing techniques.
    Applying different algorithms according to the dataset
    You will be able to know how to find the accuracy of the model.
    You will be able to build web applications using the Flask framework.
## Project Flow
Find below the project flow to be followed while developing the project.

    Download the dataset.
    Preprocess or clean the data.
    Analyze the pre-processed data.
    Train the machine with preprocessed data using an appropriate machine learning algorithm.
    Save the model and its dependencies.
    Build a Web application using flask that integrates with the model built.

Project Structure:

Create a Project folder which contains files as shown below

    household_power_consumption.txt is the dataset used.

    PCA.ipynb is the python file where algorithm is applied to dataset for testing and training. Finally, the model is saved for future use.

    PCA_model.pkl is the saved model used in flask to predict the output instantly for the given inputs.

    To build a Flask Application, save HTML pages in the templates folder and a python script PCA_Flask.ipynb for server-side scripting.

    The static folder contains an image used in html file.
## Prerequisites
In order to develop this project we need to install the following software/packages:


Step 1:

Anaconda Navigator :

Anaconda Navigator is a free and open-source distribution of the Python and R programming languages for data science and machine learning related applications. It can be installed on Windows, Linux, and macOS.Conda is an open-source, cross-platform,  package management system. Anaconda comes with great tools like JupyterLab, Jupyter Notebook, QtConsole, Spyder, Glueviz, Orange, Rstudio, Visual Studio Code. 

For this project, we will be using Jupyter notebook and Spyder


Step 2:

To build Machine learning models you must require the following packages

Sklearn: Scikit-learn is a library in Python that provides many unsupervised and supervised learning algorithms.

NumPy: NumPy is a Python package that stands for 'Numerical Python'. It is the core library for scientific computing, which contains a powerful n-dimensional array object  

Pandas: pandas is a fast, powerful, flexible, and easy to use open-source data analysis and manipulation tool, built on top of the Python programming language.  

Matplotlib: It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits

Flask: Web framework used for building Web applications. 

If you are using anaconda navigator, follow the below steps to download the required packages:

    Open anaconda prompt.
    Type “pip install numpy” and click enter.
    Type “pip install pandas” and click enter.
    Type “pip install matplotlib” and click enter.
    Type “pip install scikit-learn” and click enter.
    Type “pip install Flask” and click enter.

If you are using Pycharm IDE, you can install the packages through the command prompt and follow the same syntax as above.



## Collection of Dataset
The dataset which contains a set of features through which power consumption can be calculated, is to be collected. You can collect datasets from different open sources like kaggle.com, data.gov, UCI machine learning repository etc. 
For this project please refer to the link below to download.

https://www.kaggle.com/datasets/uciml/electric-power-consumption-data-set

