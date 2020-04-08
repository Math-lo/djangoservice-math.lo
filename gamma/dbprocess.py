import mysql.connector as MySQLdb

host = 'localhost'
user = 'root'
passwd= ''
datab = 'mychemis_algebrae_v01'

def getIdsTopic():
    ids = []
    try:
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=datab)
        cursor = db.cursor()
        query = ("select * from  ctemas")
        cursor.execute(query)
        registro = cursor.fetchall()
        for r in registro:
            ids.append(r[0])
        if db.is_connected():
            cursor.close()
            db.close()
    except Exception as e:
        print('Error in getIdsTopic: ' + str(e))
    return ids

def getAlumnosGroup(id_group):
    alumnos = []
    try:
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=datab)
        cursor = db.cursor()
        query = ("select * from eusuariosgrupo where id_gru = %s")
        data = (id_group)
        cursor.execute(query, (data,))
        registro = cursor.fetchall()
        for r in registro:
            alumnos.append(r[1])
        if db.is_connected():
            cursor.close()
            db.close()
    except Exception as e:
        print('Error in getAlumnosGroup: '+str(e))
    return alumnos

def getNameTopic(id_topic):
    topic = ''
    try:
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=datab)
        cursor = db.cursor()
        query = ("select * from ctemas where id_tem = %s")
        data = (id_topic)
        cursor.execute(query, (data,))
        registro = cursor.fetchall()
        for r in registro:
            topic = r[1]
        if db.is_connected():
            cursor.close()
            db.close()
    except Exception as e:
        print('Error in getTopicId: ' + str(e))
    return topic

def getNameQuestion(id_bpr):
    name = ''
    try:
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=datab)
        cursor = db.cursor()
        query = ("select * from mbancopreguntas where id_bpr = %s")
        data = (id_bpr)
        cursor.execute(query, (data,))
        registro = cursor.fetchall()
        for r in registro:
            name = r[1]
        if db.is_connected():
            cursor.close()
            db.close()
    except Exception as e:
        print('Error in getTopicId: ' + str(e))
    return name

def getIdAlumno(correo_alumno):
    id_alumno = ''
    try:
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=datab)
        cursor = db.cursor()
        query = ("select * from  musuario where cor_usu = %s")
        data = (id_alumno)
        cursor.execute(query, data)
        registro = cursor.fetchall()
        for r in registro:
            id_alumno = r[0]
        if db.is_connected():
            cursor.close()
            db.close()
    except Exception as e:
        print('Error in getGradeTopicAlumno: ' + str(e))
    return id_alumno

def getNameCuest(id_cue):
    name = ''
    try:
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=datab)
        cursor = db.cursor()
        query = ("select * from ecuestionario where id_cue = %s")
        data = (id_cue)
        cursor.execute(query, (data,))
        registro = cursor.fetchall()
        for r in registro:
            name = r[1]
        if db.is_connected():
            cursor.close()
            db.close()
    except Exception as e:
        print('Error in getNameId: ' + str(e))
    return name


def getGradeGroupQuestionnaire(id_cue,id_group):
    aprp = []
    alumnos = getAlumnosGroup(id_group)
    Aprobados = 0
    Reprobados = 0
    try:
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=datab)
        cursor = db.cursor()
        query = ("select * from dpuntajealumnocuestionario where id_cue = %s")
        data = (id_cue)
        cursor.execute(query, (data,))
        registro = cursor.fetchall()
        for r in registro:
            if r[1] in alumnos:
                correct = str(r[3]).strip().split(',')
                incorrect = str(r[4]).strip().split(',')
                total = len(correct)+len(incorrect)
                if (len(correct)/total)*100 > 60:
                    Aprobados = Aprobados + 1
                else:
                    Reprobados = Reprobados + 1
        if db.is_connected():
            cursor.close()
            db.close()
    except Exception as e:
        print('Error in getGradeGroupQuestionnaire: ' + str(e))
    aprp.append(Aprobados)
    aprp.append(Reprobados)
    return aprp

