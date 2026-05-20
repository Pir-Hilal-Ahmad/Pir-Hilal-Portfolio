from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    if os.path.exists('index.html'):
        return send_from_directory('.', 'index.html')
    elif os.path.exists('portfolio.html'):
        return send_from_directory('.', 'portfolio.html')
    else:
        return 'index.html not found', 404

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
