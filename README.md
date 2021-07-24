<h1>Documentation for running code</h1>

First of all type `python -m pip install -r requirements.txt` in your terminal

Using Migration
- Create Database 
- Go to `alembic.ini` file and edit `sqlalchemy.url` line 42, change the env with format `driver://user:pass@localhost/dbname`
- In case you need mock data, go to `alembic/versions/ff52e2b8b570_create_pasien_table.py` and uncomment line 36 - 73 then it will give you 3 mock data
- Type `alembic upgrade head` in terminal
- Migration is ready!

Finally for running application type `uvicorn main:app --reload` in terminal

Note:
For API Documentation and testing you can access `{{host}}/docs` or alternative `{{host}}/redoc`