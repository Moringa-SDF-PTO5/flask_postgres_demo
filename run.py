from app import create_app

app = create_app()

if __name__ == '__main__':
    # environment = current_app.config('APP_ENV')
    # is_debug = True
    # if environment == 'production':
    #     is_debug = False
    app.run(host='0.0.0.0',debug=True)
