from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
    return '''
        <h1>How To Process Incoming Request Data in Flask</h1>
        <a href="http://127.0.0.1:5000/query-example/?language=Python&framework=Flask&website=MyApp">Query example</a><br />
        <a href="http://127.0.0.1:5000/form-example">Form example</a><br />
        <a href="http://127.0.0.1:5000/json-example">JSON example (Method Not Allowed - Only POST)</a>
        '''


@app.route('/query-example/')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')

    # if key doesn't exist, returns a 400, bad request error
    framework = request.args['framework']

    # if key doesn't exist, returns None
    website = request.args.get('website')

    return '''
              <h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)


# http://127.0.0.1:5000/query-example/?language=Python&framework=Flask&website=MyApp


# allow both GET and POST requests
@app.route('/form-example/', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Language: <input type="text" name="language"></label></div>
               <div><label>Framework: <input type="text" name="framework"></label></div>
               <input type="submit" value="Submit">
           </form>'''


# http://127.0.0.1:5000/form-example


# GET requests will be blocked
@app.route('/json-example/', methods=['POST'])
def json_example():
    request_data = request.get_json()

    language = None
    framework = None
    python_version = None
    example = None
    boolean_test = None

    if request_data:
        if 'language' in request_data:
            language = request_data['language']

        if 'framework' in request_data:
            framework = request_data['framework']

        if 'version_info' in request_data:
            if 'python' in request_data['version_info']:
                python_version = request_data['version_info']['python']

        if 'examples' in request_data:
            if (type(request_data['examples']) == list) and (len(request_data['examples']) > 0):
                example = request_data['examples'][0]

        if 'boolean_test' in request_data:
            boolean_test = request_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)


# http://127.0.0.1:5000/json-example
# Method Not Allowed - Only POST request


''' 
PyCharm Services (next to Terminal and Run in the bottom of window)
Create POST request to http://127.0.0.1:5000/json-example

POST http://127.0.0.1:5000/json-example
Content-Type: application/json

{
    "language" : "Python",
    "framework" : "Flask",
    "website" : "Request Example with JSON",
    "version_info" : {
        "python" : "3.9.1",
        "flask" : "2.1.2"
    },
    "examples" : ["query", "form", "json"],
    "boolean_test" : true
}
'''

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
