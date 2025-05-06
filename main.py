from flask import Flask, request, render_template
import datetime, os
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True # Good for development


logins ={
    'kelvin': {'email': 'k@m.com', 'password': '1234'},
    'a': {'email': 'a1@a1.com', 'password': 'a1'},
    'cida':   {'email': 'tia@cida.com', 'password': '123'},
    'jean':   {'email': 'jebz@jean.com', 'password': 'jebz'},
    'xisto':   {'email': 'xisto@cogu.com', 'password': 'galego'},
    'taigo':   {'email': 'taigo@fefa.com', 'password': 'salgado'},
    'patrice':   {'email': 's@2.com', 'password': 'juju'}
    
}
#logs   

#def get_page(filename):
"""
    Reads and returns the content of a file specified by the filename.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        str: The content of the file as a string.
   redudante com render_template
   
"""

  #  with open(filename, encoding="utf-8") as f: # Specify UTF-8 encoding here
 #       return f.read()


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    #ge the time
    now = datetime.datetime.now()
    current_time_str = now.strftime(" %d/%m/%Y %H:%M") 


    if username in logins and logins[username]['password'] == password:
        return render_template('oi.html',
                                        title = 'sucesso',
                                        namepage= username,
                                        usermail = logins[username]['email'],    
                                        # Format for just date ,
                                        date = current_time_str)
    else:
        return render_template('erro.html', title='Erro de Login', message="Usuário ou senha inválidos.")
 
@app.route('/')
def  index():
    
    return render_template('index.html', title = 'Login de usuário')





# This is the standard Python way to check if the script is being run directly
# If it is, then it starts the Flask development server
# --- Standard Run Settings ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable
    app.run(host="0.0.0.0", port=port)  # Listen on 0.0.0.0 and use the specified port

  # You can change 81 to 5000 if you prefer, or remove host and port arguments entirely.
