# -*- coding: utf-8 -*-
import logging
from django.db import connection

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from mathias.api.slack import SlackApi
from mathias.utils.metadata import Meta, MetaError
from mathias.valeu.core.adapter_valeu import AdapterValeu
from mathias.valeu.core import mysql_count_valeu
from mathias.valeu.models import Valeu
from mathias.valeu.serializers import ValeuSerializer, ValeuSaveSerializer


class ValeuList(APIView):
    def search_points_user(self, user_name_to):

        query = mysql_count_valeu.query(
            user_name_from=user_name_to)
        raw_list = []
        with connection.cursor() as c:
            c.execute(query)
            columns = c.description
            results = c.fetchall()

            for value in results:
                tmp = {}
                for (index, column) in enumerate(value):
                    tmp[columns[index][0]] = column
                raw_list.append(tmp)

        return raw_list

    def send_message(self, valeu):

        raw_list = self.search_points_user(valeu.user_name_to)

        pretext = '<@' + str(valeu.user_id_to) + '>' + ' now has ' + str(raw_list[0]['points']) + ' points!'

        message = 'from ' + '<@' + str(valeu.user_id_from) + '>:\n' + valeu.text

        attachments = '[{ "color": "good", "pretext":"' + pretext + '", ' + '"text":"' + message + '"}]'

        icon_url = 'http://luizalabs.com/static/img/ll.png'

        return SlackApi.send_message(self, valeu.channel_id, 'destaque', icon_url, attachments);

    def get(self, request, format=None):
        """
        List all valeus
        ---
        response_serializer: ValeuSerializer
        """
        meta = self.metadata_class()

        try:
            valeu = Valeu.objects.all()
        except Exception as e:
            meta_error = MetaError('Internal Server Error - ' + str(e),
                                   'Was encountered an error when'
                                   ' processing your request. We '
                                   'apologize for the inconvenience',
                                   status.HTTP_500_INTERNAL_SERVER_ERROR)
            data = meta.determine_metadata_error(
                request, self, [meta_error])
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = ValeuSerializer(valeu, many=True)
        data = meta.determine_metadata(request, self, Meta(), serializer.data)
        return Response(data)

    def post(self, request, format=None):
        """
        Save valeu
        ---
        parameters:
            - name: body
              pytype: ValeuSaveSerializer
              paramType: body
        """
        meta = self.metadata_class()

        serializer_request = ValeuSaveSerializer(data=request.data)

        if serializer_request.is_valid():

            calculate = serializer_request.save()

            try:
                valeu = AdapterValeu(calculate).adapter()

                if '@' in valeu:
                    meta_error = MetaError('User(s) '+ valeu +' in /valeu not found',
                                           'User(s) '+ valeu +' in /valeu not found',
                                           status.HTTP_404_NOT_FOUND)
                    data = meta.determine_metadata_error(request, self,
                                                         [meta_error])
                    return Response(data,
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                for v in valeu:
                    v.save()
                    self.send_message(v)

            except Exception as e:
                meta_error = MetaError('Internal Server Error - ' + str(e),
                                       'Was encountered an error when'
                                       ' processing your request. We '
                                       'apologize for the inconvenience',
                                       status.HTTP_500_INTERNAL_SERVER_ERROR)
                data = meta.determine_metadata_error(request, self,
                                                     [meta_error])
                return Response(data,
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(status=status.HTTP_200_OK)


        else:
            meta_error = MetaError(
                'Bad Request - Body invalid for ValeuSaveSerializer ' +
                str(serializer_request.errors),
                'Your request is invalid for a new /valeu',
                status.HTTP_400_BAD_REQUEST)
            data = meta.determine_metadata_error(request, self,
                                                 [meta_error])
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class ValeuDetail(APIView):
    def get_object(self, pk):
        try:
            return Valeu.objects.get(pk=pk)
        except Valeu.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Get valeu by pk
        ---
        response_serializer: ValeuSerializer
        """
        meta = self.metadata_class()
        try:
            valeu = self.get_object(pk)
        except Exception as e:
            meta_error = MetaError('Not found - Valeu not Found',
                                   'Your valeu id was not found',
                                   status.HTTP_404_NOT_FOUND)
            data = meta.determine_metadata_error(request, self,
                                                 [meta_error])
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        serializer = ValeuSerializer([valeu], many=True)

        data = meta.determine_metadata(request, self, Meta(), serializer.data)

        return Response(data)

    def put(self, request, pk, format=None):
        """
        Update valeu by pk
        ---
        response_serializer: ValeuSerializer
        parameters:
            - name: body
              pytype: ValeuSerializer
              paramType: body
        """
        meta = self.metadata_class()

        try:
            organization = self.get_object(pk)
        except Exception as e:
            meta_error = MetaError('Not found - Valeu not found',
                                   'Your valeu id was not found',
                                   status.HTTP_404_NOT_FOUND)

            data = meta.determine_metadata_error(request, self,
                                                 [meta_error])
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        serializer = ValeuSerializer(organization, data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                meta_error = MetaError('Internal Server Error - ' + str(e),
                                       'Was encountered an error when'
                                       ' processing your request. We '
                                       'apologize for the inconvenience',
                                       status.HTTP_500_INTERNAL_SERVER_ERROR)

                data = meta.determine_metadata_error(request, self,
                                                     [meta_error])
                return Response(data, status=status.HTTP_500_INTERNAL)

            data = meta.determine_metadata(request, self, Meta(),
                                           [serializer.data])
            return Response(data)
        else:
            meta_error = MetaError('Valeu Detail is invalid to put',
                                   'Valeu Detail is invalid to put',
                                   status.HTTP_400_BAD_REQUEST)

            data = meta.determine_metadata_error(request, self,
                                                 [meta_error])
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete valeu by pk
        """
        meta = self.metadata_class()
        try:
            valeu = self.get_object(pk)
        except Exception as e:
            meta_error = MetaError('Not found - Valeu not found',
                                   'Your valeu id was not found',
                                   status.HTTP_404_NOT_FOUND)

            data = meta.determine_metadata_error(request, self,
                                                 [meta_error])
            return Response(data, status=status.HTTP_404_NOT_FOUND)

        try:
            valeu.delete()
        except Exception as e:
            meta_error = MetaError('Internal Server Error - ' + str(e),
                                   'Was encountered an error when'
                                   ' processing your request. We '
                                   'apologize for the inconvenience',
                                   status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_204_NO_CONTENT)
