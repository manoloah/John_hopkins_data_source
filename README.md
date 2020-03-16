# Antivirus

This project sets up a collaborative environment for data scientists to have readily accessible resources and dependencies to work with JHU's CSSE data for COVID-19 cases. 

The data is directly fetched raw from JHU's repository: https://github.com/CSSEGISandData/COVID-19.

## Environment Setup
This version works with Python 3.7 or later

To start, the following creates a virtual environment, it then activates it, and installs all the libraries and dependencies used in this project. 

```cmd
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

## Fetching Data 
fetch_data.py gets data directly from 
