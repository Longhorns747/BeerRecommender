NUM_INGREDIENT_LISTS = 4
NUM_INGREDIENTS = 2

try:
    with open('FlaskApplication/api_key') as f:
        API_KEY = f.read()
        if not API_KEY:
            raise EOFError
except (IOError, EOFError) as e:
    print("You forgot to create an api_key file. Good job.")
except EOFError:
    print("You forgot to enter your api_key. Smart.")

PROJECT = 'https://ussouthcentral.services.azureml' \
          '.net/workspaces/76c97bb7c7f640719cd92db28794a965/services/c4d6cda5f5854a4c9559d1d2e750d6bd/score'
