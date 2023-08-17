from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

flight_passenger_association = db.Table(
    'flight_passenger_association',
    db.Column('flight_id', db.Integer, db.ForeignKey('flights.id'), primary_key=True),
    db.Column('passenger_id', db.Integer, db.ForeignKey('passengers.id'), primary_key=True)
)


class Passengers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    flights = db.relationship('Flights', secondary=flight_passenger_association,
                              back_populates='passengers', lazy=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Airports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    airport_name = db.Column(db.String(60), nullable=False)
    airport_code = db.Column(db.String(4), nullable=False)
    flights = db.relationship('Flights', backref='airport', lazy=True)

    def __str__(self):
        return f"{self.airport_name} ({self.airport_code})"


class Flights(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    departure = db.Column(db.String, db.ForeignKey('airport.airport_code'), nullable=False)
    arrival = db.Column(db.String, db.ForeignKey('airport.airport_code'), nullable=False)
    passengers = db.relationship('Passengers', back_populates='flights', secondary=flight_passenger_association,
                                 lazy=True)
