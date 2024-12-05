from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import login, logout, authenticate
from .models import User, Article, SurveyResponse
from .serializers import UserSerializer, ArticleSerializer, SurveyResponseSerializer


@api_view(['POST'])
def signup(request):
    data = request.data
    if data['password'] != data['confirm_password']:
        return Response({'error': 'Passwords do not match'}, status=400)

    user = User.objects.create_user(
        username=data['username'],
        password=data['password'],
        political_affiliation=data.get('political_affiliation'),
        gender=data.get('gender'),
        age=data.get('age'),
        ethnicity=data.get('ethnicity'),
        socioeconomic_status=data.get('socioeconomic_status'),
        education_level=data.get('education_level'),
        occupation=data.get('occupation'),
    )
    return Response(UserSerializer(user).data, status=201)


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return Response({'message': 'Login successful'})
    return Response({'error': 'Invalid credentials'}, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'message': 'Logout successful'})


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile(request):
    if request.method == 'GET':
        return Response(UserSerializer(request.user).data)
    elif request.method == 'PUT':
        user = request.user
        for key, value in request.data.items():
            setattr(user, key, value)
        user.save()
        return Response(UserSerializer(user).data)


@api_view(['GET'])
def articles(request):
    articles = Article.objects.all()
    return Response(ArticleSerializer(articles, many=True).data)

@api_view(['GET'])
def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return Response(ArticleSerializer(article).data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_survey(request):
    data = request.data
    survey = SurveyResponse.objects.create(
        user=request.user,
        article_id=data['article_id'],
        response=data['response']
    )
    return Response(SurveyResponseSerializer(survey).data)

@api_view(['GET'])
def survey_responses(request, article_id):
    surveys = SurveyResponse.objects.filter(article_id=article_id)
    return Response(SurveyResponseSerializer(surveys, many=True).data)
