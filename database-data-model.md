# CalPal Database / Data Model

## Overview
This project uses a relational database to support user accounts, calorie tracking, categories, and calorie goals. The database is designed to support the MVP features of the calorie tracking application, including authentication, CRUD operations, summaries, and goal tracking.

## Tables

### 1. Users
Stores account information for each user.

| Field | Type | Required | Constraints | Description |
|---|---|---|---|---|
| id | Integer | Yes | Primary Key, Auto Increment | Unique user ID |
| email | Varchar | Yes | Unique, Not Null | User email address |
| password_hash | Varchar | Yes | Not Null | Hashed password |
| full_name | Varchar | No |  | User full name |
| account_type | Varchar | Yes | Default 'individual' | Individual or company account |
| created_at | Timestamp | Yes | Not Null | Account creation timestamp |
| updated_at | Timestamp | No |  | Last update timestamp |

---

### 2. Categories

| Field | Type | Required | Constraints | Description |
|---|---|---|---|---|
| id | Integer | Yes | Primary Key, Auto Increment | Unique category ID |
| user_id | Integer | No | Foreign Key -> Users.id | Owner of category |
| name | Varchar | Yes | Not Null | Category name |
| description | Varchar | No |  | Category description |
| created_at | Timestamp | Yes | Not Null | Creation timestamp |

---

### 3. CalorieEntries

| Field | Type | Required | Constraints | Description |
|---|---|---|---|---|
| id | Integer | Yes | Primary Key, Auto Increment | Unique entry ID |
| user_id | Integer | Yes | Foreign Key -> Users.id, Not Null | Owner of entry |
| category_id | Integer | No | Foreign Key -> Categories.id | Entry category |
| food_name | Varchar | Yes | Not Null | Name of food |
| description | Text | No |  | Optional notes |
| calories | Integer | Yes | Must be > 0 | Calorie value |
| entry_date | Date | Yes | Not Null | Entry date |
| created_at | Timestamp | Yes | Not Null | Created timestamp |
| updated_at | Timestamp | No |  | Last update |

---

### 4. Goals

| Field | Type | Required | Constraints | Description |
|---|---|---|---|---|
| id | Integer | Yes | Primary Key, Auto Increment | Unique goal ID |
| user_id | Integer | Yes | Foreign Key -> Users.id | Owner of goal |
| daily_calorie_limit | Integer | Yes | Must be > 0 | Daily calorie target |
| start_date | Date | Yes | Not Null | Start date |
| end_date | Date | No |  | End date |
| created_at | Timestamp | Yes | Not Null | Created timestamp |

---

## Relationships

- One user can have many calorie entries  
- One user can have many goals  
- One user can create many categories  
- One category can be used by many calorie entries  

---

## Constraints Summary

- Users.email must be unique  
- Required fields cannot be null  
- calories must be greater than 0  
- daily_calorie_limit must be greater than 0  
- Foreign keys must reference existing records  

---

## Why This Data Model Supports the MVP

This design supports:

- user authentication  
- calorie entry CRUD operations  
- meal categorization  
- historical calorie tracking  
- goal tracking  
- summary reporting  
