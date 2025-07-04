# run.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    # Advanced: listen on all interfaces for Docker, default Flask port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)

