from rest_framework import serializers
from rest_framework.views import APIView


class UserNewsFeedListApi(APIView):
    class OutputSerializer(serializers.Serializer):
        pass
    pass
