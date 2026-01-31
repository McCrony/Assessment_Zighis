from app import app
import traceback

with app.test_client() as c:
    try:
        r = c.get('/login')
        print('LOGIN:', r.status_code, len(r.data))
    except Exception:
        traceback.print_exc()
    try:
        r2 = c.get('/students')
        print('STUDENTS:', r2.status_code, len(r2.data))
    except Exception:
        traceback.print_exc()
