from django.shortcuts import render
from django.http import HttpResponse
from .models import Championdto
from django.core import serializers
import json

from tensorflow.keras.layers import Dense, LSTM,Embedding,Bidirectional,Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import pandas as pd
import sklearn
import numpy as np
from sklearn.preprocessing import LabelEncoder
# Create your views here.

def index(request) :
    rows = Championdto.objects.all()
    champions = serializers.serialize('json', rows)
    team_a = 50.00
    team_b = 100-team_a
    score={"team_a":team_a,"team_b":team_b}
    context = {'champions':champions,'score':score}
    return render(request,'prediction/main.html',context)

def ci_bilstm(request) :
    global ci_bilstm_model, le,champ_info_df
    #파라미터에서
    champ1 = request.GET.get('champ1')
    champ2 = request.GET.get('champ2')
    champ3 = request.GET.get('champ3')
    champ4 = request.GET.get('champ4')
    champ5 = request.GET.get('champ5')
    champ6 = request.GET.get('champ6')
    champ7 = request.GET.get('champ7')
    champ8 = request.GET.get('champ8')
    champ9 = request.GET.get('champ9')
    champ10 = request.GET.get('champ10')
    champ_info_df[]
    data_test = np.array([champ1,champ2,champ3,champ4,champ5,champ6,champ7,champ8,champ9,champ10]).astype('int')
    modelName = request.GET.get('modelName')
    print('predict : ',ci_bilstm_model.predict_classes(data_test))
    teamA = 52.11
    teamB = 100-teamA
    score ={"teamA":teamA, "teamB":teamB}
    context ={"score":score}
    return HttpResponse(json.dumps(context), content_type="application/json")

def ct_dnn() :
    pass

def cc_dnn() :
    pass
def makeModels():
    global le,ci_bilstm_model,champ_info_df
    # 전체 챔피언 정보 불러오기
    rows = Championdto.objects.all().values('name', 'key')
    # 데이터프레임으로 변환
    champ_info_df = pd.DataFrame(rows)
    # 챔피언아이디를 정수로 인코딩(이미 정수이지만 연속된 정수로 변환)하기 위해 어떤 범위의 데이터인지 학습
    le = LabelEncoder()
    le.fit(df['key'])
    champ_info_df['key'] = le.transform(df['key'])
    ci_bilstm_model = load_model('C:\PSJ\TEAM_EASY\models\championid_bilstm_model.h5')


# 미리 준비 되야 하는 것들
ci_bilstm_model, le,champ_info_df = None, None,None

makeModels()