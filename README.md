**Django REST API Machine Test**  

The project has three main entities:

1.User - Managed by Django’s default admin interface for registering users.
2.Client - Created, managed, and deleted using REST APIs.
3.Project - Created under a client, with multiple users assigned to each project.


Features
1.Register a Client:
Create a new client entity using the API.

2.Fetch Client Information:
Retrieve details for individual or all clients.

3.Edit/Delete Client Information:
Update or delete client data.

4.Add New Projects for a Client:
Create new projects under a specific client and assign users to those projects.

5.Retrieve Assigned Projects for Logged-in Users:
Fetch all projects assigned to the currently logged-in user

**Project Setup**

**1. Create the Project**:-
Start by creating the main project directory using Django’s django-admin command:
django-admin startproject task

**2. Create the App**:-
Navigate to the project folder and create a new app:
cd task
python manage.py startapp nimap

**3. Update Project URL Configuration**:-
In task/urls.py, include the app's URLs to set up endpoint routing

**4. Define Endpoints in the App**:-
In the app directory, create and define your API endpoints in urls.py

**5. Configure Database Connectivity**
Open task/settings.py and configure the database by adding the appropriate credentials

**6. Register the App in Installed Apps**
In task/settings.py, add your app name to the INSTALLED_APPS section

**7. Run Migrations and Start the Server**
Apply migrations and start the server to set up the database tables and check connectivity:
python manage.py migrate
python manage.py runserver

**8. Access the Admin Panel**
Go to http://127.0.0.1:8000/admin to access the Django admin panel and manage User entities.

#postman#
**Each feature can be tested by sending HTTP requests from Postman:**


