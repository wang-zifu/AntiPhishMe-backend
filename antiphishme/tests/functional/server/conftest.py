import pytest
import allure
import connexion
import json
from flask_sqlalchemy import SQLAlchemy
from antiphishme.src.config import (
    connexion_app, 
    BASE_PATH, 
    SWAGGER_DIR, 
    arguments, 
    AUTH_API_KEY,
    SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS
)

from antiphishme.tests.test_helpers import (
    data_to_json, 
    info, 
    assert_equal, 
    assert_dict_contains_key
)


@allure.step("Set up Flask client with db")
@pytest.fixture(scope="module")
def client_with_db():
    info("Set up Flask client with db", pre=True)
    flask_app = connexion.FlaskApp(__name__, specification_dir="../../../src/swagger")
    flask_app.app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    flask_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.app.json_encoder = json.JSONEncoder
    flask_app.add_api('swagger.yml', base_path=BASE_PATH, arguments=arguments)
    db = SQLAlchemy(flask_app.app)
    with flask_app.app.test_client() as c:
        yield c, db
    db.session.remove()
    db.drop_all()