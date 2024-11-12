from flask import Blueprint, render_template, request, jsonify
from ultralytics import YOLO
from PIL import Image

detection_bp = Blueprint('detection', __name__, template_folder='templates', static_folder='static')

# Carga el modelo `tomates.pt` con YOLO
model = YOLO('modelos/tomates.pt')  # Asegúrate de que la ruta sea correcta

@detection_bp.route('/detection')
def detection():
    return render_template('detection.html')

@detection_bp.route('/classify_tomato', methods=['POST'])
def classify_tomato():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    image_file = request.files['image']
    image = Image.open(image_file)

    # Realiza la predicción
    results = model.predict(source=image, save=False)
    
    # Extrae la clase predicha (0 o 1)
    predicted_class = int(results[0].boxes.cls[0].item())

    # Determina el resultado y la explicación
    if predicted_class == 0:
        result = "Tomate Verde"
        explanation = "El tomate está en un estado inmaduro y tiene un color verde. Esto indica que no está listo para el consumo."
    elif predicted_class == 1:
        result = "Tomate Rojo"
        explanation = "El tomate está en un estado maduro y tiene un color rojo, lo cual es ideal para el consumo."
    else:
        result = "Clasificación desconocida"
        explanation = "No se pudo determinar si el tomate es rojo o verde."

    return jsonify({"result": result, "explanation": explanation})
