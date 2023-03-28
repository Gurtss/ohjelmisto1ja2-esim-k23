import json
from flask import Flask, request, Response

app = Flask(__name__)

# create db connection here if needed

# create functions for db queries
def get_data_from_db():
    pass

@app.route('/kukkuu')
def say_hello():
    args = request.args
    print(args)
    to_whom = args.get("to")
    from_who = args.get("from")
    # response in html format
    #return f"<h1>No morjes {toWhom}! <br> t. {fromWho}</h1>"
    # response in json format
    return {
        "kenelle": to_whom,
        "kuka": from_who,
        "tervehdys": f"No morjes {to_whom}! t. {from_who}"
    }

# toinen tapa
@app.route('/kukkuu/<from_who>/<to_whom>')
def say_hello_v2(from_who, to_whom):
    # response in html format
    return f"<h1>No morjes {to_whom}! <br> t. {from_who}</h1>"

# virheenkäsittely
@app.route('/sum/<num1>/<num2>')
def calculate_sum(num1, num2):
    try:
        sum = float(num1) + float(num2)
        response = {"sum": sum}
        return response
    except ValueError:
        response = {"message": "Bad request"}
        # Muotoillaan Response-olio itse ennen palauttamista
        response_json = json.dumps(response)
        return Response(response=response_json, status=400, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(status):
    res = {"status": "404", "message": "Not found"}
    res_json = json.dumps(res)
    return Response(response=res_json, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
