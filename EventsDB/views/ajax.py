from django.http import JsonResponse
from django.db.models import ObjectDoesNotExist
from EventsDB.models import Empleado

def check_user(request):
    user_id = request.GET.get('identificacion', None)
    data = {
        'exists': False
    }
    try:
        employee = Empleado.objects.get(identificacion=user_id)
        if employee:
            data = {
                'exists': True,
                'nombres': employee.nombres,
                'email': employee.email,
                'tipo_empleado': employee.tipo_empleado
                # Añadir más campos si es necesario
            }
            # Almacenar los datos en la sesión
            request.session['pre_filled_data'] = data
    except ObjectDoesNotExist:
        pass
    return JsonResponse(data)
