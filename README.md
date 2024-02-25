# Dock-Kub-Flask-Proj
This project builds a simple web application using Flask, containerizes it using Docker, and deploys it on Kubernetes. 
The web application is a simple user registry that can add, delete, update, and get users and their information.
This aim of this project is to showcase the use of Docker and Kubernetes in deploying web applications. 

___

## User Schema
The user schema is as follows: 
```
user = {
    "id": 1, 
    "first_name": "John", 
    "last_name": "Doe", 
    "gender": "Male",
    "age": 24,
    "address":{
        "street": "123",
        "city": "Main Street",
        "state": "USA",
        "postal_code": "12345"
    },
    "phone_numbers": [
        {
            "type": "home",
            "number": "123456789
        }, 
        {
            "type": "work",
            "number": "987654321"
        }
    ]
}
```

## API Documentation 
## Endpoints
- **GET** `/users` : Get all users
- **POST** `/users` : Add a new user
- **GET** `/users/<int:id>` : Get a user by id
- **PUT** `/users/<int:id>` : Update a user by id
- **DELETE** `/users/<int:id>` : Delete a user by id
---
## Running the Application
**Prerequisites:** You would need to create a PostgreSQL database with the User, Address, and PhoneNumber tables to be 
able to run this locally. 
1. Clone the repository
2. Navigate to the project directory
3. Run the following commands:
    - `docker build -t dock-kub-flask-proj .`
    - `docker run -p 3030:3030 dock-kub-flask-proj`
4. To deploy the application on Kubernetes, run the following commands:
    - `kubectl apply -f deployment.yaml`
    - `kubectl apply -f service.yaml`
    - The application will be running on `http://localhost:3030`

## Kubernetes Deployment 
The application is deployed on Kubernetes using a deployment and a service. The Docker image is pulled from DockHub and 
deployed on the local minikube Kubernetes cluster.

Furthermore, I implemented Horizontal Pod Autoscaling (HPA) to automatically scale the number of pods in the deployment
based on CPU utilization. The HPA is configured to scale the number of pods between 1 and 10, with an average CPU 
utilization of 70%. If the demand on the web application decreases and there is no longer use for the newly created
pods, then the HPA will automatically scale down the number of pods. 

This functionality was tested using Postman Runner's stress testing capabilities. 


## Contact

For any inquiries or assistance, please contact [xena@maayah.com].
