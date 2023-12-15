from django.shortcuts import render
from django.http import JsonResponse
from .models import sampleModel
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def insert_data(request):
    try:
        if request.method == 'POST':
            received_data = json.loads(request.body)
            selectedContent_value = received_data.get('selectedContent', '');
            userFeedback_value = received_data.get('userFeedback', '');
            if(selectedContent_value and userFeedback_value):
                new_entry = sampleModel(selectedContent=selectedContent_value,
                    userFeedback=userFeedback_value);
                new_entry.save()
                return JsonResponse({'message': 'Post stored successfully!'})
            else:
                return JsonResponse({'error': 'Required fields are empty'}, status=400)
        else:
            return JsonResponse({'message': 'Invalid request method'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_data(request):
    try:
        if request.method == 'GET':
            selectedContent_value = request.GET.get('selectedContent', '');
            row = sampleModel.objects.get(selectedContent=selectedContent_value)
            return JsonResponse({'result': row.result})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)