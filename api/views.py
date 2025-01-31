from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def Get_info(request):
    try:
        email = "claraojobo@gmail.com"
        current_datetime = datetime.utcnow().isoformat() + 'Z'  
        github_url = "https://github.com/cleoivvy/stage_zero.git"
      
        data = {
            'email': email,
            'current_datetime': current_datetime,
            'github_url': github_url
        }
        return JsonResponse(data, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


