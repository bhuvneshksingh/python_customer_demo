from rest_framework import generics, permissions
from rest_framework.response import Response

from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from account.api.serializers import CustomerSerializer
from account.models import Customer
from django.views.decorators.csrf import csrf_exempt

# Views for Customer Personal Details
@api_view(['GET'])
@csrf_exempt
def CustomerListView(request):
	try:
		customers = Customer.objects.all()
		serializer = CustomerSerializer(customers, many=True)
		return Response(serializer.data)
	except Error as error:
		print(f"Error "+ error)

@api_view(['GET'])
@csrf_exempt
def CustomerDetailView(request, id):
	try:
		customers = Customer.objects.get(id=id)
		serializer = CustomerSerializer(customers, many=False)
		return Response(serializer.data)
	except Customer.DoesNotExist:
		return Response({'Response':'Customer Not exist'})

@api_view(['POST'])
@csrf_exempt
def CustomerCreateView(request):
	
	serializer = CustomerSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@csrf_exempt
def CustomerUpdateView(request, id):
	try:
		customer = Customer.objects.get(id=id)
		serializer = CustomerSerializer(instance=customer, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	except Customer.DoesNotExist:
		return Response({'Response':'Customer Not exist'})


@api_view(['DELETE'])
@csrf_exempt
def CustomerDeleteView(request, id):
	try:
		customer = Customer.objects.get(id=id)
		customer.delete()

		return Response('Item Successfully Deleted!')
	except Customer.DoesNotExist:
		return Response({'Response':'Customer Not exist'})
