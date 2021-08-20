
# Bitcoin_Prediction_Django

## Introduction

This is a time series analysis project deployed with Django which gives users access to predicting Bitcoin price in a specific time period. The backend machine learning algorithm is Facebook [Prophet](https://facebook.github.io/prophet/), and frontend made with Javascript (Jquery), Html5 and Css3. Considering confidence intervals, three predicted values are generated for the chosen date. In this case, users can compare the predicted price, the interactive graph of historical bitcoin price, and their buying price (if possible) to make trading decisions. 

## Structure of the Django Project

<p align="center">
  <img width="350" src="https://github.com/fangyiyu/Bitcoin_Prediction_Django/blob/master/structure.png">
</p>
 
 ## Data
- The real-time bitcoin price chart in the homepage is from [Bitcoin.com API](https://developer.bitcoin.com/bitcoincom-link/docs/getting-started). 
- The data fed to the machine learning model for forecasting is fetched from [Binance API](https://python-binance.readthedocs.io/en/latest/).


## Run the application locally
- Create a virtual environment by ``` virtualenv <my_env_name>```
- Activate the env by ```<my_env_name>/bin/activate```
- Clone my Repo by ``` git clone <the https of the repo>```
- Get into the dir where manage.py is by ```cd Bitcoin_Prediction_Django```
- Install required packages by ``` pip install -r requirements.txt```. This step may take a while, since the pystan and prophet packages may take approximately up to three minutes. You may encounter "Failed building wheel for prophet", but the package will ultimately been installed.
- Make migrations by ``` python3 manage.py makemigrations```, then ``` python3 manage.py migrate```
- Run the application by ``` python3 manage.py runserver```

