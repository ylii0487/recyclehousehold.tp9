import view

page_view = view.View()


def home_page():
    return page_view("HomePage")


def classification_page():
    return page_view("Classification")

def trend_page():
    return page_view("WasteTrends")

def event_page():
    return page_view("Event")


def feedback_page():
    return page_view("Feedback")


def faq_page():
    return page_view("FAQ")


def about_page():
    return page_view("AboutUs")
