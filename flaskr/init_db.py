from flaskr.db import db_instance
from flaskr.models.user import UserModel
from sqlalchemy import inspect
from sqlalchemy_utils import database_exists, create_database

def model_exists(model_class):
    engine = db_instance.get_engine()
    inspector = inspect(engine)
    return inspector.has_table(model_class.__tablename__, model_class.__table_args__["schema"])

def init_load_data():
    engine = db_instance.get_engine()
    if not database_exists(engine.url):
        create_database(engine.url)
        
    if model_exists(UserModel):
        UserModel.init_data()
