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

def select_model(request) :
    modelName =request.GET.get('modelName')
    print('modelName', modelName)
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
    champs = [champ1, champ2, champ3, champ4, champ5, champ6, champ7, champ8, champ9, champ10]
    if modelName == 'cibl':
        return ci_bilstm(request,champs)
    elif modelName =='ctd':
        return ct_dnn(request,champs)
    elif modelName == 'ccd':
        return cc_dnn(request,champs)

def ci_bilstm(request,champs) :
    global ci_bilstm_model, le,champ_info_df
    champ_newkey_df = champ_info_df.copy()
    champ_newkey_df['key'] = le.transform(champ_info_df['key'])
    print("###",len(champ_newkey_df))
    for i in range(len(champ_newkey_df)) :
        name =champ_newkey_df.iloc[i]['name']
        for k,champ in enumerate(champs) :
            if name == champ :
                champs[k] = champ_newkey_df.iloc[i]['key']
    print('###',champs)

    data_test = np.array(champs).astype('float').reshape(1,-1)
    ci_bilstm_model.summary()
    result = ci_bilstm_model.predict(data_test)
    print('predict : ',result)
    teamA = round(float(result[0][0])*100,2)
    teamB = 100-teamA
    score ={"teamA":teamA, "teamB":teamB}
    context ={"score":score}
    return HttpResponse(json.dumps(context), content_type="application/json")

def ct_dnn(request,champs) :
    global champ_info_df,ct_dnn_model
    df = pd.read_excel('C:/PSJ/TEAM_EASY/tag_psj.xlsx', sheet_name='Sheet1')
    df.set_index('챔피언', inplace=True)
    for i in range(len(champ_info_df)) :
        name =champ_info_df.iloc[i]['name']
        for k,champ in enumerate(champs) :
            if name == champ :
                champs[k] = champ_info_df.iloc[i]['key']
    print('###',champs)
    teamA_df = df.loc[[champs[0], champs[1], champs[2], champs[3], champs[4]], :]
    teamB_df = df.loc[[champs[5], champs[6], champs[7], champs[8], champs[9]], :]
    teamA_tag = teamA_df.sum()
    teamB_tag = teamB_df.sum()
    test = pd.concat([teamA_tag, teamB_tag])
    test = pd.DataFrame(test).transpose()
    test = test.values
    test = np.array(test).astype('float').reshape(1, -1)
    print(test)
    result=ct_dnn_model.predict(test)
    teamA = round(float(result[0][0]) * 100, 2)
    teamB = 100 - teamA
    score = {"teamA": teamA, "teamB": teamB}
    context = {"score": score}
    return HttpResponse(json.dumps(context), content_type="application/json")

def cc_dnn(request,champs) :
    global champ_info_df, cc_dnn_model
    for i in range(len(champ_info_df)) :
        name =champ_info_df.iloc[i]['name']
        for k,champ in enumerate(champs) :
            if name == champ :
                champs[k] = champ_info_df.iloc[i]['key']
    print('###',champs)
    champ_df=pd.read_csv('C:/PSJ/TEAM_EASY/champClass.csv')
    champ_df = champ_df.set_index('championId')
    print('###',champ_df)
    teamA_df = champ_df.loc[list(champs[:5]), :]
    teamB_df = champ_df.loc[list(champs[5:]), :]
    teamA_class = teamA_df.sum()
    teamB_class = teamB_df.sum()
    teamAB_class = pd.concat([teamA_class, teamB_class])
    test_data = pd.DataFrame(teamAB_class).transpose()
    test_data = test_data.values
    test_data = np.array(test_data).astype('float').reshape(1, -1)
    result = cc_dnn_model.predict(test_data)
    teamA = round(float(result[0][0]) * 100, 2)
    teamB = 100 - teamA
    score = {"teamA": teamA, "teamB": teamB}
    context = {"score": score}
    return HttpResponse(json.dumps(context), content_type="application/json")

def makeModels():
    global le,ci_bilstm_model,champ_info_df,ct_dnn_model,cc_dnn_model
    # 전체 챔피언 정보 불러오기
    rows = Championdto.objects.all().values('name', 'key')
    # 데이터프레임으로 변환
    champ_info_df = pd.DataFrame(rows)
    # 챔피언아이디를 정수로 인코딩(이미 정수이지만 연속된 정수로 변환)하기 위해 어떤 범위의 데이터인지 학습
    le = LabelEncoder()
    le.fit(champ_info_df['key'])

    ci_bilstm_model = load_model('C:/PSJ/TEAM_EASY/models/championid_bilstm_model.h5')
    ct_dnn_model = load_model('C:/PSJ/TEAM_EASY/models/tag_dnn_model.h5')
    cc_dnn_model = load_model('C:/PSJ/TEAM_EASY/models/class_dnn_model.h5')

# 미리 준비 되야 하는 것들
ci_bilstm_model,ct_dnn_model,cc_dnn_model, le,champ_info_df = None, None,None,None,None

makeModels()