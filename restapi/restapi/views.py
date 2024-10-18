from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from trfapp.serializers import Stuser
from trfapp.models import Student
from rest_framework.permissions import IsAuthenticated

class TesView(APIView):

    permission_classes=(IsAuthenticated, )
    # parser_classes=() means anyone can access

    def get(self,request, *args, **kwargs):
        # data = {
        #     'username':'thomas',
        #     'days_active' : 100
        # }
        # return Response(data)

        qs=Student.objects.all()

        s=Stuser(qs,many=True) #for many
        
        #for 1
        # stud1=qs.first()
        # s=Stuser(stud1)
        
        return Response(s.data)        
    
    def post(selft,request,*args,**kwargs):
        s=Stuser(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors)