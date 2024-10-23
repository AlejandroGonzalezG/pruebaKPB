from rest_framework import serializers
from posts.models import FactPosts, DimUsers, DimPosts, DimCompanies, DimAddresses

class FactPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactPosts
        fields = '__all__'

class DimUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = DimUsers
        fields = '__all__'

class DimPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DimPosts
        fields = '__all__'

class DimCompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DimCompanies
        fields = '__all__'

class DimAddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DimAddresses
        fields = '__all__'
