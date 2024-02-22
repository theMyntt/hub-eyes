from flask import jsonify
import hashlib

import sqlite3
import os

def createAccount(postData):
  sqlPath = os.path.dirname(os.path.abspath(__file__)) + "/../data/sqlite.db"

  try:
    conn = sqlite3.connect(sqlPath)
    cursor = conn.cursor() 
  except:
    return jsonify({"message": "Erro ao conectar com o banco de dados"})

  def hashPassword(pw_text):
    sha256 = hashlib.sha256()
    sha256.update(pw_text.encode("utf-8"))
    haskHex = sha256.hexdigest()
    return haskHex

  try:
    query = f"INSERT INTO USER(NM_USER, TF_USER, EM_USER, PW_USER) VALUES ('{postData[0]}', '{postData[1]}', '{postData[2]}', '{hashPassword(postData[3])}')"
    cursor.execute(query)

    conn.commit()
    conn.close()
    return jsonify({"message": "Usuário cadastrado"})
  except:
    return jsonify({"message": "Erro ao inserir"})