from app.views import app
import os

if __name__ == "__main__":
    try:
        port = int(os.environ.get('PORT', 7000))
        # app.run(host='0.0.0.0', port=port, threaded=True, debug=True)
        app.run(host='localhost', port=port, threaded=True, debug=True)
    except Exception as e:
        print(e)
