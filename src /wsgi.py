from app import create_app
from flask import render_template

app = create_app()

@app.route('/')
def frontpage():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=False, port='5000')
