# Agile Task Manager (ATM) - Backend

## Overview
The Agile Task Manager (ATM) is a Django-based backend for a task management and collaboration tool. It's designed to provide robust and scalable support for managing tasks and projects in a real-time collaborative environment.

## Backend Features Checklist
- [ ] **User Authentication**
  - Secure login and registration system using Django's built-in authentication.
- [ ] **Project Management**
  - APIs to create, view, update, and delete projects.
- [ ] **Task Tracking**
  - APIs to add, update, and delete tasks within projects.
- [ ] **Real-Time Collaboration**
  - Integration of Django Channels and WebSockets for real-time updates.
- [ ] **Commenting System**
  - API endpoints for enabling discussions on tasks.
- [ ] **Notifications**
  - Real-time alerts and notifications for task updates and comments.
- [ ] **User Roles and Permissions**
  - Manage different access levels for users.
- [ ] **Database Integration**
  - Configured to use PostgreSQL for data persistence.

## Technology Stack
- **Backend Framework:** Django (Python)
- **Database:** PostgreSQL
- **Real-Time Functionality:** Django Channels and WebSockets
- **Authentication:** Django’s built-in authentication system

## Getting Started

### Prerequisites
- Python 3.x
- Django
- PostgreSQL
- Django Channels

### Installation
1. Clone the repository:
   ```bash
   git clone [repository-url]
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your PostgreSQL database.

4. Create a `.env` file in the root directory and populate it with your database credentials and other necessary environment variables.

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Documentation
- API Documentation
- Database Schema
- System Architecture

## Testing
- Instructions for running and writing tests.
