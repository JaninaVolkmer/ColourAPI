import os
from os.path import exists
from flask import Flask, render_template, request


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
    target = os.path.join(APP_ROOT, 'static/images')
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


# gettting list of colours
@app.route('/listcolours', methods=['GET'])
def listcolours():
    images = os.listdir('./static/images') # path
    print(images)
    return render_template('display_image.html', images=images)


# display a single colour with Hex endpoint
@app.route('/colour/<colour>')
def show_colour(colour):
    # show the user profile for that user
    allhex = []
    filename = os.path.join(APP_ROOT, 'static/images') + '/' + colour + '.png'
    single_file = '/static/images' + '/' + colour + '.png'
    print(single_file)
    allhex.append(single_file)
    print(filename)
    file_exists = exists(filename)
    if not file_exists:
        print('file does not exist' + filename)
        return "Does not exist"
    return render_template('allhex.html', allhex=allhex)


if __name__ == '__main__':
    app.run(debug=True)
