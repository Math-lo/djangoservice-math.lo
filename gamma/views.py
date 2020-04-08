from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from . import dbprocess

# Create your views here.

def index(request):
	template = loader.get_template('gamma/index.html')
	return HttpResponse(template.render(None, request))

def generalGroupQuestionnaire(request,id_group,id_cue):
	valueTopic = [0,0]
	nameCuest = ""
	try:
		valueTopic = dbprocess.getGradeGroupQuestionnaire(id_cue, id_group)
		nameCuest = dbprocess.getNameCuest(id_cue)
	except Exception as e:
		print("[X] Error in view generalGroupQuestionnaire: "+str(e))
	script = "google.charts.load('current', {'packages': ['corechart']});google.charts.setOnLoadCallback(drawChart);"
	script += "function drawChart(){var data = google.visualization.arrayToDataTable(["
	script += "['Campo', 'Calificaciones'],"
	script += "['Reprobados', {}],".format(valueTopic[1])
	script += "['Aprobados', {}]".format(valueTopic[0])
	script += "]);var options = {"
	script += "title: '{} Grupo {}',is3D: true,".format(nameCuest,id_group)
	script += "slices: {0: { color: '#5c6bc0' },1: { color: '#ff9800' }}"
	script += "};var chart = new"
	script += " google.visualization.PieChart(document.getElementById('Group:{}Cuestionario:{}'));".format(id_group,id_cue)
	script += "chart.draw(data, options);}"
	return HttpResponse(script)

def generalQuestionnaire(request,id_cue):
	nameCuest = ""
	valueTopic = [0,0]
	try:
		nameCuest = dbprocess.getNameCuest(id_cue)
		valueTopic = dbprocess.getGradeQuestionnaire(id_cue)
	except Exception as e:
		print("[X] Error en view generalQuestionnaire: "+str(e))
	script = "google.charts.load('current', {'packages': ['corechart']});google.charts.setOnLoadCallback(drawChart);"
	script += "function drawChart(){var data = google.visualization.arrayToDataTable(["
	script += "['Campo', 'Calificaciones'],"
	script += "['Reprobados', {} ],".format(valueTopic[1])
	script += "['Aprobados', {}]".format(valueTopic[0])
	script += "]);var options = {"
	script += "title: '{}',is3D: true,".format(nameCuest)
	script += "slices: {0: { color: '#5c6bc0' },1: { color: '#ff9800' }}"
	script += "};var chart = new"
	script += " google.visualization.PieChart(document.getElementById('Cuestionario:{}'));".format(id_cue)
	script += "chart.draw(data, options);}"
	return HttpResponse(script)

def generalGrades(request):
	valueTopic = [0,0]
	try:
		valueTopic = dbprocess.getGeneralGrades()
	except Exception as e:
		print("[X] Error en view generalGrades: "+str(e))
	script = "google.charts.load('current', {'packages': ['corechart']});google.charts.setOnLoadCallback(drawChart);"
	script += "function drawChart(){var data = google.visualization.arrayToDataTable(["
	script += "['Campo', 'Calificaciones'],"
	script += "['Reprobados', {}],".format(valueTopic[1])
	script += "['Aprobados', {}]".format(valueTopic[0])
	script += "]);var options = {"
	script += "title: 'Numero de Aprobados y Reprobados de Todos los Alumnos',is3D: true,"
	script += "slices: {0: { color: '#5c6bc0' },1: { color: '#ff9800' }}"
	script += "};var chart = new"
	script += " google.visualization.PieChart(document.getElementById('generalGrades'));"
	script += "chart.draw(data, options);}"
	return HttpResponse(script)

def generalColumnGroupTopic(request,id_group):
	temas = {}
	try:
		temasgrade = dbprocess.getGradeTopicGroup(id_group)
		dictCor = temasgrade[0]
		dictInc = temasgrade[1]
		dictCorOr = {}
		dictIncOr = {}
		for key in sorted(dictCor):
			dictCorOr[key] = dictCor[key]
		for key in sorted(dictInc):
			dictIncOr[key] = dictInc[key]
		for valcor in dictCorOr:
			if valcor not in temas.keys():
				temas[valcor] = [dictCorOr[valcor], 0]
			else:
				array = temas[valcor]
				array[0] = dictCorOr[valcor]
				temas[valcor] = array
		for valin in dictIncOr:
			if valin not in temas.keys():
				temas[valin] = [0, dictIncOr[valin]]
			else:
				array = temas[valin]
				array[1] = dictIncOr[valin]
				temas[valin] = array
	except Exception as e:
		print("[X] Error en view generalColumnGroupTopic: "+str(e))
	script = "google.charts.load('current', {'packages':['bar']}); google.charts.setOnLoadCallback(drawChart);"
	script += "function drawChart() { var data = google.visualization.arrayToDataTable(["
	script += "['Tema', 'Correctos', 'Incorrectos'],"
	for keys in temas:
		script += "['{}',{},{}],".format(dbprocess.getNameTopic(keys),str(temas[keys][0]),str(temas[keys][1]))
	script += "]);"
	script += "var options = { chart: {"
	script += "title: 'Temas del Grupo {}'".format(id_group)
	script += ",subtitle: 'Aciertos mas Correctos y Incorrectos en Temas',}, colors: ['#ff9800','#5c6bc0'] };"
	script += "var chart = new google.charts.Bar(document.getElementById('generalTopicGroup: {}'));".format(id_group)
	script += "chart.draw(data, google.charts.Bar.convertOptions(options));}"
	return HttpResponse(script)

