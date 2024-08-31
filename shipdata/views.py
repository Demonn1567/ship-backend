from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ParameterSubmission
from .serializers import ParameterSubmissionSerializer



# Create your views here.


@api_view(['POST', 'GET'])
def submit_parameters(request):
    if request.method == 'POST':
        serializer = ParameterSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        submissions = ParameterSubmission.objects.all()
        serializer = ParameterSubmissionSerializer(submissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'DELETE'])
def get_submission_by_id(request, pk):
    try:
        submission = ParameterSubmission.objects.get(pk=pk)
    except ParameterSubmission.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ParameterSubmissionSerializer(submission)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'DELETE':
        submission.delete()
        return Response({'msg': 'Data Deleted'}, status=status.HTTP_204_NO_CONTENT)




