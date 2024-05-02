from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import EvaluationResult
from ..store.models import Item as StoreItem
from ..store.models import Category as StoreCategory
from ..transactions.models import Purchase as TransactionPurchase
from ..transactions.models import Sale as TransactionSale

from datetime import datetime
import pandas as pd


def evaluacion_modelo(request, resultado_id):
    # Obtener el objeto de Resultado Evaluacion usando el resultado_id
    resultado = EvaluationResult.objects.get(id=resultado_id)
    # Renderizar la plantilla y pasar el resultado a la plantilla
    return render(request, 'evaluacion_modelo.html', {'resultado': resultado})


def group_columns_from_django():
    # Obtener los datos de las tablas de Django
    categories = StoreCategory.objects.all().values_list('name', flat=True)
    items = StoreItem.objects.all().values_list('slug', 'name', 'quantity', 'selling_price')
    purchases = TransactionPurchase.objects.all().values_list('order_date', 'quantity', 'price', 'total_value')
    sales = TransactionSale.objects.all().values_list('transaction_date', 'quantity', 'payment_method', 'price',
                                                      'total_value', 'amount_received', 'balance')

    # Crear DataFrames para cada tabla
    df_categories = pd.DataFrame(categories, columns=['category_name'])
    df_items = pd.DataFrame(items, columns=['slug', 'item_name', 'quantity', 'selling_price'])
    df_purchase = pd.DataFrame(purchases,
                               columns=['order_date', 'quantity_purchase', 'price_purchase', 'total_value_purchase'])
    df_sale = pd.DataFrame(sales, columns=['transaction_date', 'quantity_sale', 'payment_method', 'price_sale',
                                           'total_value_sale', 'amount_received', 'balance'])

    # Agrupar las columnas de las tablas
    grouped_columns = pd.concat([df_categories['category_name'], df_items, df_purchase, df_sale], axis=1)

    return grouped_columns


# Ejemplo de uso
grouped_data = group_columns_from_django()
print(grouped_data)
