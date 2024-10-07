# views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Curso
from .serializers import CursoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def create(self, request, *args, **kwargs):
        # Lógica para crear un curso
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Curso creado"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        # Lógica para actualizar un curso
        curso = self.get_object()
        serializer = self.get_serializer(curso, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Curso actualizado"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        # Lógica para eliminar un curso
        curso = self.get_object()
        curso.delete()
        return Response({"status": "Curso eliminado"}, status=status.HTTP_204_NO_CONTENT)
