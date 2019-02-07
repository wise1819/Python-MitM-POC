from flask import Flask, request
from requests.sessions import Session

app = Flask(__name__)
session = Session()


@app.route('/app/rest/timerecording/bookings', methods=['GET', 'POST'])
def projektron_bookings():
    def get_data():
        return session.get(
            'https://fu-projekt.bcs-hosting.de/app/rest/timerecording/bookings',
            # pass url params through to bcs
            params=dict(request.args)
        )

    data = get_data()

    if not data.ok:
        session.post('https://fu-projekt.bcs-hosting.de/app/rest/auth/login', json={
            'userLogin': request.form.get('userLogin'),
            'userPwd': request.form.get('userPwd')
        })
        data = get_data()

    return data.text


if __name__ == '__main__':
    app.run()
