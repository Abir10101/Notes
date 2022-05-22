from rest_framework.response import Response
from rest_framework.views import APIView
from .serialize import NoteSerializer
from .models import Note



class NoteView( APIView ):
    def post( self, request ):
        serializer = NoteSerializer( data=request.data )
        
        if serializer.is_valid():
            serializer.save()
            return Response( {"status":"success", "data":serializer.data} )
        else:
            return Response( {"status":"error", "data":serializer.errors} )

    def get( self, request, pk=None ):
        if pk:
            note = Note.objects.get( id=pk )
            serializer = NoteSerializer( note, many=False )
            return Response( {"status":"success", "data":serializer.data} )

        notes = Note.objects.all()
        serializer = NoteSerializer( notes, many=True )
        return Response( {"status":"success", "data":serializer.data} )


# @api_view( ['GET'] )
class GetRoutes( APIView ):
    def get( self, request ):
        routes = [
            {
                'Endpoint': '/notes/',
                'method': 'GET',
                'body': None,
                'description': 'Returns an array of notes'
            },
            {
                'Endpoint': '/notes/id',
                'method': 'GET',
                'body': None,
                'description': 'Returns a single note object'
            },
            {
                'Endpoint': '/notes/',
                'method': 'POST',
                'body': {'body': ""},
                'description': 'Creates new note with data sent in post request'
            },
            {
                'Endpoint': '/notes/id/',
                'method': 'PUT',
                'body': {'body': ""},
                'description': 'Creates an existing note with data sent in post request'
            },
            {
                'Endpoint': '/notes/id/',
                'method': 'DELETE',
                'body': None,
                'description': 'Deletes and exiting note'
            },
        ]
        
        return Response( routes )