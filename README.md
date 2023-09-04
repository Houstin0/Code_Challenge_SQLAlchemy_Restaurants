# SQLAlchemy_Restaurants
## Description
This repository contains a restaurant review domain that contains reviews for restaurants posted by customers.
The database contains a restaurants table for the restaurants, a customers table for customers and a reviews table for restaurant reviews
## Project setup
1. Clone the repository to your local machine using git clone.
2. Navigate to the repository's directory.
4. Create pipenv environment and Install dependencies using pipenv install
5. Activate environment using  pipenv shell
6. Navigate into the app directory using cd app/
## Packages used
- sqlalchemy
- alembic 
- faker
## Usage
While in the app directory 
- run the 'run.py' file to see all functionality and deliverables test in the terminal.
- To populate database run the 'seed.py' file

### Review
- Review customer(), returns the `Customer` instance for this review

- Review restaurant(), returns the `Restaurant` instance for this review

- Review full_review(), should return a string formatted as follows:
Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.

### Restaurant
- Restaurant reviews(), returns a collection of all the reviews for the `Restaurant`

- Restaurant customers(), returns a collection of all the customers who reviewed the `Restaurant`

- Restaurant fanciest(), this method should be a class method, returns _one_ restaurant instance for the restaurant that has the highest   price

- Restaurant all_reviews(), should return an list of strings with all the reviews for this restaurant


### Customer
- Customer reviews(), returns a collection of all the reviews that the `Customer` has left

- Customer restaurants(), returns a collection of all the restaurants that the `Customer` has reviewed

- Customer full_name(), returns the full name of the customer, with the first name and the last name  concatenated, Western style.

- Customer favorite_restaurant(), returns the restaurant instance that has the highest star rating from this customer

- Customer add_review(restaurant, rating), takes a `restaurant` (an instance of the `Restaurant` class) and a rating and creates a new review for the restaurant with the given `restaurant_id`

- Customer delete_reviews(restaurant), takes a `restaurant` (an instance of the `Restaurant` class) and removes **all** their reviews for this restaurant

## Contributors
Houstin Angwenyi

## Licence
