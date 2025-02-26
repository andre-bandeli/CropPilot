from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.views import APIView
from rest_framework.response import Response
from .genetic_algorithm import optimize_route
from .models import Machine 

@method_decorator(csrf_exempt, name='dispatch')
class RouteOptimizationAPI(APIView):
    def post(self, request):
        try:
            machine_id = request.data.get('machine_id')
            points = request.data.get('points', [])
            
            if not points or len(points) < 2:
                return Response({"error": "Insira pelo menos 2 pontos"}, status=400)
                
            machine = Machine.objects.get(id=machine_id)
            
            best_route = optimize_route(
                points=points,
                machine_capacity=machine.capacity_kg,
                machine_id=machine_id
            )
            
            return Response({
                "optimized_route": best_route["optimized_route"],
                "total_distance": best_route["total_distance"],
                "message": "Rota otimizada com sucesso!"
            })
            
        except Machine.DoesNotExist:
            return Response({"error": "Máquina não encontrada"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)