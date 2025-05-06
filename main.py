from flask import Flask, request
import datetime, os
app = Flask(__name__)

logins ={
    'kelvin': {'email': 'k@m.com', 'password': '1234'},
    'a': {'email': 'a1@a1.com', 'password': 'a1'},
    'cida':   {'email': 'tia@cida.com', 'password': '123'},
    'jean':   {'email': 'jebz@jean.com', 'password': 'jebz'},
    'xisto':   {'email': 'xisto@cogu.com', 'password': 'galego'}
}
#logs

def get_page(filename):
    """
    Reads and returns the content of a file specified by the filename.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        str: The content of the file as a string.
    """

    with open(filename, encoding="utf-8") as f: # Specify UTF-8 encoding here
        return f.read()


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    #ge the time
    now = datetime.datetime.now()
    current_time_str = now.strftime(" %d/%m/%Y %H:%M") 


    if username in logins and logins[username]['password'] == password:
        page = get_page('templates/oi.html')
        page = page.replace('{namepage}', username)
        page = page.replace('{usermail}', logins[username]['email'])    
  # Format for just date 
        page = page.replace('{date}', current_time_str)
        return page
    else:
        return 'sai daqui, não te conheço'

@app.route('/')
def  index():
    page = f'''
    <!DOCTYPE html>
    <html>

    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>replit</title>
    <link href="/staticstyle.css" rel="stylesheet" type="text/css" />
    </head>

    <body>
    <form method="post" action="/login">
        <p> Usuario : <input type="text" name = "username" required></p>
        <p> Senha : <input type="password" name = "password"  required></p>
        <p>Email:<input type="email"  name = "email"  required></p>
        <button type="submit" >Login</button>
    </form>

    </body>

    </html>'''
    return page





# This is the standard Python way to check if the script is being run directly
# If it is, then it starts the Flask development server
# --- Standard Run Settings ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable
    app.run(host="0.0.0.0", port=port)  # Listen on 0.0.0.0 and use the specified port

  # You can change 81 to 5000 if you prefer, or remove host and port arguments entirely.
