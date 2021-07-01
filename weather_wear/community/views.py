from django.shortcuts import render, redirect, get_object_or_404
from .models import Community
from django.utils import timezone

def show(request):
    communities = Community.objects.all()
    return render(request, 'community/show.html', {'communities':communities})

def detail(request, id):
    community = get_object_or_404(Community, id = id)
    return render(request, 'community/detail.html', {'community':community})

def new(request):
    return render(request, 'community/new.html')    

def create(request):
    new_community = Community()
    new_community.title = request.POST['title']
    new_community.writer = request.POST['writer']
    new_community.pub_date = timezone.now()
    new_community.body = request.POST['body']
    new_community.image = request.FILES.get('image')
    new_community.save()
    return redirect('community:detail', new_community.id)

def edit(request, id):
    edit_community = Community.objects.get(id = id)
    return render(request, 'community/edit.html', {'community': edit_community})

def update(request, id):
    update_community = Community.objects.get(id = id)
    update_community.title = request.POST['title']
    update_community.writer = request.POST['writer']
    update_community.pub_date = timezone.now()
    update_community.body = request.POST['body']
    update_community.save()
    return redirect('community:detail', update_community.id)

def delete(request, id):
    delete_community = Community.objects.get(id = id)
    delete_community.delete()
    return redirect('community:show')
