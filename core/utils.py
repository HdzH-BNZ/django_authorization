from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.exceptions import (NotAuthenticated, PermissionDenied, NotFound, ValidationError)
from django.http import Http404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError

def custom_handler404(request, exception):
    message = {'message':'The endpoint is not found','status_code':404}
    message = JsonResponse(message)
    return HttpResponseNotFound(message)

def custom_handler500(request, *args, **argv):
    message = {'message':'Error côté serveur','status_code':500}
    message = JsonResponse(message)
    return HttpResponseServerError(message)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data = {"error":"Not found.","error_description":"Aucun élément trouvé"}
    if isinstance(exc, NotAuthenticated):
        response.data = {"error":"Unauthorized","error_description":"Utilisateur non-authentifié"}
    if isinstance(exc, PermissionDenied):
        response.data = {"error":"Permission denied","error_description":"Accès refusé"}
    if isinstance(exc, NotFound):
        #response.data = {"error":"Not Found","error_description":"Page introuvable"}
        response.data['status_code'] = response.status_code

    return response