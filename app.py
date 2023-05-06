from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cmd = ''
        if request.form['submit'] == 'Ping':
            domain = request.form['domain']
            count = request.form['count']
            size = request.form['size']
            ttl = request.form['ttl']
            cmd = f"ping -c {count} -s {size} -t {ttl} {domain}"
        elif request.form['submit'] == 'Tracert':
            domain = request.form['domain']
            cmd = f"traceroute {domain}"
        elif request.form['submit'] == 'Whois':
            domain = request.form['domain']
            cmd = f"whois {domain}"
        output = os.popen(cmd).read()
        return render_template('index.html', output=output)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
