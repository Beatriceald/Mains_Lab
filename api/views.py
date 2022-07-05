# from rest_framework.viewsets import ReadOnlyModelViewSet
# from drf_excel.mixins import XLSXFileMixin
# from drf_excel.renderers import XLSXRenderer
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework import status

# from mains_lab.settings import MEDIA_ROOT

# from .models import *
# from .serializers import *

# class AddFile(APIView):

#     parser_classes = (MultiPartParser, FormParser)

#     def post(self, request, *args, **kwargs):
#         file_serializer = BillsSerializer(data=request.data)
#         if file_serializer.is_valid():
#             file_serializer.save()
#             file_path = MEDIA_ROOT + file_serializer.data['file']
#             # with open(file_path, 'r') as f:
#             #     # do something with file
#             return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

class PostsViewSet(viewsets.ModelViewSet):

    queryset = Biils.objects.all()
    serializer_class = BillsSerializer 
    # parser_classes = (JSONParser, MultiPartParser, CSVParser)
    renderer_classes = [XLSXRenderer]


    @action(detail=False, methods=['put'], name='Uploader View', renderer_classes=[XLSXRenderer],)
    def uploader(self, request, filename, format=None):
        # Parsed data will be returned within the request object by accessing 'data' attr  
        # _data = request.data
        file_serializer = BillsSerializer(data=request.data)
        if file_serializer.is_valid():
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

