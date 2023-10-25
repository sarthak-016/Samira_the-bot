import json

def greet_user(request):
    # Extract the user's name from the request JSON data
    request_json = request.get_json()
    user_name = request_json["queryResult"]["parameters"]["Name"]

    # Construct the response
    response = {
        "fulfillmentText": f"Hello {user_name}, how can I help you?"
    }

    # Return the response in JSON format
    return json.dumps(response)

# The main entry point for the webhook
def main(request):
    if request.method == "POST":
        return greet_user(request)
    else:
        return "Invalid request method"

# For local testing
if __name__ == "__main__":
    import flask
    app = flask.Flask(__name__)

    @app.route("/", methods=["POST"])
    def test_webhook():
        return greet_user(flask.request)

    app.run(host="0.0.0.0", port=8080)
