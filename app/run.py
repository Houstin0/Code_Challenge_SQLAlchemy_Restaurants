from models import *

if __name__ == '__main__':

    dummy_restaurant=session.query(Restaurant).first()
    dummy_review=session.query(Review).first()
    customer_query=session.query(Customer)
    dummy_customer=session.query(Customer).first()
    

    print('_______review_customer()_______')
    # returns the `Customer` instance for this review
    print(dummy_review.review_customer())

    print('_______review_restaurant()_______')
    # returns the `Restaurant` instance for this review
    print(dummy_review.review_restaurant())

    print('_______restaurant_reviews()_______')
    # returns a collection of all the reviews for the `Restaurant`
    print(dummy_restaurant.restaurant_reviews())

    print('_______restaurant_customers()_______')
    #  returns a collection of all the customers who reviewed the `Restaurant`
    print(dummy_restaurant.restaurant_customers())

    print('______customer_reviews()_______')
    # returns a collection of all the reviews that the `Customer` has left
    print(dummy_customer.customer_reviews())
    
    print('_______customer_restaurants()_______')
    # returns a collection of all the restaurants that the `Customer` has reviewed
    print(dummy_customer.customer_restaurants())
   
    print('_______customer full_name()_______')
     # returns the full name of the customer, with the first name and the last name  concatenated, Western style.
    print(dummy_customer.full_name())

    print('_______ customer favorite_restaurant()_______')
    #  returns the restaurant instance that has the highest star rating from this customer
    print(dummy_customer.favorite_restaurant())

    print('_______customer add_review(restaurant, rating)')
    # creates a new review for the restaurant with the given `restaurant_id`
    dummy_customer.add_review(dummy_restaurant,12)

    print('_______customer delete_reviews(restaurant)_______')
    # removes **all** their reviews for this restaurant
    dummy_customer.delete_reviews(dummy_restaurant)

    print('_______review full_review()_______')
    # should return a string
    print(dummy_review.full_review())

    print('_______Restaurant fanciest()_______')
    #  returns _one_ restaurant instance for the restaurant that has the highest   price
    print(Restaurant.fanciest)

    print('_______ restaurant all_reviews()_______')
    # should return an list of strings with all the reviews for this restaurant
    print(dummy_restaurant.all_reviews())