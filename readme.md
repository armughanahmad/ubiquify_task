## Updates by Armughan

### 09 August 2024
1. Setup the V2 directory
2. Setup the MVC formatted Project
    1. Replicated the models from the app/models:
        - PatentApplication
        - Forms
        - Questions
        - Answers
        - Documents
    2. Created the Schemas using Marshmallow for data serialization and validation
        - PatentApplicationSchema
        - FormsSchema
        - QuestionsSchema
        - AnswersSchema
        - DocumentsSchema
    3. Created the services to handle the database operations
        - PatentApplicationServices
        - FormsServices
        - QuestionsServices
        - AnswersServices
        - DocumentsServices
    4. Created the controllers to handle the services after data validations using schemas
        - PatentApplicationControllers
        - FormsControllers
        - QuestionsControllers
        - AnswersControllers
        - DocumentsControllers
    5. Add the routes using the flask blueprints to get the routes.
        - form_bp
        - document_bp
        - patent_application_bp
        - question_bp
        - answer_bp
    6. Integreted the routes in the app to access them.
3. How to run?
    1. Docker:
        - Dockerfile and docker-compose.yaml are included
        - Run following command, it will build it image and run the project at port 5555.
        `docker compose up -d`
    2. Virtual Env:
        - Create a virtual environment:
        `python -m venv venv` 
        - Install dependencies
        `pip install -r requirements.txt`
        - Database (if want to start from new data else skip it as these steps are already completed):
            - Delete the instance and migrations directory
            - Initialize database:
            `flask db init`
            - Migrate the database:
            `flask db migrate -m "initial migrations"`
            - Apply migrations:
            `flask db upgrade`
        - Run the project
        `flask run`
4. How to test?
    - Postman collection export is attached to the repo in postman directory.
        - Patent Applications, Forms, Questions can be tested for now.
        - Patent Applications Submission in progress.
    - Simply import the *postman/ubiquify-digital.postman_collection.json* in Postman.
    