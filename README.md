# document_management_tool
# Interactive Cares Document Management API

Welcome to the Interactive Cares Document Management API! This API system is designed to provide a robust document management solution with features such as document creation, updating, deletion, sharing, and access control.


# Features

- User Authentication: Users can sign up and log in to the system securely.
- Document Management: Create, update, and delete documents.
- Document Sharing: Share documents with other users.
- Access Control: Manage access to documents based on user permissions.

# Technologies Used

- Backend: Django with Django REST Framework
- Database: SQLite3 (built-in support), can be easily changed to other databases like PostgreSQL or MySQL.
- Authentication: Token-based authentication provided by Django REST Framework
- Documentation: Swagger/OpenAPI or Django Rest Swagger

# Setting Up the Application

- Clone the repository to your local machine
    - git clone <repository-url>

# Navigate to the project directory

    - cd interactive-cares-document-api

# Install dependencies

    - pip install -r requirements.txt

# Run the migrations

    - python manage.py migrate

# Run the development server

    - python manage.py runserver

# API Endpoints

    - User Signup: /api/signup/ (POST)
    - User Login: /api/login/ (POST)
    - Document CRUD:
    - Create Document: /api/docs/create/ (POST)
    - Update Document: /api/docs/update/<doc_id>/ (PUT)
    - Delete Document: /api/docs/delete/<doc_id>/ (DELETE)
    - Document Sharing:
    - Share Document: /api/docs/share/<doc_id>/ (POST)
    - Access Management:
    - Add/Update Access: /api/docs/access/<doc_id>/ (PUT)

# API Documentation

Detailed documentation for the API endpoints can be generated using Django Rest Swagger or you can manually create API documentation.

# Live Demo

A live demo of the application can be set up on your preferred hosting platform

# Additional Notes

Django REST Framework provides powerful tools for building APIs quickly and efficiently, allowing for easy customization and scalability.
Token-based authentication ensures secure access to the API endpoints
