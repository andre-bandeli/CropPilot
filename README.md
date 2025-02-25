# CropPilot 🌾  
**Otimização de Rotas Agrícolas com Algoritmos Genéticos**  

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)  
[![Django](https://img.shields.io/badge/Django-4.2-brightgreen)](https://www.djangoproject.com/)  


---

## 📌 Problema  
Planejar rotas eficientes para máquinas agrícolas (colheitadeiras, tratores) em grandes propriedades é um desafio complexo:  
- **Desperdício de recursos**: Rotas redundantes aumentam consumo de combustível.  
- **Tempo ocioso**: Operações manuais levam a altas horas diárias de improdutividade.  
- **Custo elevado**: Falta de otimização provoca alto custo a agricultura familiar e para o agronegócio brasileiro.  

---

## 🚀 Solução  
O **CropPilot** utiliza algoritmos genéticos para calcular **rotas otimizadas** que:  
- Minimizam a distância percorrida
- Consideram capacidade das máquinas e geolocalização dos talhões 
- Reduzem custos operacionais

---

## 💻 Tecnologias  
| Componente               | Tecnologias                                                                 |  
|--------------------------|-----------------------------------------------------------------------------|  
| **Backend**              | Django 4.2, Django REST Framework                                           |  
| **Algoritmo**            | DEAP (Distributed Evolutionary Algorithms in Python)                        |  
| **Geoprocessamento**     | Geopandas, Shapely                                                         |  
| **Testes**               | Pytest, Postman                                                            |  
| **Infraestrutura**       | Docker (opcional), PostgreSQL                                              |  

---

## 🗂️ Documentação da API  

### Endpoint: `POST /api/optimize/`  
**Requisição:**  
```json  
{  
    "points": [  
        {  
            "name": "Talhão A",  
            "latitude": -29.6875,  
            "longitude": -53.7892  
        },  
        {  
            "name": "Talhão B",  
            "latitude": -29.6913,  
            "longitude": -53.7810  
        }  
    ],  
    "machine": {  
        "capacity_kg": 2000,  
        "speed_kmh": 8  
    }  
}  
```

**Resposta (Sucesso 200):**
```json
{  
    "optimized_route": [2, 1, 0],  
    "total_distance_km": 8.7,  
    "estimated_fuel_liters": 42.3  
}  
```



---

## ⚙️ Instalação  

Clone o repositório:  

```bash  
git clone https://github.com/andre-bandeli/CropPilot.git  
cd CropPilot  
```

Ambiente virtual:  
```bash  
python -m venv venv  
source venv/bin/activate  # Linux/Mac  
venv\Scripts\activate    # Windows  
```

Instale as dependências:  
```bash  
pip install -r requirements.txt  
```

Banco de dados:  
```bash  
python manage.py migrate  
```

Execute:  
```bash  
python manage.py runserver  
```

---

## 🧪 Testes  

**Via Postman:**  
- Importe a coleção `CropPilot.postman_collection.json`  
- Envie requisições para `http://localhost:8000/api/optimize/`  

**Via cURL:**  
```bash  
curl -X POST http://localhost:8000/api/optimize/ \  
-H "Content-Type: application/json" \  
-d '{"points": [{"latitude": -29.68, "longitude": -53.78}], "machine": {"capacity_kg": 1500}}'  
```

---

## 🤝 Como Contribuir  
- Abra uma issue descrevendo a melhoria  
- Faça um fork do projeto  
- Crie uma branch: `git checkout -b feature/nova-funcionalidade`  
- Envie um Pull Request  

---


**CropPilot - Transformando inteligência computacional em eficiência no campo! 🚜💡**
