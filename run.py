from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)
MENUDB = 'menu.db'




@app.route('/')
def index():
    db = sqlite3.connect(MENUDB)

    burgers= []
    cur = db.execute('SELECT burger,price FROM burgers')
    for row in cur:
        burgers.append(list(row))

    drinks= []
    cur = db.execute('SELECT drink,price FROM drinks')
    for row in cur:
        drinks.append(list(row))

    sides= []
    cur = db.execute('SELECT sides,price FROM sides')
    for row in cur:
        sides.append(list(row))

    db.close()


    return render_template('index.html', disclaimer='may contain traces of nuts', burgers=burgers, drinks=drinks, sides=sides)


@app.route('/order')
def order():
    return render_template('order.html')
