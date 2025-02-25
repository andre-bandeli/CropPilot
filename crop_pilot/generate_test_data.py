from django.core.management.base import BaseCommand
import random
from routes.models import Location

class Command(BaseCommand):
    help = "Gera pontos geográficos aleatórios para simulação"

    def handle(self, *args, **kwargs):

        min_lat, max_lat = -29.7, -29.5
        min_lon, max_lon = -53.8, -53.6

        for i in range(50):
            lat = random.uniform(min_lat, max_lat)
            lon = random.uniform(min_lon, max_lon)
            Location.objects.create(name=f"Ponto {i+1}", latitude=lat, longitude=lon)

        self.stdout.write("50 pontos criados com sucesso!")