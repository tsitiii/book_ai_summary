from rest_framework.viewsets import ModelViewSet
from .models import Book
from django.contrib.auth.models import User
from .serializers import UserSerializer, BookSerializer
from rest_framework.response import Response
from rest_framework import status
import google.generativeai as genai
import os


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyCk9yz6No87BWJ3RuYDws5yMfyng4KVAJU")
genai.configure(api_key=GEMINI_API_KEY)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self,request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        
        title = serializer.validated_data.get('title')
        author = serializer.validated_data.get('author')
        pdf_file = request.FILES.get('pdf_file')
        
        prompt = f'Give me the summary of the following BOOK with reason why i should read it, \n Title {title}, \n Author: {author}'
        if pdf_file:
            content = pdf_file.read(2048).decode(errors='ignore')
            prompt += f'content: {content}'
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            ai_summary = response.text
        except Exception as e:
            ai_summary = f"AI error: {str(e)}"
        book = serializer.save(ai_summary=ai_summary)
        output_serializer = self.get_serializer(book)
        return Response(
            data=output_serializer.data,
            status=status.HTTP_201_CREATED,
        
        )
        