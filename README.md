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