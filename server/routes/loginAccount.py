from flask import jsonify

import sqlite3

def loginAccount(postData):
  try: 
    conn = sqlite3.connect('data/sqlite.db')
    cursor = conn.cursor() 

    # return postData
    try:
      query = f"SELECT EM_USER, PW_USER FROM USER WHERE EM_USER = '{postData[0]}' AND PW_USER = '{postData[1]}'"
      cursor.execute(query)

      row = cursor.fetchall()
      if row:
        return row
      else:
        return jsonify({"message": "Usuário não encontrado"})
    except:
      return jsonify({"message": "Usuário não encontrado"})
    finally:
      cursor.close()
      conn.close()
  except:
    return jsonify({"message": "Erro ao conectar com o banco de dados"})
