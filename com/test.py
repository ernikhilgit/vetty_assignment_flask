from flask import Flask,render_template,Response,abort

app = Flask(__name__)

@app.errorhandler(400)
def not_found_error():
    return render_template('400.html'),400

@app.route('/', defaults={"input_name" : "file1"})
@app.route('/<input_name>/<int:range1>/<int:range2>/')
@app.route('/<input_name>/')
def home(input_name=None, range1=None, range2=None):
    lst = [file1,file2,file3,file4]
    try:
        filename = f"src/files/{input_name}.txt"
        if input_name not in lst:
            raise FileNotFoundError
        #special case >> file4
        if input_name == "file4":
            with open(filename, 'r', encoding="utf-16") as fh:
                content = fh.read()
            return Response(content, mimetype='text/html')
        else:

            with open(filename,'r') as fh:                data = fh.readlines()
                if range1 and range2:
                    data = data[range1:(range2+1)]


            return render_template('index.html',file_name=input_name,data=data)

    except FileNotFoundError:
        return '<h1>>>> No Such File Exists <<<<br>Please Choose Between Existing Files (file1 - file4)</h1>'


if __name__ == '__main__':
    app.run(debug=True)