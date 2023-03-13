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


@app.route('/WasteMap', methods=['GET'])
def trends():
    return model.trend_page()


@app.route('/Event', methods=['GET','POST'])
def event():
    if request.method == 'GET':
        return model.event_page()
    elif request.method == 'POST':
        search_keywords = request.form['search_keywords']
        return model.event_resultpgae(search_keywords)


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


@app.route('/Feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'GET':
        return model.feedback_page()
    elif request.method == 'POST':
        search_keywords = request.form['search_keywords']
        return model.feedback_resultpgae(search_keywords)


@app.route('/SubmitFeedback', methods=['POST', 'GET'])
def create_feedback():
    if request.method == 'GET':
        return model.create_feedbackPage()
    elif request.method == 'POST':
        feedback_name = request.form['feedback_name']
        feedback_email = request.form['feedback_email']
        feedback_subject = request.form['feedback_subject']
        feedback_comment = request.form['feedback_comment']
        return model.create_feedback(feedback_name, feedback_email, feedback_subject, feedback_comment)


@app.route('/FAQ')
def faq():
    return model.faq_page()


@app.route('/AboutUs')
def about():
    return model.about_page()


if __name__ == '__main__':
    app.run(debug=True)
