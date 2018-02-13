# Product Development Project

Install the requirements as Virtualenv in Python. The solution is using Python 2.7 and Django 1.11.

## Data Solution

The implementation done uses only two Database tables which models can be found in the productdev/api/models.py file.

The ER representation is as follow:

![alt text](https://raw.githubusercontent.com/hugoruivo/ProductDevelopmentProject/development/img/implemented.png)

### Insurance

Will have the insurance data, will store the names, ages, zip codes, etc... for the insurance.

The data will be saved as JSON in the database.

Sample Data:

{
    "firstname": "John",
    "lastname": "Doe",
    "age": 25,
    "gender": "male",
    "prize amount": 250000,
    "validation limit": "2020-01-31"
}

### Insurancetype

Will have the insurance type model, will store the skeleton of a type as well as a name for it.

The model will be saved as JSON in the database, with a structure as follows:

"field_name": "field_type"

Where "field_type" is one of the following:

`text`, `number`, `date`, or `array list of possible choices` (representing an `enum` type)

Sample Data:

{
    "firstname": "text",
    "lastname": "text",
    "age": "number",
    "gender": ["male", "female", "other"],
    "prize amount": "number",
    "validation limit": "date"
}

## Backend Solution

The solution file / app can be found in: `productdev/api` folder.

`urls.py` - Has the API URL's
`views.py` - Has the API Implementation / return values.

A couple of API have been implemented to return all risk types and a specific risk type based on it's id.

Calling <base_url>/api/v1/insurance/risktype/ or api/v1/insurance/risktype/0 will get ALL the existing Risk Types.

Calling <base_url>/api/v1/insurance/risktype/<int_id> will get the specific existing Risk Type if exists or empty if it doesn't exists.

Calling <base_url>/api/v1/insurance/get/<int_id> will get the specific existing Insurance data if exists or empty if it doesn't exists.


## Frontend Solution

The solution file / app can be found in: `productdev/insurance` folder.

`urls.py` - Has the URL's config
`views.py` - Has the view returned.
`templates/insurance/risktype.html` - Has a Vuejs implemented solution which uses the previous chapter API to list Insurance Types.

## AWS Lambda and Zappa

The Zappa config can be found in `productdev/zappa_settings.json` file.