def getGradeQuestionnaire(id_cue):
    aprp = []
    Aprobados = 0
    Reprobados = 0
    try:
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=datab)
        cursor = db.cursor()
        query = ("select * from dpuntajealumnocuestionario where id_cue = %s")
        data = (id_cue)
        cursor.execute(query, (data,))
        registro = cursor.fetchall()
        for r in registro:
            correct = str(r[3]).strip().split(',')
            incorrect = str(r[4]).strip().split(',')
            total = len(correct)+len(incorrect)
            if (len(correct)/total)*100 > 60:
                Aprobados = Aprobados + 1
            else:
                Reprobados = Reprobados + 1
        if db.is_connected():
            cursor.close()
            db.close()
    except Exception as e:
        print('Error in getGradeQuestionnaire: ' + str(e))
    aprp.append(Aprobados)
    aprp.append(Reprobados)
    return aprp

def getGeneralGrades():
    aprp = []
    Aprobados = 0
    Reprobados = 0
    try:
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=datab)
        cursor = db.cursor()
        query = ("select * from dpuntajealumnocuestionario")
        cursor.execute(query)
        registro = cursor.fetchall()
        for r in registro:
            correct = str(r[3]).strip().split(',')
            incorrect = str(r[4]).strip().split(',')
            total = len(correct)+len(incorrect)
            if (len(correct)/total)*100 > 60:
                Aprobados = Aprobados + 1
            else:
                Reprobados = Reprobados + 1
        if db.is_connected():
            cursor.close()
            db.close()
    except Exception as e:
        print('Error in getGeneralGrades: ' + str(e))
    aprp.append(Aprobados)
    aprp.append(Reprobados)
    return aprp

def getGradeTopicGroup(id_group):
    temasgrades = []
    temascorrect = {}
    temasincorrect = {}
    try:
        alumnos = getAlumnosGroup(id_group)
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=datab)
        cursor = db.cursor()
        for alu in alumnos:
            query = ("select * from dpuntajealumnocuestionario where id_usu = %s")
            data = (alu)
            cursor.execute(query, (data,))
            registro = cursor.fetchall()
            for r in registro:
                correct = str(r[3]).strip().split(',')
                incorrect = str(r[4]).strip().split(',')
                for question in correct:
                    if str(question).strip() != '':
                        topic = getQuestionsTopic(question)
                        if topic not in temascorrect.keys():
                            temascorrect[topic] = 1
                        else:
                            value = int(temascorrect[topic]) +1
                            temascorrect[topic] = value
                for question in incorrect:
                    if str(question).strip() != '':
                        topic = getQuestionsTopic(question)
                        if topic not in temasincorrect.keys():
                            temasincorrect[topic] = 1
                        else:
                            value = int(temasincorrect[topic]) + 1
                            temasincorrect[topic] = value
        temasgrades.append(temascorrect)
        temasgrades.append(temasincorrect)
        if db.is_connected():
            cursor.close()
            db.close()
    except Exception as e:
        print('Error in getGradeTopicGroup: ' + str(e))
    return temasgrades

def getGradesTopic():
    temasgrades = []
    temascorrect = {}
    temasincorrect = {}
    try:
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=datab)
        cursor = db.cursor()
        query = ("select * from dpuntajealumnocuestionario")
        cursor.execute(query)
        registro = cursor.fetchall()
        for r in registro:
            correct = str(r[3]).strip().split(',')
            incorrect = str(r[4]).strip().split(',')
            for question in correct:
                if str(question).strip() != '':
                    topic = getQuestionsTopic(question)
                    if topic not in temascorrect.keys():
                        temascorrect[topic] = 1
                    else:
                        value = int(temascorrect[topic]) +1
                        temascorrect[topic] = value
            for question in incorrect:
                if str(question).strip() != '':
                    topic = getQuestionsTopic(question)
                    if topic not in temasincorrect.keys():
                        temasincorrect[topic] = 1
                    else:
                        value = int(temasincorrect[topic]) + 1
                        temasincorrect[topic] = value
        temasgrades.append(temascorrect)
        temasgrades.append(temasincorrect)
        if db.is_connected():
            cursor.close()
            db.close()
    except Exception as e:
        print('Error in getGradesTopic: ' + str(e))
    return temasgrades

