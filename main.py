from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'INFORMATION_SECURITY'


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo_func():
    if request.method == 'GET':
        if os.access('static/img/img.jpg', os.R_OK):
            img = 'img.png'

            return render_template('select_photo_viewer.html', img=img)
        else:
            return render_template('select_photo.html')
    elif request.method == 'POST':
        file = request.files['file']

        new_file = open('static/img/img.jpg', mode='wb')
        new_file.write(file.read())
        new_file.close()

        return "Форма отправлена"


def main():
    app.run(
        host='127.0.0.1',
        port=8080
    )


if __name__ == '__main__':
    main()
