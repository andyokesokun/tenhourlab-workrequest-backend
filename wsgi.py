from application import createApp

app = createApp()

print("DATABASE URL", app.config["SQLALCHEMY_DATABASE_URI"])

if __name__ == "__main__":
    app.run()