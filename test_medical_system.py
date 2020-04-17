from test_medical_system import app

if __name__ == '__main__':
    app.run(ssl_context=('domain-crt.pem', 'domain-key.pem'))
