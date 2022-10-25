from flask import render_template
from app import app

@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/cars')
def cars():
    fav_cars = ['mercedes s63 AMG', 'bmw m3', 'mercedes g63 amg', 'lexus lc500', 'audi r8']
    return render_template('cars.html', cars=fav_cars)