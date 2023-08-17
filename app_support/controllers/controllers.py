from flask import Blueprint, render_template, request, redirect

from ..models.models import db, Passengers, Airports, Flights

bp = Blueprint('controllers', __name__)  # Using Blueprint for controller file


@db.route('/')
def index():
    pass


@db.route('/delete/<int:id>')
def delete():
    pass


@db.route('/add_passenger/')
def add_passenger():
    pass


@db.route('/add_airport/')
def add_airport():
    pass


@db.route('/add_flight/')
def add_flight():
    pass


@db.route('/details/')
def details():
    pass
