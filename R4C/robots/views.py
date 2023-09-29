import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Robot
from datetime import datetime


@method_decorator(csrf_exempt, name='dispatch')
class RobotAPIView(View):
    def post(self, request):
        try:
            # Парсинг входных данных
            data = json.loads(request.body)
            serial = data.get('serial')
            model = data.get('model')
            version = data.get('version')
            created = datetime.strptime(data.get('created'), '%Y-%m-%d %H:%M:%S')

            # Проверка на существование модели
            if not Robot.objects.filter(model=model).exists():
                return JsonResponse({'error': 'Invalid model.'}, status=400)


            # Проверка на валидность данных
            if len(serial) > 5 or len(model) > 2 or len(version) > 2:
                return JsonResponse({'error': 'Invalid data. Exceeded maximum length.'}, status=400)


            robot = Robot.objects.create(serial=serial, model=model, version=version, created=created)
            robot.save()

            return JsonResponse({'message': 'Robot information saved successfully.'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)