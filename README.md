# Requirement  

The widespread use of smartphones and sophisticated camera equipment in the modern digital era has created a  trend toward constant photographing. People are taking more photos than ever before, people are explanding the range of their lens to perosnal photos and beautiful landscapes. Selfies have evolved into a self-expression tool that people use to manage their online persona. The urge to take pictures goes beyond mere aesthetics, as people frequently take pictures of important documents, invoices, and other items to instantly digitize and organize them. The increase of  photos has also increased the need of organization. People's galleries are filled to the brim with photos which need to be organized.

# Features 
PicSort classifies and helps organize pictures. It will accpet any sort of image and classify it into
* people
* documents 
* scenery
People have a abundant of photos and we can sort them on the categories mentioned before.

# Future Prospects
This is just a prototype that classifies the images in the future we plan to-
* make it such that one can input a folder of images which will get sorted according to the categories and the sorted folders can be directly downloaded.
* input blurred images which will be rectified
* cluster images of the same people together

# How we built it 

### Step 1- Import the neccesary libraries
Libraries include-
* Tensorflow
* Numpy
* Matplotlib
* cv2
* os

### Step 2- Gather the training data
Training data was gathered from google images. Around 2500 images have been used for the training.

### Step 3- Preprocess the data
* Filtering out the invalid images. Only keeping png,jpeg,jpg,bmp images
* Reading the images with tensorflow utils as a array of 256,256 pixels
* Scaling the data by dividing it by 255
* Spliting the data into train,validation and test

### Step 4- Creating the Model
* We are using a CNN image classification model using tensorflow
* The model contains 3 convolution layers and 1 dense layer
* The model is using adam optimizier with loss binary_enthrophy
* The model was trained with around 62 batchs of images with each batch having 32 images
* Total of 20 epochs was used for the training process

### Step 5- Integration of OneAPI
* Without the optimization of the GPUs by oneAPI the training process would have taken a lot of time. We have around 3000 images to train and 3million parameters in the CNN model. Training will take around 6-7 min.
* Using The oneDNN toolkit the training time becomes significantly lower
* We used the Intel Developer Clouds Jupyter Notebook for training the model with the Intel Optimizations

![intel](https://user-images.githubusercontent.com/72274851/218504609-585bcebe-5101-4477-bdd2-3a1ba13a64a8.png)

![1](https://i.ibb.co/9WgYGbY/inteldnn.jpg)

### Step 6- Saving the Models
* The models were saved as a .h5 file which we use later in the flask application

### Step 7-Deployment
* We have deployed the model using flask
* The frontend was made using html,css and js
  











# Preview of the appliction

![image](https://i.ibb.co/F3bh2Sp/Pic-Sort-homepage.png)
