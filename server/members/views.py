from django.shortcuts import render, loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ImageForm
import tensorflow as tf
from PIL import Image
import numpy as np

IMAGE_SIZE = 256

def api(request):
    if request.method == "GET":
        form = ImageForm()
        return render(request, "index.html", {"form": form})

@csrf_exempt
def predict(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        potato_classes = ['Early Blight', 'Healthy', 'Late Blight']
        if form.is_valid():
            model = tf.keras.models.load_model("/models/potato_model")
            image_file = request.FILES['image']
            image = Image.open(image_file)
            image = image.resize((IMAGE_SIZE, IMAGE_SIZE))
            image = np.array(image)
            batch = np.array([image])
            predictions = model.predict(batch)
            return JsonResponse({"message": f"The potato plant looks as {potato_classes[np.argmax(predictions)]}"})
        else:
            return JsonResponse({"message": "Form Value Invalid"})
