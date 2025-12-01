from database.DB_connect import DBConnect
from model.spedizione import Spedizione
from model.hub import Hub
from model.compagnia import Compagnia

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO

    @staticmethod
    def get_spedizioni():

        cnx= DBConnect.get_connection()

        result = []
        if cnx is None:
            print("Errore di connessione al database.")
            return None


        cursor = cnx.cursor()
        query = """ SELECT
                    LEAST(id_hub_origine, id_hub_destinazione) AS hub1,
                    GREATEST(id_hub_origine, id_hub_destinazione) AS hub2,
                    AVG(valore_merce) AS peso_arco
                    FROM spedizione
                    GROUP BY
                    LEAST(id_hub_origine, id_hub_destinazione),
                    GREATEST(id_hub_origine, id_hub_destinazione); """
        try:
            cursor.execute(query)
            for row in cursor:
                spedizione = (row[0], row[1], float(row[2]))
                result.append(spedizione)

        except Exception as e:
            print(f"Errore durante la query get_tour: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result

    @staticmethod
    def get_hub():
        cnx = DBConnect.get_connection()

        result = {}
        if cnx is None:
            print("Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT * FROM hub """
        try:
            cursor.execute(query)
            for row in cursor:
                hub = Hub( id= row['id'],
                            codice=row['codice'],
                            nome=row['nome'],
                            citta=row['citta'],
                            stato=row['stato'],
                            latitudine=row['latitudine'],
                            longitudine=row['longitudine'])
                result[hub.id]=hub.nome

        except Exception as e:
            print(f"Errore durante la query get_tour: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result

    @staticmethod
    def get_compagnie():
        cnx = DBConnect.get_connection()

        result = []
        if cnx is None:
            print("Errore di connessione al database.")
            return None

        cursor = cnx.cursor()
        query = """ SELECT * FROM compagnia """
        try:
            cursor.execute(query)
            for row in cursor:
                compagnia = Compagnia(*row)
                result.append(compagnia)

        except Exception as e:
            print(f"Errore durante la query get_tour: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result





