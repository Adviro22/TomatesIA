// Función para mostrar la vista previa de la imagen
function previewImage(event) {
    const previewContainer = document.getElementById('image-preview-container');
    const preview = document.getElementById('image-preview');
    preview.src = URL.createObjectURL(event.target.files[0]);
    previewContainer.style.display = 'block';
}

// Función para clasificar la imagen mediante AJAX
function classifyImage() {
    const form = document.getElementById('classification-form');
    const formData = new FormData(form);

    fetch('/classify_tomato', {  // Asegúrate de que la URL aquí sea correcta
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Muestra el resultado y la explicación en el contenedor de resultados
        document.getElementById('result-text').innerText = data.result;
        document.getElementById('explanation-text').innerText = data.explanation;
        document.getElementById('result-container').style.display = 'block';
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
