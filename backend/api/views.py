from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import re

class JsonView(APIView):
    def post(self, request):
        try:
            data = request.data.get("data", [])
            if not isinstance(data, list):
                return Response({"error": "Invalid input: data must be an array"}, status=status.HTTP_400_BAD_REQUEST)

            numbers = []
            alphabets = []
            highest_alphabet = []

            for item in data:
                if isinstance(item, str):
                    if re.match(r"^\d+$", item):
                        numbers.append(item)
                    elif re.match(r"^[A-Za-z]$", item):
                        alphabets.append(item)

            if alphabets:
                highest_alphabet = [max(alphabets, key=str.lower)]

            response_data = {
                "is_success": True,
                "user_id": "john_doe_17091999",  
                "email": "john@xyz.com",
                "roll_number": "ABCD123",
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_alphabet": highest_alphabet,
            }
            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)