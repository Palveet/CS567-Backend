from rest_framework import serializers
from .models import User, Article, SurveyResponse

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'political_affiliation', 'gender', 'age', 'ethnicity',
                  'socioeconomic_status', 'education_level', 'occupation', 'created_at', 'updated_at']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'publisher', 'created_at']

class SurveyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyResponse
        fields = ['id', 'user', 'article', 'response', 'created_at']
