from rest_framework.response import Response


def response_data(status_code, message, data):
    response_data = Response({
            'status': status_code,
            'message': message,
            'data': data
          })
    return response_data