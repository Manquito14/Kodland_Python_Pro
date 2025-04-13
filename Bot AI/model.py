from keras.models import load_model
from PIL import Image
import numpy as np
def get_class(model_path, labels_path, image_path):
    model = load_model(model_path)
    
    # Cargar y preparar imagen
    img = Image.open(image_path).resize((224, 224))
    img_array = np.asarray(img).astype(np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Cargar etiquetas
    with open(labels_path, "r") as f:
        labels = f.read().splitlines()
    
    predictions = model.predict(img_array)
    class_index = np.argmax(predictions[0])
    return f"Predicción: {labels[class_index]} ({predictions[0][class_index]*100:.2f}%)"
