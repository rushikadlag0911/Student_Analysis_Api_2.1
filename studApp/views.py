from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import studdetails, studmarks
from django.views.decorators.csrf import csrf_exempt
from .serializers import studserializers,studmarksserializers, smarkserializer
import json
import csv
from rest_framework.decorators import api_view

@api_view(['POST'])
def retrive(request):
	try:
		print(request.data)
		roll_num = request.data['roll_num']
		
		if roll_num == None:
			return JsonResponse("some parameter is missing", status=400, safe=False)

		if roll_num == " ":
			return JsonResponse("some parameter is missing", status=400, safe=False)
		
		stud1 = studmarks.objects.filter(roll_num=roll_num).select_related('roll_num')
		print('m',stud1);
		serializer = studmarksserializers(stud1, many=True)
		print('t',serializer.data)
		data={}
		listofstud=[]
		for i in stud1 :
			data["Name"]=i.roll_num.name
			data["English"] = i.English
			data["Maths"] = i.Maths
			data["History"] = i.History
		listofstud.append(data)
		return JsonResponse(serializer.data,status=200,safe=False)
	except Exception as ex:
		print(ex)
		return JsonResponse('Bad Request something wrong', status=404, safe=False)
	
# @api_view(['POST'])
# def create(request):
# 	try:
# 		serializer1 = studmarksserializers(data=request.data)
# 		print(serializer1)
# 		if serializer1.is_valid():
# 			serializer1.save()
# 			return Response(serializer1.data, status=status.HTTP_201_CREATED)
#
# 		return  Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)
#
# 	except Exception as ex:
# 		print(ex)
# 		return JsonResponse('Bad Request Something Wrong')

@api_view(['POST'])
def s_create(request):
    
	serializer = studserializers(data=request.data)
	print(serializer)
	if serializer.is_valid():
		serializer.save()
		return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

	return  JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
