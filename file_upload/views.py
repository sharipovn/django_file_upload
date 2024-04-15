# file_upload/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UploadedFile
from .forms import FileUploadForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
items_per_page =15  # Set the number of items per page

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_files = request.FILES.getlist('file')  # Get list of uploaded files
            for uploaded_file in uploaded_files:
                form = FileUploadForm(request.POST, request.FILES)  # Instantiate form inside loop
                if form.is_valid():
                    file_instance = form.save(commit=False)
                    file_instance.user = request.user
                    file_instance.file = uploaded_file
                    file_instance.save()
                    form.save_m2m()  # Save many-to-many relationships
            return redirect('uploaded_files')
            # uploaded_file = form.save(commit=False)
            # uploaded_file.user = request.user
            # uploaded_file.save()
            # form.save_m2m()  # Save many-to-many relationships
            # return redirect('uploaded_files')
    else:
        default_allowed_users = User.objects.all()  # Default to all users
        form = FileUploadForm(initial={'allowed_users': default_allowed_users})
    return render(request, 'upload_file.html', {'form': form})



@login_required
def uploaded_files(request):
    query = request.GET.get('q')
    if query:
        files = UploadedFile.objects.filter(user=request.user).filter(file__icontains=query).order_by('-uploaded_at')
    else:
        files = UploadedFile.objects.filter(user=request.user).order_by('-uploaded_at')
    count=len(files)
    paginator = Paginator(files, items_per_page)
    page = request.GET.get('page', 1)
    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)
    start_number = (files.number - 1) * paginator.per_page if files else 0
    return render(request, 'uploaded_files.html', {'files': files,'count':count,'start_number': start_number})


@login_required
def all_uploaded_files(request):
    query = request.GET.get('q')
    if request.user.is_superuser:
        if query:
            files = UploadedFile.objects.filter(file__icontains=query) | UploadedFile.objects.filter(user__username__icontains=query).order_by('-uploaded_at')
        else:
            files = UploadedFile.objects.all().order_by('-uploaded_at')
    else:
        if query:
            files = UploadedFile.objects.filter(allowed_users=request.user).filter(file__icontains=query) | UploadedFile.objects.filter(user__username__icontains=query).order_by('-uploaded_at')
        else:
            files = UploadedFile.objects.filter(allowed_users=request.user).order_by('-uploaded_at')
    count=len(files)
    paginator = Paginator(files, items_per_page)
    page = request.GET.get('page', 1)
    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)
    start_number = (files.number - 1) * paginator.per_page if files else 0
    return render(request, 'all_uploaded_files.html', {'files': files,'count':count,'start_number':start_number})

@login_required
def delete_file(request, file_id):
    file = get_object_or_404(UploadedFile, pk=file_id)
    if request.user == file.user or request.user.is_superuser:
        file.delete()
    return redirect('uploaded_files')



@login_required
def delete_file_from_all(request, file_id):
    file = get_object_or_404(UploadedFile, pk=file_id)
    if request.user == file.user or request.user.is_superuser:
        file.delete()
    return redirect('all_uploaded_files')