# SoftDesk

SoftDesk is a project management platform that allows users to manage projects, issues, and comments in a secure, scalable, and energy-efficient way. This API serves as the backend system for client applications across different platforms. The API is designed with security standards (OWASP), GDPR compliance, and optimized for green code principles.

## Features

- **User Management:**
  - Authentication with JSON Web Tokens (JWT).
  - Age verification for data collection and consent.
  - Privacy options with GDPR compliance (can_be_contacted, can_data_be_shared).
- **Project Management:**
  - Create, update, and delete projects.
  - Projects can be categorized by type (Back-end, Front-end, iOS, Android).
- **Issue Management:**
  - Create, assign, and prioritize issues (tasks/bugs).
  - Issues can be tagged with different priorities (LOW, MEDIUM, HIGH) and types (BUG, TASK, FEATURE).
- **Comment System**
  - Comment on issues to facilitate team collaboration.
  - Comments are tied to specific issues.
- **Security:**
  - Implements OWASP security standards.
  - Role-based access control for project contributors.
- **Green Code:**
  - Optimized queries to reduce server load and increase efficiency.

## Prerequisites

- Python 3.x
- [pip](https://pip.pypa.io/en/stable/)

## Installation

1. **Clone the GitHub repository**

    ```sh
    git clone https://github.com/HDanDev/SoftDesk.git
    cd SoftDesk
    ```
   
2. **Install Pipenv**

    ```sh
    pip install pipenv
    pipenv install
    ```

3. **Activate the virtual environment**

    ```sh
    pipenv shell
    ```

4. **Install dependencies**
   
   ```sh
   pipenv install -r requirements.txt
   ```

5. **Move within managing scope**

   ```sh
   cd softdesk
   ```

## Usage

   Run the development server

   ```sh
   py manage.py runserver
   ```

   Access the application

   Open your browser and go to: http://localhost:8000

  Or use a tool such as [Postman](https://identity.getpostman.com/login) to simplify your requests.

## Endpoints

| Method | Endpoint                    | Description                     |
|--------|-----------------------------|---------------------------------|
| POST   | `/users/register`            | Register a new user             |
| POST   | `/users/login`               | User login, returns JWT         |
| GET    | `/projects`                  | List all projects               |
| POST   | `/projects`                  | Create a new project            |
| GET    | `/projects/:id`              | Get a single project            |
| PUT    | `/projects/:id`              | Update a project                |
| DELETE | `/projects/:id`              | Delete a project                |
| POST   | `/projects/:id/issues`       | Create an issue for a project   |
| GET    | `/projects/:id/issues`       | Get all issues for a project    |
| POST   | `/issues/:id/comments`       | Add a comment to an issue       |
| GET    | `/issues/:id/comments`       | List comments on an issue       |
