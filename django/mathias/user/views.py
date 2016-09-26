# -*- coding: utf-8 -*-
import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from mathias.api.slack import SlackApi
from mathias.user.core.adapter_user import AdapterUser
from mathias.utils.metadata import MetaError


class UserList(APIView):

    def post(self, request, format=None):
        """
        Save user
        ---
        """
        meta = self.metadata_class()

        users = SlackApi.get_users(self)

        try:
            list_users = AdapterUser(users).adapter()

            for u in list_users:
                # if u.id == 'U22C623DL':
                #     teste = u.title
                #
                #     u.title = teste[0:-1]

                u.save()
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
