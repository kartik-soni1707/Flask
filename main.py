from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sum', methods=['POST'])
def sum():
    res=0
    for x in (request.form.values()):
        res+=int(x)
    return render_template('index.html', res=res)
if __name__=="__main__":

    app.run(debug=True)
