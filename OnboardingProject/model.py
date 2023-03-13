import view
import database
import datetime

page_view = view.View()
database = database.MySQLDatabase()

database.tables_setup()


def home_page():
    return page_view("HomePage")


def classification_page():
    return page_view("Classification")


def trend_page():
    area= database.get_allArea()
    return page_view("WasteMap", areas = area)


def event_page():
    events = database.get_allEvents()
    return page_view("Event", events=events)


def create_eventPage():
    return page_view("createEvent")


def create_event(event_topic, event_time, event_place, contact_details, event_content):
    if event_topic is None or event_time is None or event_place is None or event_content is None or contact_details is None:

        err_str = "event_topic or event_time or event_place or event_content or contact_details cannot be null"

        return page_view("invalid_add", reason=err_str)

    else:

        event_create = database.add_event(event_topic, event_time, event_place, contact_details, event_content)
        events = database.get_allEvents()
        if event_create:
            return page_view("Event", events=events)
        else:
            err_str = "The new event is duplicate"
            return page_view("invalid_add", reason=err_str)


def feedback_page():
    feedbacks = database.get_allFeedback()
    return page_view("Feedback", feedbacks=feedbacks)


def create_feedbackPage():
    return page_view("createFeedback")


def create_feedback(feedback_name, feedback_email, feedback_subject, feedback_comment):
    if feedback_name is None or feedback_email is None or feedback_subject is None or feedback_comment is None:

        err_str = "feedback_name or feedback_email or feedback_subject or feedback_comment cannot be null"

        return page_view("invalid_add", reason=err_str)

    else:

        feedback_create = database.add_feedback(feedback_name, feedback_email, feedback_subject, feedback_comment)

        if feedback_create:
            feedbacks = database.get_allFeedback()
            return page_view("Feedback", feedbacks=feedbacks)
        else:
            err_str = "The new feedback is duplicate"
            return page_view("invalid_add", reason=err_str)


def faq_page():
    return page_view("FAQ")


def about_page():
    return page_view("AboutUs")


def event_resultpgae(search_keywords):
    if search_keywords is None:

        err_str = "search_keywords cannot be null"

        return page_view("invalid_add", reason=err_str)

    else:

        events = database.get_searchEvent(search_keywords)

        if len(events) > 0:
            return page_view("Event", events=events)
        else:
            err_str = "Cannot find it"
            return page_view("invalid_add", reason=err_str)


def feedback_resultpgae(search_keywords):

    if search_keywords is None:

        err_str = "search_keywords cannot be null"

        return page_view("invalid_add", reason=err_str)

    else:

        feedbacks = database.get_searchFeedback(search_keywords)


        if len(feedbacks) > 0:

            return page_view("Feedback", feedbacks=feedbacks)
        else:

            err_str = "Cannot find it"
            return page_view("invalid_add", reason=err_str)
