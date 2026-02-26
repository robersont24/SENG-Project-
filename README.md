# SENG-Project-
REST API 

# Project Title
***

# Team Members
- Nada Algafni
- Jesus Gil
- Randall McNeil
- Taylor Roberson

# Project Description
This project is a RESTful Calorie Tracking service that allows users to log, manage, and analyze their daily food intake. The API provides structured endpoints for tracking meals, calorie totals, and related nutrition data while following REST principles and best practices for cloud deployment and security.

# Project Structure

RESTful API:
The service exposes well-documented endpoints for managing food entries and daily calorie logs. Each route includes defined request/response formats, HTTP status codes, and input validation to ensure accurate and reliable data handling.

Database:
Using MySQL to store and manage data
The application uses a managed database to persist user data, including meals, calorie counts, and timestamps. The API supports full CRUD functionality:
  Create new food entries
  Retrieve daily or historical logs
  Update existing entries
  Delete logged items

Cloud Deployment (GCP):
The application is containerized through Docker and deployed on Google Cloud Platform (GCP). This ensures consistent runtime behavior, scalability, and portability across environments.

Security:
IAM roles follow the principle of least privilege.
Secrets (database credentials) are managed using Secret Manager.

Operational Hygiene:
Basic logging is implemented to support debugging and monitoring through Cloud. 
A clear teardown process is documented to properly remove cloud resources and prevent unnecessary costs.

- /src → Source code
- /docs → Documentation
- /tests → Test files
