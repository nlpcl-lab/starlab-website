class Config:
    SECRET_KEY = 'YOUR_SECRET_KEY'
    ENCRYPTION_KEY = 'YOUR_ENCRYPTION_KEY'
    MONGODB_SETTINGS = {
        'host': '127.0.0.1',
        'db': 'YOUR_DB_NAME',
        'port': 27017,
        'username': 'YOUR_DB_USERNAME',
        'password': 'YOUR_DB_PASSWORD',
    }

    DEPLOY_HOSTS = ['admin@example.com:22']
    DEPLOY_PASSWORDS = {'admin@example.com:22': 'password'}
