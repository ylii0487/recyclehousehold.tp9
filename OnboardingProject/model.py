import view
import database
import security

page_view = view.View()
database = database.MySQLDatabase()

database.tables_setup()

page_security = security.Security()


def home_page():
    return page_view("HomePage")


def classification_page():
    return page_view("Classification")


def map_page():
    area = database.get_allArea()
    return page_view("WasteMap", areas=area)


def event_page():
    events = database.get_allEvents()
    count = len(events)
    return page_view("Event", events=events, count=count+1)


def create_eventPage():
    return page_view("createEvent")


def create_event(event_topic, event_time, event_place, contact_details, event_content):
    if len(event_topic.split(" ")) == 0 or len(event_content.split(" ")) == 0 or len(contact_details.split(" ")) == 0:

        err_str = "event_topic or event_time or event_place or event_content or contact_details cannot be null"

        return page_view("invalid_add", reason=err_str)

    else:
        if page_security.is_xss(event_topic) or page_security.is_sql_injection(event_topic) or page_security.is_xss(contact_details) or page_security.is_sql_injection(contact_details) or page_security.is_xss(event_content) or page_security.is_sql_injection(event_content):
            err_str = "String formate is incorrect"
            return page_view("invalid_add", reason=err_str)
        else:
            event_create = database.add_event(event_topic, event_time, event_place, contact_details, event_content)
            events = database.get_allEvents()
            if event_create:
                return page_view("Event", events=events)
            else:
                err_str = "The new event is duplicate"
                return page_view("invalid_add", reason=err_str)





def faq_page():
    return page_view("FAQ")


def about_page():
    return page_view("AboutUs")


def event_resultpgae(search_keywords):
    if len(search_keywords.split(" ")) == 0:

        err_str = "search_keywords cannot be null"

        return page_view("invalid_add", reason=err_str)

    else:
        if page_security.is_xss(search_keywords) or page_security.is_sql_injection(search_keywords):
            err_str = "String formate is incorrect"
            return page_view("invalid_add", reason=err_str)
        else:
            events = database.get_searchEvent(search_keywords)

            if len(events) > 0:
                return page_view("Event", events=events)
            else:
                err_str = "Cannot find it"
                return page_view("invalid_add", reason=err_str)


def location_resultpage(search_keywords):
    if search_keywords is None:

        err_str = "search_keywords cannot be null"

        return page_view("invalid_add", reason=err_str)

    else:
        if page_security.is_xss(search_keywords) or page_security.is_sql_injection(search_keywords):
            err_str = "String formate is incorrect"
            return page_view("invalid_add", reason=err_str)
        else:
            results = database.get_searchLocation(search_keywords)

            if len(results) > 0:

                return page_view("MapResult", areas=results)
            else:

                err_str = "Cannot find it"
                return page_view("invalid_add", reason=err_str)


