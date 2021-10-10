import os

from flask import Flask, render_template, request
from markupsafe import escape
from PIL import Image 

# 'static' from template will point to colours folder
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    print('im a print statement')
    # join/add folder where uploads will go (colours)
    target = os.path.join(APP_ROOT, 'static/images/')
    print(target)

# make sure folder exists
#if not: create it!
    if not os.path.isdir(target):
        os.mkdir(target)

# loop through the list
    for file in request.files.getlist('file'):
        print(file)
        # get the filename from the list because: getting list of objects to be uploaded
        filename = file.filename
        # tell the server to upload specific file to specific location
        destination = '/'.join([target, filename])
        print(destination)
        file.save(destination)
    return render_template('complete.html', image_name=filename)
    # image_name= display image of specific name


@app.route('/get_colours', methods=['GET'])
def get_colours():
    print('hallo')
    images = os.listdir(os.path.join(app.static_folder, 'images'))
    return render_template('display_image.html', images=images)

@app.route('/get_colour/<colour>')
def get_colour(colour):
    print('hallo')
    print(colour)
    images = os.listdir(os.path.join(app.static_folder, 'images'))
    return render_template('display_image.html', images=images)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/colour/<colour>')
def show_colour(colour):
    # show the user profile for that user
    with Image.open(os.path.join(app.static_folder, 'images') + '/' + '2E98D3.png') as im:
        im.show()
    return f'User {escape(colour)}'

if __name__ == '__main__':
    app.run(debug=True)
    