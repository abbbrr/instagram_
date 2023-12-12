from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Используйте свою базу данных
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


admin = Admin(app, name='Your App', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))  # Замените YourModel на вашу модель данных


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        username = request.form['firstInput']
        password = request.form['pass']

        # Проверяем, что оба поля не пустые
        if not username or not password:
            return 'Ошибка: Оба поля должны быть заполнены.'

        # Создаем объект пользователя и добавляем его в базу данных
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return 'Данные успешно добавлены в базу данных!'

    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5005)

