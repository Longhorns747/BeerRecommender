NUM_INGREDIENT_LISTS = 4
NUM_INGREDIENTS = 2
# Should add some exception handling with a message telling you that you're a dumbass and didn't fill out api_key
with open('api_key') as file:
	API_KEY = file.read()
PROJECT = 'https://ussouthcentral.services.azureml.net/workspaces/76c97bb7c7f640719cd92db28794a965/services/3a865a07cfd94e25b18374d30a41fda7/score'