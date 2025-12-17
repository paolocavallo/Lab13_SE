

from database.DB_connect import DBConnect
from model.gene import Gene
from model.interazione import Interazione


class DAO:

    @staticmethod
    def get_geni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM gene """

        cursor.execute(query)

        for row in cursor:
            gene = Gene(row["id"], row["funzione"], row["essenziale"], row["cromosoma"])
            result.append(gene)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_interazione():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM interazione """
        cursor.execute(query)
        for row in cursor:
            interazione = Interazione(row["id_gene1"], row["id_gene2"], row["tipo"], row["correlazione"])
            result.append(interazione)
        cursor.close()
        conn.close()
        return result


    def get_interazioni(self):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT g1.cromosoma as cromosoma1, g2.cromosoma as cromosoma2, sum(distinct(correlazione)) as peso
                    FROM gene g1, gene g2, interazione i
                    WHERE g1.cromosoma != g2.cromosoma and g1.id=i.id_gene1 and g2.id = i.id_gene2
                    GROUP BY g1.cromosoma, g2.cromosoma"""
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result

