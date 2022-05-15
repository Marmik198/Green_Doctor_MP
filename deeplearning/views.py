from django.shortcuts import render
from .dl_model.model import classify_image
from django.core.files.storage import FileSystemStorage

disease_supplement_mapping = {    
    "Apple": {
        "Apple_scab": {
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "Black_rot": {
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "Cedar_apple_rust" : {
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "healthy":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
    },
    "Blueberry": {
        "healthy":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
    },
    "Cherry_(including_sour)": {
        "Powdery_mildew":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "healthy":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
    },
    "Corn_(maize)": {
        "Cercospora_leaf_spot Gray_leaf_spot":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "Common_rust":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "Northern_Leaf_Blight":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "healthy":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
    },
    "Grape": {
        "Black_rot":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "Esca_(Black_Measles)":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "Leaf_blight_(Isariopsis_Leaf_Spot)":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "healthy":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
    },
    "Orange": {
        "Haunglongbing_(Citrus_greening)":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
    },
    "Peach": {
        "Bacterial_spot":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "healthy":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
    },
    "Pepper": {
        "Bacterial_spot":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "healthy":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
    },
    "Potato": {
        "Early_blight":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "Late_blight":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "healthy":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
    },
    "Raspberry": {
        "healthy":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
    },
    "Soybean": {
        "healthy":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
    },
    "Squash": {
        "Powdery_mildew":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
    },
    "Strawberry": {
        "Leaf_scorch":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "healthy":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
    },
    "Tomato": {
        "Bacterial_spot":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "Early_blight":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "Late_blight":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "Leaf_Mold":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "Septoria_leaf_spot":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "Spider_mites Two-spotted_spider_mite":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "Target_Spot":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "Tomato_Yellow_Leaf_Curl_Virus":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "Tomato_mosaic_virus":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
        "healthy":{
            "title": "Apple Scab",
            "description": "Lorem Ipsum",
            "supplement_photo": "ASD"
        },
    }
}

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
        
        top1 = display_supplement_cards(result[0][0], result[0][1], result[0][2])
        top2 = display_supplement_cards(result[1][0], result[1][1], result[1][2])
        top3 = display_supplement_cards(result[2][0], result[2][1], result[2][2])

        predictions = [ top1, top2, top3 ]
        context = { 'predictions':predictions }

        # ## In addition to image classification, Let's store the predicted filecd
        # # Save the file to ./media
        fs = FileSystemStorage()
        filename = fs.save(unploaded_file.name, unploaded_file)
        uploaded_file_url = fs.url(filename)
        context['url'] = uploaded_file_url

        return render(request, 'deeplearning/predict.html', context)

def display_supplement_cards(species, disease, probability):
    title = disease_supplement_mapping[species][disease]["title"]
    description = disease_supplement_mapping[species][disease]["description"]
    image_url = disease_supplement_mapping[species][disease]["supplement_photo"]

    return [title, description, image_url]



