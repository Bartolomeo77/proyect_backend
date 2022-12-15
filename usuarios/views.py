from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Usuario
from .serializers import UsuarioSerializer

class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    
class UsuariosView(APIView):
    
    def get(self,request):
        dataSeries = Usuario.objects.all()
        serSeries = UsuarioSerializer(dataSeries,many=True)
        return Response(serSeries.data)
    
    def post(self,request):
        serSerie = UsuarioSerializer(data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        
        return Response(serSerie.data)
    
class UsuarioDetailView(APIView):
    
    def get(self,request,serie_id):
        dataSerie = Usuario.objects.get(pk=serie_id)
        serSerie = UsuarioSerializer(dataSerie)
        return Response(serSerie.data)
    
    def put(self,request,serie_id):
        dataSerie = Usuario.objects.get(pk=serie_id)
        serSerie = UsuarioSerializer(dataSerie,data=request.data)
        serSerie.is_valid(raise_exception=True)
        serSerie.save()
        return Response(serSerie.data)
    
    def delete(self,request,serie_id):
        dataSerie = Usuario.objects.get(pk=serie_id)
        serSerie = UsuarioSerializer(dataSerie)
        dataSerie.delete()
        return Response(serSerie.data)
