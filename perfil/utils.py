from django.db.models import Sum

'-----------------------------------------'
# Calcular o total
'''def calcula_total(obj, campo):
    total = 0
    for i in obj:
        total += getattr(i, campo)

    return total'''
'-----------------------------------------'
def calcula_total(obj, campo):
    total = obj.aggregate(Sum(campo))['valor__sum']
    return total



'-----------------------------------------'