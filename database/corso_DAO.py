# Add whatever it is needed to interface with the DB Table corso
import mysql.connector
from model.corso import Corso
from database.DB_connect import get_connection


class CorsoDao:
    pass


class CorsoDao:
    def getCorsi(self):
        try:
            cnx = get_connection()
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * FROM corso"""
            cursor.execute(query)
            result = []
            for row in cursor:
                result.append(Corso(row["codins"],
                                    row["crediti"],
                                    row["nome"],
                                    row["pd"]))
            cursor.close()
            cnx.close()
            return result
        except mysql.connector.Error as err:
            print(err)
            return None