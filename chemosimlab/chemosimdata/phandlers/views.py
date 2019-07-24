from django.shortcuts import render
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
import pandas as pd
from .models import Ligend, Donnee_affinite, Recepteur
import logging
from django.core.paginator import Paginator

# Create your views here.
@login_required
def home(request):
   
    return render(request, 'home.html', {})

 
@login_required
def ligend(request):
	queryset = Ligend.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(queryset, 2)

	try:
		ligend = paginator.page(page)
	except PageNotAnInteger:
		# fallback to the first page
		ligend = paginator.page(1)
	except EmptyPage:
		# probably the user tried to add a page number
		# in the url, so we fallback to the last page
		ligend = paginator.page(paginator.num_pages)
	return render(request, 'ligend.html', {"ligend":ligend })

#@login_required
#def upload(request):
   
    #return render(request, 'upload.html', {})

def numbers_to_database(argument,df): 
    switcher = { 
        0: write_to_Ligend(df), 
        1: write_to_Recepteur(df), 
        2: write_to_Donnee_affinite(df), 
    }
    return switcher.get(argument, "nothing")
def write_to_Ligend(df):
	for index, row in df.iterrows():	
		model = Ligend()
		model.name = row["name"]
		model.smiles = row["smiles"]
		model.inchikey = row["inchikey"]
		model.save()	
	return True	

def write_to_Recepteur(df):
	for index, row in df.iterrows():	
		model = Ligend()
		model.name = row["name"]
		model.smiles = row["smiles"]
		model.inchikey = row["inchikey"]
		model.save()	
	return True	
def write_to_Donnee_affinite(df):
	for index, row in df.iterrows():	
		model = Ligend()
		model.name = row["name"]
		model.smiles = row["smiles"]
		model.inchikey = row["inchikey"]
		model.save()	
	return True	
@login_required
def upload(request):
	data = {}
	test="empty"
	if "GET" == request.method:
		return render(request, "upload.html", data)
    # if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file"]
		database_name = request.POST["database"]
		#Model = numbers_to_database(database_name); 
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("upload"))
        #if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
			return HttpResponseRedirect(reverse("upload"))

		df=pd.read_csv(csv_file,sep="\t")
		val=numbers_to_database(database_name,df)


		#file_data = csv_file.read().decode("utf-8")		
		#Check where the database name

		#lines = file_data.split("\n")
		#loop over the lines and save them in db. If error , store as string and then display
					
			

	except Exception as e:
		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		messages.error(request,"Unable to upload file. "+repr(e))

	return render(request, 'upload.html', {'test':" Uploaded with sucess"})#HttpResponseRedirect(reverse("upload",test="File Uploaded"))
