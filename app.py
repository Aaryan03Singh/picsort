from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import cv2 
import tensorflow as tf
import numpy as np
from  werkzeug.utils import secure_filename
import os


app = Flask(__name__)

doc_dic = {0 : 'Document', 1 : 'Pictures'}
people_dic = {0 : 'Person', 1 : 'Scenery'}

model_doc = load_model('models/pictures_documents.h5')
model_people = load_model('models/scene_people.h5')


def predict_label(img_path):
	i = cv2.imread(img_path)
	i = tf.image.resize(i,(256,256))
	i = np.expand_dims(i/255,0)
	d = model_doc.predict(i).round()
	if d[0][0] ==0:
		return doc_dic[d[0][0]]
	else:
		p = model_people.predict(i).round()
		if p[0][0]==0:
			return people_dic[p[0][0]]
		else:
			return people_dic[p[0][0]]
	


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "Please subscribe  Artificial Intelligence Hub..!!!"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']
		img_path = "static/" + img.filename
		img.save(img_path)
		
		p = predict_label(img_path)
	return render_template("index.html", prediction = p, img_path = img_path)

# @app.route("/submit", methods=['GET','POST'])
# def get_output():
# 	if request.method == 'POST':

# 		img = request.files.getlist('my_images[]')
# 		predictions = []
# 		img_paths = []
		
# 		for i in img:
# 			img_path = "static/" + i.filename
# 			img.save(img_path)

# 			p = predict_label(i)
# 			predictions.append(p)
# 			img_paths.append(img_path)
			
# 		return render_template("index.html",predictions=predictions,img_paths=img_paths)




if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)