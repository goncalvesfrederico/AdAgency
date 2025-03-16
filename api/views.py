from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Branchs, Audiences, Positionings, Campaigns, Ads
from .serializer import BranchsSerializer, AudiencesSerializer, PositioningsSerializer, \
    CampaignsSerializer, AdsSerializer

@api_view(['GET'])
def get_branchs(request):
    branchs = Branchs.objects.all()
    serializer = BranchsSerializer(branchs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_branch(request):
    serializer = BranchsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def branch_detail(request, pk):
    try:
        branch = Branchs.objects.get(pk=pk)
    except Branchs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = BranchsSerializer(branch)
        return Response(serializer.data)
    
    elif request.method == "PATCH":
        serializer = BranchsSerializer(branch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)