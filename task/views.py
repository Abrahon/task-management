from django.shortcuts import render,redirect
from task.forms import TaskStoreForm,TaskStoreModel
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def hostel(request):
    data = TaskStoreModel.objects.filter(is_available=True)
    context = {'data': data}
    return render(request, 'show_task.html', context)

def add_task(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            task = TaskStoreForm(request.POST, request.FILES)
            if task.is_valid():
                task.save()
                print(task.cleaned_data)
                return redirect('show_task')
                
        
        else:
            task = TaskStoreForm()    
        return render(request,'add_task.html',{'form':task})
    else:
        return redirect('signup')

def show_task(request):
    if request.user.is_authenticated:
        task = TaskStoreModel.objects.all().order_by('priority')
        print(task)
        return render(request,'show_task.html',{'data':task})
    else:
        return redirect('signup')

def edit_task(request, id):
    task = TaskStoreModel.objects.get(pk=id)
    form = TaskStoreForm(instance=task)
    if request.method == 'POST':
        form =TaskStoreForm(request.POST, request.FILES, instance=task) 
        if form.is_valid():
            form.save(commit=True)
            return redirect('show_task')
    return render(request,'add_task.html',{'form':form})
    
        
def delete_task(request,id):
    task = TaskStoreModel.objects.get(pk=id).delete()
    return redirect('show_task')

def details_task(request, id):
    single_task = TaskStoreModel.objects.get(pk=id)
    context = {
        'single_task': single_task,  
    }
    return render(request,'details.html',context)

def complete_task(request, id):
    task = TaskStoreModel.objects.get(pk=id)
    task.status = True
    task.save()
    return redirect('show_task')

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
    
    if keyword:
        data = TaskStoreModel.objects.order_by('-created_date').filter(Q(title__icontains=keyword) | Q(priority__icontains=keyword ))
        print(data)
        
        data_count = data.count()
        context = {
            'data' :data,
            'd_count' : data_count,
        }  
    return render(request, 'show_task.html',context)