from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Curso
from .serializers import CursoSerializer

class WorkerView(APIView):
    def post(self, request):
        accion = request.data.get('accion')
        if accion == 'crear':
            serializer = CursoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'Curso creado'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif accion == 'actualizar':
            try:
                curso = Curso.objects.get(id=request.data.get('curso_id'))
            except Curso.DoesNotExist:
                return Response({'error': 'Curso no encontrado'}, status=status.HTTP_404_NOT_FOUND)
            serializer = CursoSerializer(curso, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'Curso actualizado'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Acción no válida'}, status=status.HTTP_400_BAD_REQUEST)
