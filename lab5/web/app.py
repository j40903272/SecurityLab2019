from flask import Flask, request, redirect, session, render_template
from urllib.parse import urlencode
import requests
app = Flask(__name__)
app.config["SECRET_KEY"] = "fuck you"

@app.route("/login")
def index():
    params = {"client_id":"579a345bae9d858d03ae", "redirect_url":"http:/127.0.0.1:5000/callback", "scope":"repo"}
    link = "https://github.com/login/oauth/authorize?" + urlencode(params)
    return "<a href=%s>Login</a>" % link

@app.route("/callback", methods=["POST", "GET"])
def callback():
    url = "https://github.com/login/oauth/access_token"
    code = request.args["code"]
    params = {"client_id":"579a345bae9d858d03ae", "client_secret":"f18b55959d58c59bcdc27ea9b113243f163caeff", "code":request.args["code"]}
    headers = {"Accept": "application/json"}
    res = requests.post(url, params=params, headers=headers).json()
    session["access_token"] = res["access_token"]
    return redirect("/show")
    
    
@app.route("/show")
def show():
    headers = {"Authorization":"token {}".format(session["access_token"])}
    res = requests.get("https://api.github.com/user/repos", headers=headers, params={'per_page':100}).json()
    repos = [repo["full_name"] for repo in res]
    print(len(repos))
    return "<br>".join(repos)

if __name__ == "__main__":
    app.run()