from flask import Flask,render_template,request,jsonify
from rag_engine import get_rag_answer

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask",methods=["POST"])
def ask():
    msg=request.json["message"]
    reply=get_rag_answer(msg)
    return jsonify({"reply":reply})

if __name__=="__main__":
    app.run(debug=True)