def getQuestionnaireGradeGroup(id_group,id_cue):
    questionsgrades = []
    questioncorrect = {}
    questionincorrect = {}
    try:
        alumnos = getAlumnosGroup(id_group)
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=datab)
        cursor = db.cursor()
        for alu in alumnos:
            query = ("select * from dpuntajealumnocuestionario where id_usu = %s and id_cue = %s")
            data = (alu,id_cue)
            cursor.execute(query, data)
            registro = cursor.fetchall()
            for r in registro:
                correct = str(r[3]).strip().split(',')
                incorrect = str(r[4]).strip().split(',')
                for question in correct:
                    if str(question).strip() != '':
                        if question not in questioncorrect.keys():
                            questioncorrect[question] = 1
                        else:
                            value = int(questioncorrect[question]) + 1
                            questioncorrect[question] = value
                for question in incorrect:
                    if str(question).strip() != '':
                        if question not in questionincorrect.keys():
                            questionincorrect[question] = 1
                        else:
                            value = int(questionincorrect[question]) + 1
                            questionincorrect[question] = value
        questionsgrades.append(questioncorrect)
        questionsgrades.append(questionincorrect)
        if db.is_connected():
            cursor.close()
            db.close()
    except Exception as e:
        print('Error in getGradeQuestionnaireGroup: ' + str(e))
    return questionsgrades

def getQuestionnaireGrades(id_cue):
    questionsgrades = []
    questioncorrect = {}
    questionincorrect = {}
    try:
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=datab)
        cursor = db.cursor()
        query = ("select * from dpuntajealumnocuestionario where id_cue = %s")
        data = (id_cue)
        cursor.execute(query, (data,))
        registro = cursor.fetchall()
        for r in registro:
            correct = str(r[3]).strip().split(',')
            incorrect = str(r[4]).strip().split(',')
            for question in correct:
                if str(question).strip() != '':
                    if question not in questioncorrect.keys():
                        questioncorrect[question] = 1
                    else:
                        value = int(questioncorrect[question]) + 1
                        questioncorrect[question] = value
            for question in incorrect:
                if str(question).strip() != '':
                    if question not in questionincorrect.keys():
                        questionincorrect[question] = 1
                    else:
                        value = int(questionincorrect[question]) + 1
                        questionincorrect[question] = value
        questionsgrades.append(questioncorrect)
        questionsgrades.append(questionincorrect)
        if db.is_connected():
            cursor.close()
            db.close()
    except Exception as e:
        print('Error in getGradesQuestionnaire: ' + str(e))
    return questionsgrades




##FUNCIONES CENTRADAS POR ALUMNO##################

def getGradeQuestionnaireAlumno(id_alumno,id_cue):
    answers = []
    try:
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=datab)
        cursor = db.cursor()
        query = ("select * from  dpuntajealumnocuestionario where id_usu = %s and id_cue = %s")
        data = (id_alumno,id_cue)
        cursor.execute(query, data)
        registro = cursor.fetchall()
        for r in registro:
            correct = []
            incorrect = []
            data = str(r[3]).split(",")
            for answer in data:
                correct.append(answer)
            data = str(r[4]).split(",")
            for answer in data:
                incorrect.append(answer)
            answers.append(correct)
            answers.append(incorrect)
        if db.is_connected():
            cursor.close()
            db.close()
    except Exception as e:
        print('Error in getGradeQuestionnaireAlumno: ' + str(e))
    return answers

def getGradesQuestionnairesAlumno(id_alumno):
    answers = []
    try:
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=datab)
        cursor = db.cursor()
        query = ("select * from  dpuntajealumnocuestionario where id_usu = %s")
        data = (id_alumno)
        cursor.execute(query, (data,))
        registro = cursor.fetchall()
        correct = []
        incorrect = []
        for r in registro:
            data = str(r[3]).split(",")
            for answer in data:
                correct.append(answer.strip())
            data = str(r[4]).split(",")
            for answer in data:
                incorrect.append(answer.strip())
        answers.append(correct)
        answers.append(incorrect)
        if db.is_connected():
            cursor.close()
            db.close()
    except Exception as e:
        print('Error in getGradesQuestionnairesAlumno: ' + str(e))
    return answers

def getQuestionsTopic(id_bpr):
    id_topic = ''
    try:
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=datab)
        cursor = db.cursor()
        query = ("select * from mbancopreguntas where id_bpr = %s")
        data = (id_bpr)
        cursor.execute(query, (data,))
        registro = cursor.fetchall()
        for r in registro:
            id_topic = r[7]
        if db.is_connected():
            cursor.close()
            db.close()
    except Exception as e:
        print('Error in getQuestionTopic: ' + str(e))
    return id_topic

