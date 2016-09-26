# -*- coding: utf-8 -*-
import http.client

import requests
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser


class SlackApi:

    host = 'slack.com/api/chat.postMessage'
    token = 'xoxp-2151854096-3554168434-83721985331-3eeb5d6670ad5a1b4fb640d4b3bd6c31'

    @staticmethod
    def send_message(self, channel, username, icon_url, attachments):

        url = '?token=' + SlackApi.token + '&channel=' + channel + '&username=' + username + \
               '&icon_url=' + icon_url + '&attachments=' + attachments;
        try:
            res = requests.post(
                'http://slack.com/api/chat.postMessage'+url,
            )

        except Exception as e:
            raise Exception('Error in request slack api (http://slack.com/api/chat.postMessage) ' + str(e))

        if res.status_code == http.client.OK:
            stream = BytesIO(res.content)
            data = JSONParser().parse(stream)
            return data
        else:
            raise Exception('Could not be to send message')

    @staticmethod
    def get_users(self):

        url = '?token=' + SlackApi.token;
        try:
            res = requests.get(
                'https://slack.com/api/users.list' + url,
            )

        except Exception as e:
            raise Exception('Error in request slack api (https://slack.com/api/users.list) ' + str(e))

        if res.status_code == http.client.OK:
            stream = BytesIO(res.content)
            data = JSONParser().parse(stream)

            return data['members']
        else:
            raise Exception('Users not found')
