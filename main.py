from app.views import app
import os

if __name__ == "__main__":
    try:
        port = int(os.environ.get('PORT', 7000))
        app.run('0.0.0.0')
        # app.run(host='localhost', port=port, threaded=True, debug=True)
    except Exception as e:
        print(e)
