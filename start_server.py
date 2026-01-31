from app import app
import time
import traceback

if __name__ == '__main__':
    print("Starting Flask server...")
    try:
        print("App imported successfully")
        print(f"App debug mode: {app.debug}")
        print(f"App config DEBUG: {app.config.get('DEBUG', 'Not set')}")
        print("Calling app.run()...")
        app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
    except Exception as e:
        print(f"Error starting server: {e}")
        traceback.print_exc()