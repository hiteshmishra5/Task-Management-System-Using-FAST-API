# Task Management System

## Setup
1. Clone the repository.
2. Create a PostgreSQL database and update `database.py` with your credentials.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `uvicorn main:app --reload`


## Running Tests
Run all 3 function written one by one in test_task.py 

#API TESTING
Use Postman and import the JSON file from Github and run each API one at a time.

## API Endpoints
1. POST `/tasks/` - Create a task
2. GET `/tasks/` - Retrieve tasks
3. GET `/tasks/{task_id}` - get data by id
4. PUT `/tasks/{task_id}` - Update a task
5. DELETE `/tasks/{task_id}` - Delete a task



