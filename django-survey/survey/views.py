from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.contrib import messages
import datetime
import settings

from models import Question, Survey, Category, Response, AnswerBase, AnswerSelect
from forms import ResponseForm
from cars_db_query import cars_db_filter


def Index(request):
	return render(request, 'index.html')

def SurveyDetail(request, id):
	survey = Survey.objects.get(id=id)
	category_items = Category.objects.filter(survey=survey)
	categories = [c.name for c in category_items]
	print 'categories for this survey:'
	print categories
	if request.method == 'POST':
		form = ResponseForm(request.POST, survey=survey)
		if form.is_valid():
			response = form.save()
			return HttpResponseRedirect("/confirm/%s" % response.interview_uuid)
	else:
		form = ResponseForm(survey=survey)
		print form
		# TODO sort by category
	return render(request, 'survey.html', {'response_form': form, 'survey': survey, 'categories': categories})

def Confirm(request, uuid):
	email = settings.support_email
	filtered_list = get_vehicle_list(uuid)
	return render(request, 'confirm.html', {'uuid':uuid, "email": email,'filtered_list': filtered_list})

def privacy(request):
	return render(request, 'privacy.html')


def get_vehicle_list(uuid):
	r = Response.objects.filter(interview_uuid = uuid)[0]
	qs = AnswerBase.objects.filter(response_id = r.id)
   	q1id = qs.filter(question_id = 1)[0]
   	q1qs = AnswerSelect.objects.filter(answerbase_ptr_id = q1id.id)
   	for e in q1qs:
   		q1 = e.body
	q2id = qs.filter(question_id = 2)[0]
   	q2qs = AnswerSelect.objects.filter(answerbase_ptr_id = q2id.id)
   	for e in q2qs:
   		q2 = e.body
	q9id = qs.filter(question_id = 9)[0]
   	q9qs = AnswerSelect.objects.filter(answerbase_ptr_id = q9id.id)
   	for e in q9qs:
   		q9 = e.body 
	q10id = qs.filter(question_id = 10)[0]
   	q10qs = AnswerSelect.objects.filter(answerbase_ptr_id = q10id.id)
   	for e in q10qs:
   		q10 = e.body
	q13id = qs.filter(question_id = 13)[0]
   	q13qs = AnswerSelect.objects.filter(answerbase_ptr_id = q13id.id)
   	for e in q13qs:
   		q13 = e.body
	q14id = qs.filter(question_id = 14)[0]
   	q14qs = AnswerSelect.objects.filter(answerbase_ptr_id = q14id.id)
   	for e in q14qs:
   		q14 = e.body
	q15id = qs.filter(question_id = 15)[0]
   	q15qs = AnswerSelect.objects.filter(answerbase_ptr_id = q15id.id)
   	for e in q15qs:
   		q15 = e.body
	q16id = qs.filter(question_id = 16)[0]
   	q16qs = AnswerSelect.objects.filter(answerbase_ptr_id = q16id.id)
   	for e in q16qs:
   		q16 = e.body
	q17id = qs.filter(question_id = 17)[0]
   	q17qs = AnswerSelect.objects.filter(answerbase_ptr_id = q17id.id)
   	for e in q17qs:
   		q17 = e.body
	return cars_db_filter(q1,q2,q9,q10,q13,q14,q15,q16,q17)




