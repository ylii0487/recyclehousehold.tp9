import datetime

import mysql.connector
from mysql.connector import errorcode


#
# try:
#     cnx = mysql.connector.connect(user="onboardingAdmin",
#                                   password="CNblue1996!",
#                                   host="onboarding-database.mysql.database.azure.com",
#                                   port=3306,
#                                   database="onboarding",
#                                   ssl_ca= "C:/Users/liyon/Desktop/2023S1/FIT5120/fit5120/OnboardingProject/DigiCertGlobalRootCA.crt.pem")
#
#     if cnx.is_connected():
#         print("Connection established")
#         cursor = cnx.cursor()
#         cursor.execute("SELECT 1")
#         result = cursor.fetchone()
#         print("Query result: ", result)
#         cnx.close()
#     else:
#         print("Connection failed.")
# except mysql.connector.Error as err:
#     print(err)
    # print("Something is wrong with the user name or password")



# hostname=recycling.mysql.database.azure.com
# username=fit5120TP9
# password={your-password}
# ssl-mode=require

class MySQLDatabase():

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(user="onboardingAdmin",
                                          password="CNblue1996!",
                                          host="onboarding-database.mysql.database.azure.com",
                                          port=3306,
                                          database="onboarding",
                                          ssl_ca= "C:/Users/liyon/Desktop/2023S1/FIT5120/fit5120/OnboardingProject/DigiCertGlobalRootCA.crt.pem")

            if self.conn.is_connected():
                print("Connection established")
                self.cursor = self.conn.cursor()

            else:
                print("Connection failed.")
        except mysql.connector.Error as err:
            print(err)


        # self.conn = mysql.connector.connect(
        #     user="onboardingAdmin",
        #     password="CNblue1996!",
        #     host="onboarding-database.mysql.database.azure.com",
        #     port=3306,
        #     database="onboarding",
        #     ssl_ca="C:/Users/liyon/Desktop/2023S1/FIT5120/fit5120/OnboardingProject/DigiCertGlobalRootCA.crt.pem")
        # self.cursor = self.conn.cursor()

    def execute(self, sql_string):

        output = None

        for string in sql_string.split(";"):
            try:
                output = self.cursor.execute(string)
            except:
                pass
        return output

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def tables_setup(self):

        sql = """CREATE TABLE IF NOT EXISTS Events(
                    event_topic varchar(20) NOT NULL,
                    event_time DATETIME NOT NULL,
                    event_place varchar(100) NOT NULL,
                    contact_details varchar(100) NOT NULL,
                    event_content varchar(500) NOT NULL
                  );  
                  CREATE TABLE IF NOT EXISTS Feedbacks(
                    feedback_name varchar(20) NOT NULL,
                    feedback_email varchar(20) NOT NULL,
                    feedback_subject varchar(100) NOT NULL,
                    feedback_comment varchar(100) NOT NULL

                )"""

        self.cursor.execute(sql, multi=True)
        self.commit()
        # self.add_event('Happy Recycling Day', '2023-03-21 15:00:00', 'Melbourne center', 'ylii0487@student.monash.edu', 'Learn learn learn!!')

    def add_event(self, event_topic, event_time, event_place, contact_details, event_content):


        sql_cmd = """INSERT INTO Events
                        VALUES('{event_topic}', '{event_time}','{event_place}', '{contact_details}', '{event_content}')
                        """.format(event_topic=event_topic, event_time=event_time, event_place=event_place, contact_details=contact_details, event_content=event_content)
        self.execute(sql_cmd)

        self.commit()

        return True

    def get_allEvents(self):
        sql_cmd = """SELECT *
                FROM Events
                """

        r = self.execute(sql_cmd)

        print(r)
        result = list(r.fetchall())

        self.commit()

        return result


    def add_feedback(self, feedback_name, feedback_email, feedback_subject, feedback_comment):
        sql_cmd = """INSERT INTO Events
                    VALUES('{feedback_name}', '{feedback_email}','{feedback_subject}', '{feedback_comment}')
                    """.format(feedback_name=feedback_name, feedback_email=feedback_email, feedback_subject=feedback_subject, feedback_comment=feedback_comment, event_content=event_content)
        self.execute(sql_cmd)

        self.commit()

        return True

    def get_allFeedback(self):
        sql_cmd = """SELECT *
                FROM Feedbacks
                """

        r = self.execute(sql_cmd)

        print(r)
        result = list(r.fetchall())

        self.commit()

        return result
# def connection(self, sql_string):
#     # Construct connection string
#
#     try:
#         conn = mysql.connector.connect(**self.conn)
#         print("Connection established")
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             print("Something is wrong with the user name or password")
#         elif err.errno == errorcode.ER_BAD_DB_ERROR:
#             print("Database does not exist")
#         else:
#             print(err)
#     else:
#         cursor = conn.cursor()
#
#         # Drop previous table of same name if one exists
#         cursor.execute("DROP TABLE IF EXISTS inventory;")
#         print("Finished dropping table (if existed).")
#
#         # Create table
#         cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
#         print("Finished creating table.")
#
#         # Insert some data into table
#         cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
#         print("Inserted", cursor.rowcount, "row(s) of data.")
#         cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
#         print("Inserted", cursor.rowcount, "row(s) of data.")
#         cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
#         print("Inserted", cursor.rowcount, "row(s) of data.")
#
#         # Cleanup
#         conn.commit()
#         cursor.close()
#         conn.close()
#         print("Done.")
