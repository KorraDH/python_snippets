import pyodbc

def test_sqlserver_connection(server_name, database_name, username, password):
  """
  Funzione per testare una connessione a un database SQL Server.

  Args:
      server_name (str): Nome del server SQL Server.
      database_name (str): Nome del database SQL Server.
      username (str): Username per l'autenticazione al database.
      password (str): Password per l'autenticazione al database.

  Returns:
      bool: True se la connessione è stata stabilita correttamente, False altrimenti.
  """

  try:
    connection_string = f"Driver={driver};Server={server_name};Database={database_name};Uid={username};Pwd={password}"
    with pyodbc.connect(connection_string) as connection:
      cursor = connection.cursor()
      cursor.execute("SELECT 1")
      cursor.close()
      return True
  except pyodbc.Error as e:
    print(f"Errore durante la connessione al database: {e}")
    return False

# Esempio di utilizzo

driver = "ODBC Driver 17 for SQL Server"
server_name = "192.168.2.49\SQLEXPRESS"
database_name = "UnicoM6_DEMO"
username = "Erp"
password = "!Erp23"

'''
driver = "ODBC Driver 17 for SQL Server"
server_name = "192.168.227.233\SQLEXPRESS"
database_name = "Bertolini"
username = "Erp"
password = "!Erp23"
'''

if test_sqlserver_connection(server_name, database_name, username, password):
  print("Connessione al database stabilita correttamente!")
else:
  print("Errore durante la connessione al database.")
