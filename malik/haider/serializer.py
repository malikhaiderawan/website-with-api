from rest_framework import serializers
from haider.models import Contact, Feedback, Home

class Contactserializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'

class Feedbackserializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields='__all__'


class Homeserializer(serializers.ModelSerializer):
    class Meta:
        model=Home
        fields='__all__'


