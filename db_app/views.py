from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
import time
from rest_framework.response import Response
import json

# Create your views here


class A_list(APIView):

    def get(self, request, format=None):
        startT = time.time()
        a1 = A.objects.all()
        serializer = A_Serializer(a1, many=True)
        result = serializer.data
        od1 = json.dumps(result)
        print(type(od1))
        results1 = (f'Execution time: {time.time() - startT}ms for A_list', "\n", od1)
        print(results1)
        print(type(od1))
        outF = open("A_model.txt", "w")
        for line in results1:
            # write line to output file
            outF.write(line)
        outF.close()

        return Response(result)

class A_list_select_related(APIView):

    def get(self, format=None):
        startT = time.time()
        a2 = A.objects.select_related()
        serializer = A_Serializer(a2, many=True)
        result = serializer.data
        od1 = json.dumps(result)
        print(type(od1))
        results1 = ("\n", f'Execution time: {time.time() - startT}ms for A_list_select_related', "\n", od1)
        print(results1)

        outF = open("A_model.txt", "a")
        for line in results1:

            outF.write(line)
        outF.close()
        return Response(result)

class A_list_prefetch_related(APIView):

    def get(self, format=None):
        startT = time.time()
        a2= A.objects.select_related().prefetch_related("c")
        serializer = A_Serializer(a2, many=True)
        result = serializer.data
        od1 = json.dumps(result)
        print(type(od1))
        results1 = ("\n", f'Execution time: {time.time() - startT}ms for A_list_prefetch_related', "\n", od1)
        print(results1)

        outF = open("A_model.txt", "a")
        for line in results1:

            outF.write(line)
        outF.close()
        return Response(result)
class A_list_create(APIView):

    def post(self, request, format=None):
        startT = time.time()
        a1 = A.objects.bulk_create([A(name="a5"),A(name="a6")])
        serializer = A_Serializer(a1, many=True)
        # serializer.is_valid()
        result = serializer.data
        od1 = json.dumps(result)
        print(type(od1))
        results1 = (f'Execution time: {time.time() - startT}ms', od1)
        print(results1)

        outF = open("A_list.txt", "w")
        for line in results1:
            outF.write(line)
        outF.close()
        return Response(result)

class B_list(APIView):

    def get(self, request, format=None):
        startT = time.time()
        b1 = B.objects.all()
        serializer = B_Serializer(b1, many=True)
        result = serializer.data
        od1 = json.dumps(result)
        print(type(od1))
        results1 = (f'Execution time: {time.time() - startT}ms of B_list', '\n', od1)
        print(results1)

        outF = open("B_model.txt", "w")
        for line in results1:

            outF.write(line)
        outF.close()

        return Response(result)

class B_list_select_related(APIView):

    def get(self, request, format=None):
        startT = time.time()
        b1 = B.objects.select_related()
        serializer = B_Serializer(b1, many=True)

        result = serializer.data
        od1 = json.dumps(result)
        print(type(od1))
        results1 = ("\n", f'Execution time: {time.time() - startT}ms of B_select_related', "\n", od1)
        print(results1)

        outF = open("B_model.txt", "a")
        for line in results1:
            outF.write(line)
        outF.close()

        return Response(result)
class C_list(APIView):

    def get(self, request, format=None):
        startT = time.time()
        c1 = C.objects.all()
        serializer = C_Serializer(c1, many=True)
        result = serializer.data
        od1 = json.dumps(result)
        print(type(od1))
        results1 = ("\n", f'Execution time: {time.time() - startT}ms for C_list', "\n", od1)
        print(results1)

        outF = open("C_model.txt", "w")
        for line in results1:
            outF.write(line)
        outF.close()

        return Response(result)


class C_list_prefetch_related(APIView):

    def get(self, request, format=None):
        startT = time.time()
        c1 = C.objects.prefetch_related('a')
        serializer = C_Serializer(c1, many=True)
        result = serializer.data

        od1 = json.dumps(result)
        print(type(od1))
        results1 = ("\n",f'Execution time: {time.time() - startT}ms for C_list_prefetch_related',"\n", od1)
        print(results1)

        outF = open("C_model.txt", "a")
        for line in results1:
            outF.write(line)
        outF.close()

        return Response(result)