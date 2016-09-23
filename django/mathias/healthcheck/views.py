from django.db import connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class HealthcheckView(APIView):
    def get(self, request, format=None):
        """
        Health Check
        """
        meta = self.metadata_class()

        check = {
            "APPLICATION": True,
            "MYSQL": True
        }

        try:
            cursor = connection.cursor()

            cursor.execute('SELECT 1')
            row = cursor.fetchone()

        except Exception as e:
            check['MYSQL'] = False

            return Response(check, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(check, status=status.HTTP_200_OK)
