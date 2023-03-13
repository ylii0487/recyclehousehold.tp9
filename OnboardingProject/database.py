import datetime

import mysql.connector
from mysql.connector import errorcode


class MySQLDatabase():

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(user="root",
                                          password="fit5120",
                                          host="127.0.0.1",
                                          port=3306,
                                          database="onboarding")
                                          #ssl_ca= "C:/Users/liyon/Desktop/2023S1/FIT5120/fit5120/OnboardingProject/DigiCertGlobalRootCA.crt.pem")

            if self.conn.is_connected():
                print("Connection established")
                self.cursor = self.conn.cursor()

            else:
                print("Connection failed.")
        except mysql.connector.Error as err:
            print(err)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def tables_setup(self):

        sql = """CREATE TABLE IF NOT EXISTS Events(
                    event_id INT PRIMARY KEY AUTO_INCREMENT,
                    event_topic varchar(100) NOT NULL,
                    event_time DATETIME NOT NULL,
                    event_place varchar(100) NOT NULL,
                    contact_details varchar(100) NOT NULL,
                    event_content varchar(500) NOT NULL
                  );  
                  CREATE TABLE IF NOT EXISTS Feedbacks(
                    feedback_id INT PRIMARY KEY AUTO_INCREMENT,
                    feedback_name varchar(100) NOT NULL,
                    feedback_email varchar(100) NOT NULL,
                    feedback_subject varchar(100) NOT NULL,
                    feedback_comment varchar(100) NOT NULL

                );"""

        self.cursor.execute(sql, multi=True)
        self.commit()
        # self.add_event('Happy Recycling Day', '2023-03-21 15:00:00', 'Melbourne center', 'ylii0487@student.monash.edu', 'Learn learn learn!!')

    def add_event(self, event_topic, event_time, event_place, contact_details, event_content):


        sql_cmd = """INSERT INTO Events
                        VALUES('{event_topic}', '{event_time}','{event_place}', '{contact_details}', '{event_content}')
                        """.format(event_topic=event_topic, event_time=event_time, event_place=event_place, contact_details=contact_details, event_content=event_content)
        self.cursor.execute(sql_cmd)

        self.commit()

        return True

    def get_allEvents(self):
        sql_cmd = """SELECT * 
                FROM Events
                """

        self.cursor.execute(sql_cmd)


        result = list(self.cursor.fetchall())
        print(result)
        self.commit()

        return result


    def add_feedback(self, feedback_name, feedback_email, feedback_subject, feedback_comment):
        sql_cmd = """INSERT INTO Feedbacks
                    VALUES('{feedback_name}', '{feedback_email}','{feedback_subject}', '{feedback_comment}')
                    """.format(feedback_name=feedback_name, feedback_email=feedback_email, feedback_subject=feedback_subject, feedback_comment=feedback_comment)
        self.cursor.execute(sql_cmd)

        self.commit()

        return True

    def get_allFeedback(self):
        sql_cmd = """SELECT *
                FROM Feedbacks
                """

        self.cursor.execute(sql_cmd)

        result = list(self.cursor.fetchall())
        print(result)
        self.commit()

        return result
    
    #function used to get the data in recycle_area, and display in the wastemap page
    def get_allArea(self):
        sql_cmd = """
                SELECT * FROM recycle_area
                """
        
        self.cursor.execute(sql_cmd)
        result = list(self.cursor.fetchall())
        print(result)
        self.commit()

        return result
