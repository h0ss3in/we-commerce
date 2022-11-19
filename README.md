# WeCommerce

## How to Run

You need to have Docker and docker-compose to build and run the project

- Build the project: `docker-compose build`
- Run the project: `docker-compose up`

The project will be run on port **8080**

The endpoint is: **/checkout**

# Automated Testing

- Run `docker exec -ti <CONTAINER_NAME> sh` to access the running container from a second session
- Run `python -m pytest` to run the tests
- The tests are located at `app/tests`

# Technology

### Programming Language and Framework 
The programming language used in this application is **Python** and the framework is **FastAPI**, a modern and high-performance web framework for developing APIs with Python 3.6+. It offers high performance on par with NodeJS and GO because of advantage of handling requests asynchronously. It is used by top companies like Uber and Netflix to build their applications.

### Database
The **database** (watch catalogue) is considered as a key-value store similar to **NoSQL** Database (Python Dictionary). the reason is the **O(1)** time complexity that a **HashTable** provides us with searching, inserting and deleting items by key. 

# Approach

The application is developed in TDD and ATDD approaches.

Apart from that the general approach is defining a fastAPI router and injecting a dependency that is a class which is responsible for checkout process.

Then it will create checkout lines that are actually another HashTable (Python Dictionary) that the keys are the item ids and the value is the fetched data from database and the amount of the related item in user's shopping card. 

At the end the class will do a loop over the values of this HashTable and set the total price considering the discount plans and return this total price as response of the api.

The time complexity of this solution is **O(n)**

# What could be improved

- The structure of the input could be more complex, a json that the keys are ids and the values are the amount of the related product, and the calculation on backend could be a bit simpler and faster in this case. So instead of having a flat array like `["001", "002", "001"]` we could have `{"001": 2, "002": 1}`.
- It's not a good practice and realistic to store watch catalogue in a hard coded HashTable. It's better to use a database instead.
- It's good to get deeper in asynchronous features of the framework to improve the performance as much as possible.
- More error handling could be added
