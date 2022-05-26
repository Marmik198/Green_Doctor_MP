from django.shortcuts import render
from .dl_model.model import classify_image
from django.core.files.storage import FileSystemStorage
import pandas as pd

disease_info = pd.read_csv('deeplearning/disease_info.csv' , encoding='cp1252')
supplement_info = pd.read_csv('deeplearning/supplement_info.csv',encoding='cp1252')

# Create your views here.
def home(request):
    return render(request, 'deeplearning/index.html')

def engine(request):
    return render(request, 'deeplearning/engine.html')

def plant(request):
    return render(request, 'deeplearning/plant.html')

def predict(request):
    if request.method == "GET":
        return render(request, 'deeplearning/predict.html')
    if request.method == 'POST':
        # Access the input (image) stream and keep it in the Filestorage
        unploaded_file = request.FILES['myfile']
        #convert the file to bytes
        image = unploaded_file.read()
        # predict the class of the image
        result = classify_image(image)
        #Select the top three predictions according to their probabilities
        
        # top1 = [result[0][0], result[0][1], result[0][2]]
        # top2 = [result[1][0], result[1][1], result[1][2]]
        # top3 = [result[2][0], result[2][1], result[2][2]]
        
        # top1 = display_supplement_cards(result[0][0], result[0][1], result[0][2])
        top1 = display_supplement_cards(result)
        predictions = top1
        context = { 'predictions':predictions }

        # ## In addition to image classification, Let's store the predicted filecd
        # # Save the file to ./media
        fs = FileSystemStorage()
        filename = fs.save(unploaded_file.name, unploaded_file)
        uploaded_file_url = fs.url(filename)
        context['url'] = uploaded_file_url

        return render(request, 'deeplearning/predict.html', context)

# def display_supplement_cards(species, disease, probability):
def display_supplement_cards(pred):
    title = disease_info['disease_name'][pred]
    description =disease_info['description'][pred]
    prevent = disease_info['Possible Steps'][pred]
    image_url = disease_info['image_url'][pred]
    supplement_name = supplement_info['supplement_name'][pred]
    supplement_image_url = supplement_info['supplement_image'][pred]
    supplement_buy_link = supplement_info['buy_link'][pred]


    obj = {
        "title": title,
        "description": description,
        "prevent": prevent,
        "image_url": image_url,
        "supplement_name": supplement_name,
        "supplement_image_url": supplement_image_url,
        "supplement_buy_link": supplement_buy_link,
    }

    return obj



