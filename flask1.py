from flask import Flask,render_template
from flask import request
from flask import jsonify
app = Flask('__name__')
@app.route('/')
def hello():
    return render_template('layout.html')

@app.route('/send',methods=['GET'])
def var():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)

    return jsonify(result=a + b)

if __name__ == '__main__':
    app.run(debug=True)
