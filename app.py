from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user', methods=['GET','POST'])
def user():
    if request.method == 'POST':
        user = postUser(request.form)
        return render_template('success.html', Email=user['user']['email'], Phone=user['user']['phone'])
    else:
        return getUser()


def postUser(data):
    """ Returns success/failure json response from MYSQL insert | Type Dictionary """

    # Sample response
    response = {
        "status": True,
        "message": "Success",
        "user": {
            "email": data['Email'],
            "phone": data['Phone']
        }
    }

    return response


def getUser():
    """ Returns all signups from MYSQL | Type Array """

    # TODO: Query MYSQL using ORM for all signups

    sample_data = [{"Email": "sample@gmail.com", "Phone": "(718) 555 - 5555"}]
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(debug=True)