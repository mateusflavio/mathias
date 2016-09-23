# -*- coding: utf-8 -*-
from rest_framework import serializers

from mathias.valeu.models import Valeu


class ValeuSerializer(serializers.ModelSerializer):
    createAt = serializers.CharField(max_length=20, source='create_at')

    class Meta:
        model = Valeu
        fields = ('id', 'username', 'message', 'createAt')
