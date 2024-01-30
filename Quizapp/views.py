from django.shortcuts import render,redirect
from .models import NewUser,SportsQuestion as sports ,PlantsAndAnimalQuestion as plantsAndanimal,ZoologyQuestion as zoology, HistoryQuestion as history, CurrentAffairsQuestion as currentAffairs,Feedback,UserResult
import random as r
from json import dumps
from django.http import JsonResponse

# Create your views here.

def home(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user = NewUser(user_name=user_name)
        user.save()
        current_user = NewUser.objects.last().pk
        request.session['uid'] = current_user
        return redirect('questions')
    return render(request,'home.html')


# Question Page
def questions(request):
    current_userid = request.session.get('uid')

    # Checking for currend user
    if current_userid:
        current_user_name = NewUser.objects.get(pk=current_userid).user_name
              
        questions = []
        catagery = [sports,plantsAndanimal,zoology,history,currentAffairs]
        for i in range(0,5):
            # Find the Random no
            random_no = r.randrange(1,20)
            random_question_no = catagery[i].objects.get(question_no=random_no)
            # Get the question details
            question_detail = {
                    'catagery' : random_question_no.catagery,
                    'question' : random_question_no.question,
                    'opt1' : random_question_no.opt1,
                    'opt2' : random_question_no.opt2,
                    'opt3' : random_question_no.opt3,
                    'opt4' : random_question_no.opt4,
                    'correct_opt' : random_question_no.correct_opt,
                    'related_img' : str(random_question_no.related_img)
                    }
            question_detail['question_no'] = i + 1
            # Add to the list
            questions.append(question_detail)
        
        # Save user result
        if request.method == 'POST':
            user_name = request.POST.get('user_name')
            score = request.POST.get('score')
            result = UserResult(user_id=current_userid,user_name=user_name,score=score)
            result.save()
            response = {'url' : "/result"}
            return JsonResponse(response)
        
        context = {
            'user':current_user_name,
            'questions':questions,
            'questions_json':dumps(questions),
            }
        return render(request,'questions.html',context=context)
    else:
        return redirect('home')

def result(request):
    current_userid = request.session.get('uid')
    print(current_userid)

    # Checking for currend user
    if current_userid:

        user_querry = UserResult.objects.get(user_id=current_userid)
        print(user_querry)
        if user_querry:
            score = user_querry.score
            context = {
                'user_name' : user_querry.user_name,
                'score' : score
                }
        else:
            return redirect('home')
        
        if request.method == 'POST':
            user_id = user_querry.user_id
            user_name = request.POST.get('user_name')
            feedback = request.POST.get('feedback')
            feedback = Feedback(user_id=user_id,user_name=user_name,feedback=feedback)
            feedback.save()
            return redirect('home')
    else:
        return redirect('home')
    return render(request,'result.html',context=context)


def FeedbackResult(request):
    data = Feedback.objects.all()
    context = {
        'data' : data
    }
    return render(request,'feedback_result.html',context=context)