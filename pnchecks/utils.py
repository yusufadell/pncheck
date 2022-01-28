import cv2
import numpy
import tensorflow as tf

MODEL_FILE = "model.h5"
IMG_SIZE = 128

model = tf.keras.models.load_model(MODEL_FILE)


def pneumonia_check(image, IMG_SIZE=128, MODEL_FILE="model.h5"):
    """pneumonia_check: Detect pneumonia symptoms Via Ml Model Enhanced by  mathematical algorithms 
    that are trained using data (image) to replicate a decision an expert would make when provided that same information.

    :param image: ImageFile Uploaded from user
    :type image: any
    :param IMG_SIZE: Size of an image to work on with the model, defaults to 128
    :type IMG_SIZE: int, optional
    :param model: ML Model which carry out the heavy lifting, defaults to "model.h5"
    :type model: str, optional
    :return: probability of having pneumonia and a boolean value To indicate so.
    :rtype: pneumonia: int, pnemunia: bool
    """
    image = cv2.imdecode(numpy.frombuffer(
        image.read(), numpy.uint8), cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
    image = image.reshape(1, IMG_SIZE, IMG_SIZE, 1)

    pneumonia_probability = model.predict([image])[0][0]
    pneumonia = True if pneumonia_probability > 0.5 else False
    context_varaibles = {"pneumonia_probability": pneumonia_probability, "pneumonia":pneumonia}
    return context_varaibles

