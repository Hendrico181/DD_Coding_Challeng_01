from django.shortcuts import render, redirect
from .models import Note

# Create your views here.


def notes_home_view(request):
    note_queryset = Note.objects.all()
    context = {
        'notes': note_queryset
    }
    return render(request, 'notes/notes.html', context=context)


def note_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(title=title, content=content)
        return redirect('/notes')
    context = {
        'button': "Create"
    }
    return render(request, 'notes/create.html', context=context)


def note_edit_view(request, id):
    note = Note.objects.get(id=id)
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
    context = {
        'note': note,
        'button': "Edit"
    }
    return render(request, 'notes/create.html', context=context)


def delete_view(request, id):
    Note.objects.filter(id=id).delete()
    return redirect('/notes')


def note_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        note_obj = Note.objects.get(id=id)
    context = {
        'object': note_obj,
    }

    return render(request, "notes/detail.html", context=context)
