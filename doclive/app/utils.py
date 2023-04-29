from rest_framework.response import Response


def response_data(status_code, message, data):
    return Response({
            'status': status_code,
            'message': message,
            'data': data
          })