from flask import Flask, request
import model

app = Flask(__name__, template_folder="templates", static_folder='static')




@app.route('/')
@app.route('/home')
def index():  # put application's code here
    return model.home_page()


@app.route('/Classification')
def classification():
    return model.classification_page()


@app.route('/WasteMap')
def trends():
    return model.trend_page()


@app.route('/Event', methods=['GET'])
def event():
    return model.event_page()


@app.route('/CreateEvent', methods=['POST', 'GET'])
def create_event():
    if request.method == 'GET':
        return model.create_eventPage()
    elif request.method == 'POST':
        event_topic = request.form['event_topic']
        event_time = request.form['event_time']
        event_place = request.form['event_place']
        contact_details = request.form['contact_details']
        event_content = request.form['event_content']
        return model.create_event(event_topic, event_time, event_place, contact_details, event_content)



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