def generalColumnTopic(request):
	temas = {}
	try:
		temasgrade = dbprocess.getGradesTopic()
		dictCor = temasgrade[0]
		dictInc = temasgrade[1]
		dictCorOr = {}
		dictIncOr = {}
		for key in sorted(dictCor):
			dictCorOr[key] = dictCor[key]
		for key in sorted(dictInc):
			dictIncOr[key] = dictInc[key]
		for valcor in dictCorOr:
			if valcor not in temas.keys():
				temas[valcor] = [dictCorOr[valcor], 0]
			else:
				array = temas[valcor]
				array[0] = dictCorOr[valcor]
				temas[valcor] = array
		for valin in dictIncOr:
			if valin not in temas.keys():
				temas[valin] = [0, dictIncOr[valin]]
			else:
				array = temas[valin]
				array[1] = dictIncOr[valin]
				temas[valin] = array
	except Exception as e:
		print("[X] Error en view generalColumnTopic: "+str(e))
	script = "google.charts.load('current', {'packages':['bar']}); google.charts.setOnLoadCallback(drawChart);"
	script += "function drawChart() { var data = google.visualization.arrayToDataTable(["
	script += "['Tema', 'Correctos', 'Incorrectos'],"
	for keys in temas:
		script += "['{}',{},{}],".format(dbprocess.getNameTopic(keys),str(temas[keys][0]),str(temas[keys][1]))
	script += "]);"
	script += "var options = { chart: {"
	script += "title: 'Temas'"
	script += ",subtitle: 'Aciertos mas Correctos y Incorrectos en Temas',}, colors: ['#ff9800','#5c6bc0']};"
	script += "var chart = new google.charts.Bar(document.getElementById('generalTopic'));"
	script += "chart.draw(data, google.charts.Bar.convertOptions(options));}"
	return HttpResponse(script)

def questionnaireGradeGroup(request,id_group,id_cue):
	temas = {}
	nameCuest = ""
	try:
		nameCuest = dbprocess.getNameCuest(id_cue)
		questionsgrade = dbprocess.getQuestionnaireGradeGroup(id_group, id_cue)
		dictCor = questionsgrade[0]
		dictInc = questionsgrade[1]
		dictCorOr = {}
		dictIncOr = {}
		for key in sorted(dictCor):
			dictCorOr[key] = dictCor[key]
		for key in sorted(dictInc):
			dictIncOr[key] = dictInc[key]
		for valcor in dictCorOr:
			if valcor not in temas.keys():
				temas[valcor] = [dictCorOr[valcor], 0]
			else:
				array = temas[valcor]
				array[0] = dictCorOr[valcor]
				temas[valcor] = array
		for valin in dictIncOr:
			if valin not in temas.keys():
				temas[valin] = [0, dictIncOr[valin]]
			else:
				array = temas[valin]
				array[1] = dictIncOr[valin]
				temas[valin] = array
	except Exception as e:
		print("[X] Error en view questionnaireGradeGroup"+str(e))
	script = "google.charts.load('current', {'packages':['bar']}); google.charts.setOnLoadCallback(drawChart);"
	script += "function drawChart() { var data = google.visualization.arrayToDataTable(["
	script += "['Preguntas', 'Correctos', 'Incorrectos'],"
	for keys in temas:
		script += "['{}',{},{}],".format(dbprocess.getNameQuestion(keys),str(temas[keys][0]),str(temas[keys][1]))
	script += "]);"
	script += "var options = { chart: {"
	script += "title: 'Aciertos del Grupo {} del {}'".format(id_group,nameCuest)
	script += ",subtitle: 'Aciertos mas Correctos y Incorrectos en Preguntas',}, colors: ['#ff9800','#5c6bc0']};"
	script += "var chart = new google.charts.Bar(document.getElementById('questions-Group:{} Cue:{}'));".format(id_group,id_cue)
	script += "chart.draw(data, google.charts.Bar.convertOptions(options));}"
	return HttpResponse(script)

