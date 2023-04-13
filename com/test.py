from flask import Flask,render_template,Response,abort

app = Flask(__name__)

@app.errorhandler(404)
def error404(error):
    return '<br><h2>Invalide Input Given..!</h2><br><h4>Check For Range Values You Entered..!</h4><br><p>Enter Both Range Values or Ignore Both..!</p>'
@app.errorhandler(400)
def not_found_error(error):
    return render_template('400.html')



@app.route('/', defaults={"input_name" : "file1"})
@app.route('/<input_name>/<int:range1>/<int:range2>/')
@app.route('/<input_name>/')
def home(input_name=None, range1=None, range2=None):
    try:
        filename = f"src/files/{input_name}.txt"

        #special case >> file4
        if input_name == "file4":
            with open(filename, 'r', encoding="utf-16") as fh:
                content = fh.read()
            return Response(content, mimetype='text/html')
        else:
            with open(filename,'r') as fh:
                data = fh.readlines()
                if range1 and range2:
                    if range1 >= range2:
                        raise ValueError
                    data = data[range1:(range2+1)]
            return render_template('index.html',file_name=input_name,data=data)

    except FileNotFoundError:
        return '<h2>>>> No Such File Exists <<<</h2><br><p>Please Choose Between Existing Files (file1 - file4)..!<p>'
    except ValueError:
        return '<h2>Invalide Range Given...!!</h2><br><p>Check Your Range Values..!</p>'

if __name__ == '__main__':
    app.run(debug=True)
