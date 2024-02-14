from rest_framework import generics
from rest_framework.response import Response

class FibonacciAPI(generics.ListAPIView):
    
    def get(self, request,pk=None):
        num = pk

        if num>0:
            fib_list = [0] * (num+1)
            fib_list[0]=0
            fib_list[1]=1
            
            for i in range(2,num+1):
                fib_list[i] = fib_list[i-1]+fib_list[i-2]

            return Response({f"fibonnaci numbers upto {num} integer(s) are":fib_list[:num]})
        
        return Response({"error": "Wrong Input"},status=400)


