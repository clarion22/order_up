from dotenv import load_dotenv
load_dotenv()  # noqa
from app import app, db
from app.models import Employee


# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234,
                        password="password")
    db.session.add(employee)
    db.session.commit()
