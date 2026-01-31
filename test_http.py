import requests

# Test the Flask app endpoints
base_url = 'http://127.0.0.1:5000'

# Test login page
try:
    response = requests.get(f'{base_url}/login')
    print(f'Login page: {response.status_code}')
except Exception as e:
    print(f'Login page error: {e}')

# Test students page (should be 403 without login)
try:
    response = requests.get(f'{base_url}/students')
    print(f'Students page: {response.status_code}')
except Exception as e:
    print(f'Students page error: {e}')

# Test assessments page (should be 403 without login)
try:
    response = requests.get(f'{base_url}/assessments')
    print(f'Assessments page: {response.status_code}')
except Exception as e:
    print(f'Assessments page error: {e}')

# Test dashboard (should redirect to login)
try:
    response = requests.get(f'{base_url}/dashboard')
    print(f'Dashboard: {response.status_code}')
except Exception as e:
    print(f'Dashboard error: {e}')

print('HTTP tests completed')