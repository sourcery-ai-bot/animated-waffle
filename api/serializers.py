from rest_framework import serializers

from api.models import GithubUser


class GithubUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GithubUser
        fields = ['avatar_url', 'username', 'name', 'followers', 'following']




