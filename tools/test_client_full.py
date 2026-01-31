from app import app
import traceback

# Use testing config and disable CSRF for form submissions
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False

endpoints = [
    ('GET', '/'),
    ('GET', '/login'),
    ('POST', '/login', {'username': app.config.get('DEFAULT_ADMIN_USERNAME','admin'), 'password': app.config.get('DEFAULT_ADMIN_PASSWORD','Admin@123')}),
    ('GET', '/students'),
    ('GET', '/students/new'),
    ('GET', '/assessments'),
    ('GET', '/assessments/new'),
    ('GET', '/teacher/questions/bulk_import'),
    ('GET', '/student/login'),
    ('GET', '/student/dashboard')
]

with app.test_client() as c:
    for ep in endpoints:
        try:
            method = ep[0]
            path = ep[1]
            if method == 'GET':
                resp = c.get(path)
            elif method == 'POST':
                data = ep[2] if len(ep) > 2 else {}
                resp = c.post(path, data=data, follow_redirects=True)
            else:
                continue

            print(f"{method} {path} -> {resp.status_code} (len={len(resp.data)})")

        except Exception:
            print(f"ERROR while requesting {ep}")
            traceback.print_exc()

print('\nTest client run complete')
