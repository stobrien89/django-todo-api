from models import Todo
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class Todo Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        # fields that should be included in the serialized output
        fields = ['id', 'subject', 'details']
