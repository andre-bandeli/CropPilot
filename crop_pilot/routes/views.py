from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.views import APIView
from rest_framework.response import Response
from .genetic_algorithm import optimize_route
from .models import Location

@method_decorator(csrf_exempt, name='dispatch')
class RouteOptimizationAPI(APIView):
    def post(self, request):
        points = request.data.get('points', [])
        
        if len(points) < 2:
            return Response({"error": "Insira pelo menos 2 pontos"}, status=400)
        
        try:
            best_route = optimize_route(points)
            return Response({
                "optimized_route": best_route,
                "message": "Rota otimizada com sucesso!"
            })
        except Exception as e:
            return Response({"error": str(e)}, status=500)