from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes =[
        {
            'Endpoint' : '/notes/',
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns an array of notes'
        },
        {
            'Endpoint' : '/notes/id',
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns a single note object'
        },
        {
            'Endpoint' : '/notes/create/',
            'method' : 'POST',
            'body' : {'body':""},
            'description' : 'Creates new note with data sent in post request'
        },
        {
            'Endpoint' : '/notes/id/update/',
            'method' : 'PUT',
            'body' : {'body':""},
            'description' : 'Creats an existing note with data sent in PUT request'
        },
        {
            'Endpoint' : '/notes/id/delete/',
            'method' : 'DELETE',
            'body' : None,
            'description' : 'Deletes an existing note'
        },
        
    ]
    return Response(routes)
        