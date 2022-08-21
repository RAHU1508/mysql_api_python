from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/testfun')
def test():
    get_name = request.args.get('get_name')
    get_mob = request.args.get('mob')
    return 'This is my first function for get {} {}'.format(get_name, get_mob)

if __name__=="__main__":
    app.run(port=5002)