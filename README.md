# Navia Care Assignment Project

Clone the repo - git clone https://github.com/rmanjhi/naviacare.git

install any virtual environment -

install the dependencies - pip install -r requirements.txt

run the migrations and createsuperuser

Start the Server - ./manage.py runserver 0:8080
start server at any point of your choice - I used 'http://localhost:8080'


Features implemented-

- Create new users - 
 URL - 'http://localhost:8080/api/users/'
 Method - POST
payload - {
"first_name":"rajeev",
"last_name":"kumar",
"company_name":"Naviacare",
"city":"Gurgaon",
"state":"Haryana",
"zip":12205,
"web":"rmanjhi.cse13@nituk.ac.in",
"email":"www.naviacare.com",
"age":23
}

on User already exist which you want to update - 'requested user already exist..'
on success response - 'User has been inserted successfully' status code -200
on error response - 'Error occurred while updating the users' status code -400

-update the exisitng user 
 URL - 'http://localhost:8080/api/users/1/'
 Method - PUT
 payload - {
"first_name":"rajeev",
"last_name":"kumar",
"company_name":"Naviacare",
"city":"Gurgaon",
"state":"Haryana",
"zip":12205,
"web":"rmanjhi.cse13@nituk.ac.in",
"email":"www.naviacare.com",
"age":23
}

on User doesn't exist which you want to update - 'requested user doesn't exist..'
on success response - 'User has been updated successfully' status code -200
on error response - 'Error occurred while updating the users' status code -400

-Delete an user
URL - http://localhost:8080/api/users/1/'
Method - DELETE

on User doesn't exist which you want to delete - 'requested user doesn't exist..'
on success response - 'User has been deleted successfully' status code -200
on error response - 'Error occurred while deleting the users' status code -400

List Api's Implemented- 
URL's - 'http://localhost:8080/api/users'

Response -

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "first_name": "rajeev",
            "last_name": "Kumar",
            "company_name": "Navia Care",
            "age": 28,
            "city": "Gurgoan",
            "state": "Haryana",
            "zip": 122005,
            "email": "rmanjhi.cse13@nituk.ac.in",
            "web": "www.naviacare.com"
        }
    ]
}



POSTMAN COllection - 'https://www.getpostman.com/collections/3f86507b0c77f27a618e'
