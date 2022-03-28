from rest_framework import filters
from rest_framework import generics
from .serializers import MemberSerializer
from .models import Member
# Create your views here.

class MemberListView(generics.ListCreateAPIView):
    search_fields = ['gender', 'firstName', 'lastName']
    filter_backends = [filters.SearchFilter, ]
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


