# -*- coding: utf-8 -*-
from rest_framework import serializers

from mathias.user.models import User
from mathias.user.serializers import UserSerializer
from mathias.valeu.models import Valeu, SaveValeu


class ValeuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Valeu
        fields = ('id', 'team_id', 'team_domain', 'channel_id', 'channel_name',
                  'user_id_from', 'user_name_from', 'user_id_to', 'user_name_to',
                  'command', 'text', 'create_at')

class ValeuSaveSerializer(serializers.Serializer):
    token = serializers.CharField()
    team_id = serializers.CharField()
    team_domain = serializers.CharField()
    channel_id = serializers.CharField()
    channel_name = serializers.CharField()
    user_id = serializers.CharField()
    user_name = serializers.CharField()
    command = serializers.CharField()
    text = serializers.CharField()
    response_url = serializers.CharField()

    def create(self, validated_data):
        return SaveValeu(**validated_data)

    def update(self, instance, validated_data):
        return instance


class ValeuLeaderBoardSerializer(serializers.Serializer):
    total = serializers.IntegerField()
    user = serializers.SerializerMethodField()

    def get_user(self, obj):

        user = User.objects.get(name=obj['user_name_to'])

        serializer_user = UserSerializer(user)

        return serializer_user.data

