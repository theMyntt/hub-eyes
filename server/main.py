from flask import Flask, request, jsonify
from routes.createAccount import createAccount
from routes.loginAccount import loginAccount
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/account/create", methods=["POST"])
def create():
  if request.method == "POST":
    try:
      post = request.get_json()

      postData = [
        post.get("NM_USER"), 
        post.get("TF_USER"), 
        post.get("EM_USER"),
        post.get("PW_USER")
      ]
      
      return createAccount(postData)
    except:
      return jsonify({"message": "Erro interno"})
  else:
    return jsonify({"message": "Method not allowed"})
  
@app.route("/api/account/login", methods=["POST"])
def login():
  if request.method == "POST":
    try:
      post = request.get_json()

      postData = [ 
        post.get("EM_USER"),
        post.get("PW_USER")
      ]
      
      # return postData

      return loginAccount(postData)
    except:
      return jsonify({"message": "Erro ao fazer login"})
  else:
    return jsonify({"message": "Method not allowed"})

if __name__ == "__main__":
  app.run(debug=True)