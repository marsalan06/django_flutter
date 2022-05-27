from email.quoprimime import body_check
from xmlrpc.client import ServerProxy
from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

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
        
@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    notes = Note.objects.filter(id=pk)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data

    note = Note.objects.create(
        body = data['body']
    )
    serializer = NoteSerializer(note,many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(request,pk):
    data = request.data
    # print(data)
    note = Note.objects.get(id=pk)
    print("============testing======")
    # print(note)
    serializer = NoteSerializer(note, data=data)
    # print(serializer)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note deleted")
