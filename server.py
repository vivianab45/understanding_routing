from flask import Flask
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello():
    return "Hello World!"  # Return the string 'Hello World!' as a response

@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')          # The "@" decorator associates this route with the function immediately following
def say(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<string:word>') 
def repeat_word(num, word):
    output=''

    for i in range(0,num):
        output += f'<p>{word}<p>'
    return output

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
