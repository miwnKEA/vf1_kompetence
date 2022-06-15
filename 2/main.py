from flask import Flask, render_template
from Services.car_salesbonus import Car


app = Flask(__name__)


car1 = Car('Volkswagen', 'Golf', 'Grøn', True, 28000, 24000, 18.1, ['Skifte gearkassen i 2018', 'Dækskifte til vintersæson'])
car2 = Car('Toyota', 'Prius', 'Blå', False, 50000, 40000, 15.8, [])
car3 = Car('Ford', 'Mustang', 'Rød', False, 44500, 30000, 16.5, ['Klargøring til sommersalg'])
car4 = Car('Tesla', '3', 'Rød', True, 70000, 40000, 16.5, ['Nyt batteri'])


cars = [car1, car2, car3, car4]


@app.route('/')
def index():
    return render_template('index.html', cars=cars)


if __name__ == '__main__':
    app.run()
