from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Joueurs
from .serializers import JoueursSerializer
from django.http import Http404

'''
from rest_framework.authtoken.models import Token

token = Token.objects.create(user=...)
print(token.key)
'''

# Create your views here.
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def getJoueurs(request):
    '''
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated!')
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
    '''
    joueurs = Joueurs.objects.all()
    serializer = JoueursSerializer(joueurs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getOneJoueur(request, pk):
    try:
        joueurs = Joueurs.objects.get(id=pk)
        serializer = JoueursSerializer(joueurs, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Joueurs.DoesNotExist:
        raise Http404

@api_view(['GET'])
def view400(request):
    payload = {
            "error":"erreur 400",
            "error_description":"Erreur côté 400"
        }
    return JsonResponse(data=payload, status=400)