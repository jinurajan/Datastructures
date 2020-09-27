from flask import Flask, request, abort, jsonify, make_response

FILENAME = "banner.txt"
HEADERNAME = "admin-auth"

app = Flask(__name__)


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify(error=str(e)), 405

@app.errorhandler(406)
def not_acceptable(e):
    return jsonify(error=str(e)), 406

@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400


@app.errorhandler(403)
def forbidden(e):
    return jsonify(error=str(e)), 403


def valid_headers(headers):
    val = headers.get(HEADERNAME)
    if not val and val != "1234":
        return False
    return True


def set_headers(resp):
    try:
        with open(FILENAME, 'r') as f:
            banner = f.read()
        if banner:
            resp.headers['banner'] = banner
        return resp
    except IOError:
        return resp


def set_banner(banner):
    with open(FILENAME, 'w') as f:
        f.write(banner)



@app.route("/echo", methods=['GET'])
def echo():
    if len(request.args) > 1:
        abort(406)
    message = request.args.get("message")
    if not message:
        abort(406)
    else:
        resp = make_response(message)
        resp = set_headers(resp)
        return resp


@app.route("/set_banner", methods=['POST'])
def admin():
    if not valid_headers(request.headers):
        abort(403)
    banner = request.form.get("banner")
    if not banner:
        abort(400)
    set_banner(banner)
    return "", 200


if __name__ == '__main__':
    # do not change the ip nor the port that is used for the app
    app.run(host='127.0.0.1', port=8080, debug=True)


