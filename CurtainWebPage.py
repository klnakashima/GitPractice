#!usr/bin/python
from time import sleep
import subprocess as sub

from flask import (
    Flask,
    render_template,
    request,

)

curtainsOpen = TRUE

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    value = request.form.getlist('check')
    if value is 'checked':
        sub.call(['/home/pi/Curtain/open.sh'])
        curtainsOpen = TRUE
    else:
        sub.call(['/home/pi/Curtain/close.sh'])
        curtainsOpen = FALSE
    return render_template('index.html')

@app.route('/status', methods=['GET','POST'])

def setStatus():
    status = request.values['action']

    if status.lower().__contains__("close"):
        sub.call(['/home/pi/Curtain/close.sh'])
    elif status.lower().__contains__("open"):
        sub.call(['/home/pi/Curtain/open.sh'])
    elif status.lower().__contains__("off"):
        sub.call(['/home/pi/Curtain/off.sh'])
    elif status.lower().__contains__("restart"):
        sub.call(['/home/pi/Curtain/restart.sh'])

    return status


if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
