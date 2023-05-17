import mysql.connector

def conectar():
  mydb = mysql.connector.connect(
    host="44.197.187.241",
    user="admin",
    password="aula",
    database="africa"
  )
  return mydb
  try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")
conn.close()
