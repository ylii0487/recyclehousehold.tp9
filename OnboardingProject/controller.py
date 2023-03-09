from flask import Flask, render_template
import model

app = Flask(__name__, template_folder="templates", static_folder='static')


@app.route('/')
@app.route('/home')
def index():  # put application's code here
    return model.home_page()


@app.route('/Classification')
def classification():
    return model.classification_page()


@app.route('/WasteTrends')
def trends():
    return model.trend_page()


@app.route('/Event')
def event():
    return model.event_page()


@app.route('/Feedback')
def feedback():
    return model.feedback_page()

@app.route('/FAQ')
def faq():
    return model.faq_page()

@app.route('/AboutUs')
def about():
    return model.about_page()


if __name__ == '__main__':
    app.run(debug=True)
