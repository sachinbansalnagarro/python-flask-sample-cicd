from flask import Flask
import socket    

app = Flask(__name__)

@app.route("/")
def index():
  hostname = socket.gethostname()    
  IPAddr = socket.gethostbyname(hostname)    
  return "Your Computer Name is: " + hostname + ". Your Computer IP Address is: "+ IPAddr
  
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')