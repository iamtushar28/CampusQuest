from django.shortcuts import render
from custom_admin.models import QuestionPaper
from django.http import JsonResponse


#Home page view
def home(request):
    return render(request, 'index.html')


#contribution page view
def contribute(request):
    return render(request, 'contribute.html')    
 
 
#Get papers page view
def papers(request):
    papers = QuestionPaper.objects.all()

    branch = request.GET.get('branch')
    year = request.GET.get('year')

    if branch and branch != 'all':
        papers = papers.filter(branch=branch)
    if year and year != 'all':
        papers = papers.filter(year=year)

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        papers_data = list(papers.values('paper_name', 'branch', 'year', 'pdf'))
        return JsonResponse({'papers': papers_data})    

    return render(request, 'pyq.html', {'papers': papers})

