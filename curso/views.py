from django.shortcuts import redirect, render
from curso.forms import *
from .models import *
from django.contrib.auth.decorators import login_required


class DisciplinaViewModel:
    def __init__(self, disciplina, projetos):
        self.info = disciplina
        self.projetos = projetos

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/cursos.html', {'cursos': cursos})

def curso_detail_view(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    disciplinas = Disciplina.objects.filter(course = curso)
    disciplinasLista = []

    for d in disciplinas:
        disciplinasLista.append(DisciplinaViewModel(d, Projeto.objects.filter(disciplina = d)))

    return render(request, 'curso/curso_detail.html', {'curso': curso, 'disciplinasLista': disciplinasLista})


def projeto_detail_view(request, projeto_id):
    projeto = Projeto.objects.get(pk=projeto_id)
    return render(request, 'curso/projeto_detail.html', {'projeto': projeto})

@login_required
def create_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso:index')  
    else:
        form = CursoForm()
    return render(request, 'curso/curso_form.html', {'form': form})

@login_required
def update_curso(request, pk):
    curso = Curso.objects.get(pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso:index') 
    else:
        form = CursoForm(instance=curso)
    return render(request, 'curso/curso_form.html', {'form': form})

@login_required
def delete_curso(request, pk):
    curso = Curso.objects.get(pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('curso:index')  
    return render(request, 'curso/curso_confirm_delete.html', {'curso': curso})

@login_required
def create_area_cientifica(request):
    if request.method == 'POST':
        form = AreaCientificaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso:index')
    else:
        form = AreaCientificaForm()
    return render(request, 'curso/area_cientifica_form.html', {'form': form})

@login_required
def update_area_cientifica(request, pk):
    area_cientifica = AreaCientifica.objects.get(pk=pk)
    if request.method == 'POST':
        form = AreaCientificaForm(request.POST, instance=area_cientifica)
        if form.is_valid():
            form.save()
            return redirect('curso:index')
    else:
        form = AreaCientificaForm(instance=area_cientifica)
    return render(request, 'curso/area_cientifica_form.html', {'form': form})

@login_required
def delete_area_cientifica(request, pk):
    area_cientifica = AreaCientifica.objects.get(pk=pk)
    if request.method == 'POST':
        area_cientifica.delete()
        return redirect('curso:index')
    return render(request, 'curso/area_cientifica_confirm_delete.html', {'object': area_cientifica})

@login_required
def docente_create(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso:index')  # Change this to your desired URL name
    else:
        form = DocenteForm()
    return render(request, 'curso/docente_form.html', {'form': form})

@login_required
def docente_update(request, pk):
    docente = Docente.objects.get(pk=pk)
    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('curso:index')  
    else:
        form = DocenteForm(instance=docente)
    return render(request, 'curso/docente_form.html', {'form': form})

@login_required
def docente_delete(request, pk):
    docente = Docente.objects.get(pk=pk)
    if request.method == 'POST':
        docente.delete()
        return redirect('curso:index')  
    return render(request, 'curso/docente_confirm_delete.html', {'object': docente})


@login_required
def create_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso:index')
    else:
        form = DisciplinaForm()
    return render(request, 'curso/disciplina_form.html', {'form': form})

@login_required
def update_disciplina(request, pk):
    disciplina = Disciplina.objects.get(pk=pk)

    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('curso:index')
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request, 'curso/disciplina_form.html', {'form': form})

@login_required
def delete_disciplina(request, pk):
    disciplina = Disciplina.objects.get(pk=pk)
    if request.method == 'POST':
        disciplina.delete()
        return redirect('curso:index')
    return render(request, 'curso/disciplina_confirm_delete.html', {'disciplina': disciplina})