def questionnaireGrades(request,id_cue):
	temas = {}
	nameCuest = ""
	try:
		nameCuest = dbprocess.getNameCuest(id_cue)
		questionsgrade = dbprocess.getQuestionnaireGrades(id_cue)
		dictCor = questionsgrade[0]
		dictInc = questionsgrade[1]
		dictCorOr = {}
		dictIncOr = {}
		for key in sorted(dictCor):
			dictCorOr[key] = dictCor[key]
		for key in sorted(dictInc):
			dictIncOr[key] = dictInc[key]
		for valcor in dictCorOr:
			if valcor not in temas.keys():
				temas[valcor] = [dictCorOr[valcor], 0]
			else:
				array = temas[valcor]
				array[0] = dictCorOr[valcor]
				temas[valcor] = array
		for valin in dictIncOr:
			if valin not in temas.keys():
				temas[valin] = [0, dictIncOr[valin]]
			else:
				array = temas[valin]
				array[1] = dictIncOr[valin]
				temas[valin] = array
	except Exception as e:
		print("[X] Error en view questionnaireGrades: "+str(e))
	script = "google.charts.load('current', {'packages':['bar']}); google.charts.setOnLoadCallback(drawChart);"
	script += "function drawChart() { var data = google.visualization.arrayToDataTable(["
	script += "['Preguntas', 'Correctos', 'Incorrectos'],"
	for keys in temas:
		script += "['{}',{},{}],".format(dbprocess.getNameQuestion(keys),str(temas[keys][0]),str(temas[keys][1]))
	script += "]);"
	script += "var options = { chart: {"
	script += "title: 'Aciertos del {}'".format(nameCuest)
	script += ",subtitle: 'Aciertos mas Correctos y Incorrectos en Preguntas',}, colors: ['#ff9800','#5c6bc0']};"
	script += "var chart = new google.charts.Bar(document.getElementById('generalQuestionsCue:{}'));".format(id_cue)
	script += "chart.draw(data, google.charts.Bar.convertOptions(options));}"
	return HttpResponse(script)

##POR ALUMNO###########################

def questionnaireAlumno(request,id_alumno,id_cue):
	nameCuest = ""
	answers = [[0], [0]]
	try:
		nameCuest = dbprocess.getNameCuest(id_cue)
		answers = dbprocess.getGradeQuestionnaireAlumno(id_alumno, id_cue)
	except Exception as e:
		nameCuest = ""
		answers = [[0], [0]]
		print("[X] Error en view questionnaireAlumno: "+str(e))
	script = "google.charts.load('current', {'packages': ['corechart']});google.charts.setOnLoadCallback(drawChart);"
	script += "function drawChart(){var data = google.visualization.arrayToDataTable(["
	script += "['Campo', 'Calificacion Cuestionario'],"
	if len(answers) > 0:
		script += "['Correctas', {}],".format(len(answers[0]))
		script += "['Incorrectas', {}]".format(len(answers[1]))
	else:
		script += "['Correctas', {}],".format(str(0))
		script += "['Incorrectas', {}]".format(str(0))
	script += "]);var options = {"
	script += "title: '{}',is3D: true,".format(nameCuest)
	script += "slices: {1: { color: '#5c6bc0' },0: { color: '#ff9800' }}"
	script += "};var chart = new"
	script += " google.visualization.PieChart(document.getElementById('questionnarie:{}alu:{}'));".format(id_cue,id_alumno)
	script += "chart.draw(data, options);}"
	return HttpResponse(script)

def questionnairesAlumnoTopic(request,id_alumno,id_tem):
	nameTopic = ""
	correctas = []
	incorrectas = []
	try:
		answers = dbprocess.getGradesQuestionnairesAlumno(id_alumno)
		nameTopic = dbprocess.getNameTopic(id_tem)
		for ans in answers[0]:
			if (dbprocess.getQuestionsTopic(ans) == id_tem):
				correctas.append(ans)
		for ans in answers[1]:
			if (dbprocess.getQuestionsTopic(ans) == id_tem):
				incorrectas.append(ans)
	except Exception as e:
		print("[X] Error en view questionnairesAlumnoTopic: "+str(e))
	script = "google.charts.load('current', {'packages': ['corechart']});google.charts.setOnLoadCallback(drawChart);"
	script += "function drawChart(){var data = google.visualization.arrayToDataTable(["
	script += "['Campo', 'Calificacion Cuestionario'],"
	script += "['Correctas', {}],".format(len(correctas))
	script += "['Incorrectas', {}]".format(len(incorrectas))
	script += "]);var options = {"
	script += "title: '{}',".format(nameTopic)
	script += "is3D: true,slices: {1: { color: '#5c6bc0' },0: { color: '#ff9800' }}"
	script += "};var chart = new"
	script += " google.visualization.PieChart(document.getElementById('topic:{}alu:{}'));".format(id_tem,id_alumno)
	script += "chart.draw(data, options);}"
	return HttpResponse(script)