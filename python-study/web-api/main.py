from flask import Flask

app = Flask(__name__)


@app.route('/getUsers')
def get_users():
    user = {}
    user['name'] = 'enzo'
    user['age'] = 25
    return user


if __name__ == "__main__":
    app.run(debug=True)