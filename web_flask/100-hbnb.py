#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB webpage"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(amenities, key=lambda amenity: amenity.name)
    places = storage.all(Place).values()
    sorted_places = sorted(places, key=lambda place: place.name)
    return render_template('100-hbnb.html', states=sorted_states, amenities=sorted_amenities, places=sorted_places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
