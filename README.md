### Description:

Locaverse_Backend_Challenge is a project created for the Backend Internship
application task for Locaverse Vienna. It is a Flask API designed
to normalize Austrian phone numbers. The project includes full API CRUD and
SQLite3 database support, and accepts one phone number at a time as JSON.
The phone number can be written as a string in many various formats.
The project uses PhoneNumbers library to validate and format the numbers to 
start with +43 and only contain numbers, leaving no spaces, dashes, letters
or any special characters. After normalization, the new phone number is returned
as JSON from the route.


### Launchung the Project:

Clone the repository and navigate to it's root directory in the command line:

```
git clone 
```

```
cd coding_challenge
```

Create and activate the virtual environment:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Or, for Windows users:

```
source venv/Scripts/activate
```

Install project dependencies from the requirements.txt file:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Run pytest to check for project integrity:

```
pytest
```

Launch the project:

```
flask run
```
