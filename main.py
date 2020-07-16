from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
from keras.models import load_model
import cv2
import numpy as np
from PIL import Image
app=Flask(__name__)
UPLOAD_FOLDER = '/media/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/pred', methods=['POST'])
def pred():
    file = request.files['file']
    filename = secure_filename(file.filename)
    # file.save(('data.jpg'))
    model = load_model('facefeatures_new_model.h5')
    
    #face = Image.open("wow.jpg")
    #face = cv2.resize(np.float32(face), (224, 224))
    #im = Image.fromarray(face, 'RGB')
    # Resizing into 128x128 because we trained the model with this image size.
    #img_array = np.array(im)
    # Our keras model used a 4D tensor, (images x height x width x channel)
    # So changing dimension 128x128x3 into 1x128x128x3
    #img_array = np.expand_dims(img_array, axis=0)
    #pred = model.predict(img_array)
    #if(pred[0][1]==1):
    #    name="On"
    #else:
    #    name="Off"

    return render_template('index.html', res=" ")
if __name__=="__main__":

    app.run(debug=True)
