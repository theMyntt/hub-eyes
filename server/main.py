from flask import Flask, request, jsonify
from routes.createAccount import createAccount

app = Flask(__name__)

@app.route("/api/account/create", methods=["POST"])
def create():
  if request.method == "POST":
    post = request.get_json()
    postData = [
      post.get("NM_USER"), 
      post.get("TF_USER"), 
      post.get("EM_USER"),
      post.get("PW_USER")
    ]
    return createAccount(postData)
  else:
    return jsonify({"message": "Method not allowed"})

if __name__ == "__main__":
  app.run(debug=True)