@api_view(['POST'])
def m_create(request):
	print(request.data)
	mserializer = smarkserializer(data=request.data)
	print(mserializer)
	if mserializer.is_valid():
		mserializer.save()
		return JsonResponse(mserializer.data, status=status.HTTP_201_CREATED)
	
	return JsonResponse(mserializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_update(request):     #anand sir logic
	data=studmarks.objects.filter(roll_num=request.data['roll_num'])
	if data.exists():
		update_data = data.update(
			English = request.data["English"],
			Maths = request.data["Maths"],
			History = request.data["History"]
		)
		print(update_data)
		if (update_data)>0:
			return JsonResponse("Updated sucessfully", status=status.HTTP_201_CREATED,safe=False)
		else:
			return JsonResponse("Unabel to update", status=status.HTTP_400_BAD_REQUEST,safe=False)
		
	else:
		data=studdetails.objects.get(roll_num=request.data['roll_num'])
		create_marks=studmarks.objects.create(
			roll_num=data,
			English=request.data["English"],
			Maths=request.data["Maths"],
			History=request.data["History"]
		)
		if (create_marks.id)>0:
			return JsonResponse("created sucessfully", status=status.HTTP_201_CREATED,safe=False)
		else:
			return JsonResponse("Unabel to create", status=status.HTTP_400_BAD_REQUEST,safe=False)

@api_view(['POST'])
def create_update1(request):	# arun sir logic
	data = studdetails.objects.filter(roll_num=request.data['roll_num'])
	print(data)
	if data.exists():
		try:
			data1 = studmarks.objects.filter(roll_num=request.data['roll_num'])
			if data1.exists():
				update_data = data1.update(
					English=request.data["English"],
					Maths=request.data["Maths"],
					History=request.data["History"]
				)
				if (update_data) > 0:
					return JsonResponse("Updated sucessfully", status=status.HTTP_201_CREATED, safe=False)
				else:
					return JsonResponse("Unabel to update", status=status.HTTP_400_BAD_REQUEST, safe=False)
			else:
				create_marks = studmarks.objects.create(
					roll_num=data,
					English=request.data["English"],
					Maths=request.data["Maths"],
					History=request.data["History"]
				)
				if (create_marks.id) > 0:
					return JsonResponse("created sucessfully", status=status.HTTP_201_CREATED, safe=False)
				else:
					return JsonResponse("Unabel to create", status=status.HTTP_400_BAD_REQUEST, safe=False)
		
		except Exception as ex:
			return JsonResponse("Unabel to create", status=status.HTTP_400_BAD_REQUEST, safe=False)
	else:
		try:
			create_stud = studdetails.objects.create(
				roll_num=request.data['roll_num'],
				name=request.data['name'],
				DOB=request.data['DOB']
			)
			
			create_marks = studmarks.objects.create(
				roll_num_id=request.data['roll_num'],
				English=request.data["English"],
				Maths=request.data["Maths"],
				History=request.data["History"]
			)
			if (create_marks.id) > 0:
				return JsonResponse("created sucessfully", status=status.HTTP_201_CREATED, safe=False)
			else:
				return JsonResponse("Unabel to create", status=status.HTTP_400_BAD_REQUEST, safe=False)
		
		except Exception as ex:
			return JsonResponse("Unabel to create", status=status.HTTP_400_BAD_REQUEST, safe=False)


@api_view(['POST'])
def create_all(request):            # created_by_rushi
	data = studdetails.objects.filter(roll_num=request.data['roll_num'])
	print(data)
	if data.exists():
		return JsonResponse("Data Already Exist", status=status.HTTP_400_BAD_REQUEST, safe=False)
	else:
		try:
			create_stud = studdetails.objects.create(
				roll_num=request.data['roll_num'],
				name=request.data['name'],
				DOB=request.data['DOB']
			)
			create_marks = studmarks.objects.create(
				roll_num_id=request.data['roll_num'],
				English=request.data["English"],
				Maths=request.data["Maths"],
				History=request.data["History"]
			)
			return JsonResponse("Record created sucessfully", status=status.HTTP_201_CREATED, safe=False)
		
		except Exception as ex:
			return JsonResponse("Unabel to create", status=status.HTTP_400_BAD_REQUEST, safe=False)
		

@api_view(['POST'])
def updateallmarks(request):
	if not all(k in request.data for k in ("roll_num","English","Maths","History")):
		return JsonResponse('Parameter missing',status=status.HTTP_400_BAD_REQUEST,safe=False)
	data = studmarks.objects.filter(roll_num=request.data['roll_num'])
	print(data)
	if data.exists():
		update_mark_data = data.update(
			English=request.data["English"],
			Maths=request.data["Maths"],
			History=request.data["History"]
		)
		return JsonResponse("Data Updated", status=status.HTTP_200_OK, safe=False)
	
	else:
		return JsonResponse("Data is not there pls create record first",status=status.HTTP_400_BAD_REQUEST,safe=False)

@api_view(['POST'])
def deletemarks(request):
	print(request)
	data = studmarks.objects.filter(roll_num=request.data['roll_num'])
	# data = studmarks.objects.all()
	print(data)
	if data.exists():
		deleted_data = data.delete()
		return JsonResponse("Data Deleted successfully", status=status.HTTP_200_OK, safe=False)
	
	else:
		return JsonResponse("Data is not there", status=status.HTTP_400_BAD_REQUEST, safe=False)


@api_view(['POST'])
def deletestud(request):
	print(request)
	data = studdetails.objects.filter(roll_num = request.data['roll_num'])
	print(data)
	if data.exists():
		deleted_student = data.delete()
		return JsonResponse("Data Deleted Successfully", status=status.HTTP_200_OK, safe=False)
	else:
		return JsonResponse("Data Not Found", status=status.HTTP_400_BAD_REQUEST, safe = False)
	
@api_view(['POST'])
def export_stud_csv(request):
	response = HttpResponse(content_type = 'text\csv')
	response['Content-Disposition'] = 'attachment; filename="students.csv"'
	
	writer = csv.writer(response)
	writer.writerow(['roll_num','name','DOB','English','Maths','History'])
	stud1 = studmarks.objects.all()
	serializer = studmarksserializers(stud1, many=True)
	data = {}
	listofstud = []
	for i in stud1:
		data["Name"] = i.roll_num.name
		data["English"] = i.English
		data["Maths"] = i.Maths
		data["History"] = i.History
	listofstud.append(data)
	writer.writerow(serializer.data)
	return response

@api_view(['POST'])
def allstudentmarks(request):
	try:
		stud1 = studmarks.objects.all()
		serializer = studmarksserializers(stud1, many=True)
		data = {}
		listofstud = []
		for i in stud1:
			data["Name"] = i.roll_num.name
			data["English"] = i.English
			data["Maths"] = i.Maths
			data["History"] = i.History
		listofstud.append(data)
		return JsonResponse(serializer.data, status=200, safe=False)
	except Exception as ex:
		print(ex)
		return JsonResponse('Bad Request something wrong', status=404, safe=False)