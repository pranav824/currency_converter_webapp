# Currency Converter

This is a simple currency converter application built using Django. The application allows users to convert amounts between different currencies and view historical conversion rates.

## Features

- Convert currency amounts between different currencies.
- View the last 5 days of historical conversion rates.
- Store and retrieve conversion history.

## Requirements

- Python 3.x
- Django 3.2 or higher
- requests
- python-decouple

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pranav824/currency_converter_webapp.git
   cd currency_converter

3. Remove .venv directory and create a new .venv and activate it, this will help the user not to install the dependencies globally. Since I am running a localhost I have created a virtual environment so that the dependencies are not installed globally into the system, which is a best practice.

2. Install the dependencies in requirements.txt

4. Make migrations:
   python manage.py makemigrations
   python manage.py migrate

3. To run the localhost - python manage.py runserver 

4. The localhost will directly lead to the index.html where the operation of conversion can be performed and tested.

**NOTE**: Use the API key within the application, else can create a new API key from https://app.exchangerate-api.com/ before the execution. Since app.exchangerate-api.com doesn't provide past 5 days historical data for the same conversion, it won't show the past 5 days value of the currencies in the index page. But it will work properly for other API provided websites which provides the past currency value data.
