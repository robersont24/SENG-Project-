# SENG Project:
REST API 

# Project Title:
***

# Team Members:
- Nada Algafni
- Jesus Gil
- Randall McNeil
- Taylor Roberson

# Project Description:
This project is a RESTful calorie tracking service that allows users to log, manage, and analyze their daily food intake. The API provides structured endpoints for tracking meals, calorie totals, and related nutrition data while following REST principles and best practices for cloud deployment and security.

# Project Structure:

RESTful API:
The service exposes well-documented endpoints for managing food entries and daily calorie logs. Each route includes defined request/response (JSON) formats, HTTP status codes, and input validation to ensure accurate and reliable data handling.

Language: Python
Framework: FastAPI

Database:
CLoud SQL stores and manage data, including meals, calorie counts, and timestamps. The API supports full CRUD functionality:
  Create new food entries
  Retrieve daily or historical logs
  Update existing entries
  Delete logged items

Cloud Deployment (GCP):
The application is containerized through Docker and deployed to Cloud Run on Google Cloud Platform (GCP), to ensure consistent scalability and portability across environments.

Security:
IAM roles are set to least privilege, and secrets (database credentials) are managed through Secret Manager.

Baseline Operations:
Basic logging is implemented to support debugging and monitoring through GCP Cloud tools. 

Code: 
Documentation:
Testing:
