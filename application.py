from flask import Flask

application = Flask(__name__)


@application.route("/", methods=["GET"])
def get_hello_world():
    return "olá mundo 2"


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080, debug=True)



 
