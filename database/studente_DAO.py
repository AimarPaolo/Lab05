# Add whatever it is needed to interface with the DB Table studente
import mysql.connector
from database.DB_connect import get_connection
from model.studente import Studente


class StudenteDAO:

    @staticmethod
    def get_studenti_map(id_map):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM studente"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(Studente(row["matricola"],
                                   row["cognome"],
                                   row["nome"],
                                   row["CDS"]))
        cursor.close()
        cnx.close()
        for res in result:
            id_map[res.matricola] = res
        return id_map
            #get connection
        #for each studente id_map["matricola"] = studente

    def getStudenti(self):
        # try:
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM studente"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(Studente(row["matricola"],
                                   row["cognome"],
                                   row["nome"],
                                   row["CDS"]))
        cursor.close()
        cnx.close()
        return result
        #except mysql.connector.Error as err:
        #    print(err)
        #    return None

    #non è necessario fare try, except in quanto viene già fatto nella classe DB_connect

    def studentsInCorso(self, codins):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM iscrizione i, studente s 
                    WHERE i.codins = %s and i.matricola = s.matricola"""
        cursor.execute(query, (codins,))
        result = []
        for row in cursor:
            result.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
        """query = select matricola from iscrizione where codins = %s
        cursor.execute(query, (codins,))
        result = []
        for row in cursor:
            matricola = row["matricola"]
            cnx2 = get_connection()
            cursor2 = cnx2.cursor(dictionary=True)
            query2 = SELECT * FROM studente where matricola = %s
            cursor2.execute(query2, (matricola,))
            for row2 in cursor2:
                result.append(Studente(row2["matricola"], row2["cognome"], row2["nome"], row2["CDS"]))
            cursor2.close()"""
        cursor.close()
        cnx.close()
        return result

    def get_nome_cognome(self, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM studente s 
                            WHERE matricola = %s"""
        cursor.execute(query, (matricola,))
        result = []
        for row in cursor:
            result.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
        cursor.close()
        cnx.close()
        return result


