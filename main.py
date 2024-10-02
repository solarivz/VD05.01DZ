from flask import Flask, render_template

app = Flask(__name__)

# Маршрут для главной страницы
@app.route('/')
def index():
    context = {
        "caption": "Физкультурная зарядка",
        "user": "Иван",
        "number": 1,
        "list": ["Nina", "Karina", "Anton", "Nikita"],
        "poem": [
            "Сижу за решёткой в темнице сырой.",
            "Вскормленный в неволе орёл молодой,",
            "Мой грустный товарищ, махая крылом,",
            "Кровавую пищу клюёт под окном,",
            "Клюёт, и бросает, и смотрит в окно,",
            "Как будто со мною задумал одно."]
    }


    return render_template('shablon.html', **context)

@app.route('/shablon/')
def index2():
    context = {
        "caption": "ЗАРЯДКА",
        "user": "Иван"
    }
    return render_template("index.html", **context)

# Маршрут для страницы блога
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Маршрут для страницы контактов
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=1)
