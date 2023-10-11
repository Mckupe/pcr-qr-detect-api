import datetime
from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config
import model
import orm
import repository
import services
import unit_of_work


orm.start_mappers()
get_session = sessionmaker(bind=create_engine(config.get_postgres_uri()))
app = Flask(__name__)

@app.route("/camera", methods=['POST'])
def add_camera():
    name = request.json['name']
    services.add_camera(
        name,
        unit_of_work.SqlAlchemyUnitOfWork(),
    )
    return 'OK', 201

@app.route("/tracking_object", methods=['POST'])
def add_tracking_object():
    label = request.json['name']
    services.add_tracking_object(
        label,
        unit_of_work.SqlAlchemyUnitOfWork(),
    )
    return 'OK', 201