import sqlite3

def createAccount(postData):
  # conn = sqlite3.connect('accounts.db')
  # cursor = conn.cursor()

  # query = f"INSERT INTO USER(NM_USER, TF_USER, EM_USER, PW_USER) VALUES ({postData[0]}, {postData[1]}, {postData[2], {postData[3]}})"
  # cursor.execute(query)
  
  # conn.commit()
  # conn.close()
  return postData