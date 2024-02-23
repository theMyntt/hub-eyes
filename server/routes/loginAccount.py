from flask import jsonify

import sqlite3
import hashlib
import os

def loginAccount(postData):
  def hashPassword(pw_text):
    sha256 = hashlib.sha256()
    sha256.update(pw_text.encode("utf-8"))
    haskHex = sha256.hexdigest()
    return haskHex

  try: 
    sqlPath = os.path.dirname(os.path.abspath(__file__)) + "/../data/sqlite.db"
    conn = sqlite3.connect(sqlPath)
    cursor = conn.cursor() 

    # return postData
    try:
      query = f"SELECT NM_USER, EM_USER FROM USER WHERE EM_USER = '{postData[0]}' AND PW_USER = '{hashPassword(postData[1])}'"
      cursor.execute(query)

      row = cursor.fetchall()
      if row:
        return jsonify(row)
      else:
        return "Usuário não encontrado"
    except:
      return "Usuário não encontrado"
    finally:
      cursor.close()
      conn.close()
  except:
    return "Erro ao conectar com o banco de dados"
