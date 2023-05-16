API Restful designed with Flask

Get Method brings the total of money spent grouped by category
load_products method brings all the information given in a json file so that we can manipulate the information

Categories method just returns us which are the categories within the information

money_spent_by_category returns the money spent for the given category with the respective discount

get_statistics is the main method for the api, which asks if there is any given parameter, if there is, checks if exists within the given categories
if not, it returns a 404 error saying that is not a valid category

In case that there is no parameter defined, simply returns the money spent in all categories

To run, install Flask and FlaskRestful libraries so it can be used
also, remember to install unittests framework for corresponding unit tests