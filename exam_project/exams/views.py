from django.shortcuts import render
from .models import abexam

def abexam_list(request):
    exams = abexam.objects.filter(is_public=True)
    context = {
        'exams': exams,
        'full_name': 'Барладина Ангелина Александровна',
        'group_number': '241-671'
    }
    return render(request, 'exams/abexam_list.html', context)