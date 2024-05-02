# En tu archivo urls.py

from django.urls import path
from . import views

urlpatterns = [
    # URL para ver los detalles de un resultado de evaluación específico
    path('evaluacion/<int:resultado_id>/', views.evaluacion_modelo, name='evaluacion-detalle'),
    # Otras URLs pueden ser definidas aquí según sea necesario
]