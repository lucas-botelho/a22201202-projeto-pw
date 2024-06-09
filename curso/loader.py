from curso.models import *
import json

# curso = Curso.objects.create(
#     name='Example Course',
#     objectives='Example objectives of the course.',
#     presentation='Example presentation of the course.',
#     competences='Example competences of the course.'
# )

Curso.objects.all().delete()
Disciplina.objects.all().delete()
AreaCientifica.objects.all().delete()
Projeto.objects.all().delete()
LinguagemDeProgramacao.objects.all().delete()
Docente.objects.all().delete()

with open('curso/json/curso.json') as f:

    dados = json.load(f)
    detalhesCurso = dados["courseDetail"]

    scientificArea = AreaCientifica.objects.create(
        name = detalhesCurso["scientificArea"]
    )

    curso = Curso.objects.create(
        name=detalhesCurso["courseName"],
        objectives=detalhesCurso["objectives"],
        presentation=detalhesCurso["presentation"],
        competences=detalhesCurso["competences"]
    )

    disciplinas = dados["courseFlatPlan"]

    for d in disciplinas:
        Disciplina.objects.create(
            name = d["curricularUnitName"],
            year = d["curricularYear"],
            semester = d["semester"],
            ects = d["ects"],
            curricularIUnitReadableCode = d["curricularIUnitReadableCode"],
            scientificArea = scientificArea,
            course = curso
        )




    # print(dados)