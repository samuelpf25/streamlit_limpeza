#Atualizado em 06/02/2024

from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
# import json
#
# def escrever_json(dados):
# 	with open('controle.json','w',encoding='utf8') as f:
# 		json.dump(dados,f,ensure_ascii=False,sort_keys=True,indent=4,separators=(',',':'))
#
# variavel="-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC00DwYUXNE169X\nF+aR3cW6/NenD2ZYO5R6doc7ijOSOyv+yDTS01JKBynaAxM9JIP9KRQgMZgPxoWW\nltA7qFHqsO5X78exh5jtDXp71p/nmZTzWfDUVsY33ciKbgb8c4EmD8VY9SoOxzuf\nQLlWLFtmwM77dX7ZWeXGe9GmpO2eQ847YqVE4ClVIcDWco05n3vzTAKVeT1Rm6Kw\nZ2NSxp4aPjFM0Zc+Y2U0m30Og7HqWvwpLOcfpffZezXInFJdYW+/14MQ4Xvozfsn\nHlFe2XuSgrvkUD1QYpPmFxhdHKUy3go36iBlKgWos5t85x2X1kFnPHAHKanUhSO4\n7cJqG69zAgMBAAECggEAUgIqZ4s1wVEkJVfhS2JvZs58DzkEXdt0DhFJZ79YgagV\n3cK3drHDHnFeUZPYe4Be3wltJ+bmha0wdOslOhGvSceC6t6Fz6blPQtCdP2U3CoD\n7VXrTZun3rnYVbTutTy8JGO9ygm0UCycBbCI/yUyNYoYtuOFK5bDCUGqhq9CWOe6\nLyXKJY/SQF5rVNV+Il54VHzkc1ofgIF2hmNI9kxhfDg1FTmoZstFWHU9gg0Yxa6i\n+sLSrDTOtJq7uGlSVx74i+FKKNf5WbJM4zSTJySMfVisTpTTOMgcRoFkpEAYizBA\niBEtfHxdC7HJK63t111htY7Bi6uLk4XW7aI3PnJ2sQKBgQD15ZQmXcbJlwcK4WpF\n6ixhSX9npApVnVX3ergQd/8OXqdq9R1zsZHaEA1GDSCt/kH42nl9rCUtDAsk6JOU\ngGbfBMVLBDXP1V0vsZPL0chXGT4gykaTmJSdHYgNr0ArowMGWV3EDIw3uua5frbW\nifK1ngHKb1t7NQkpSBAnbHj/MQKBgQC8PhaWeM8GSKEgoOLbm97+nOv3yYf+jUVl\nsQZnuMdvI2ApKYEqRtu7FyqxvRJ2/8K6W1UoepL1+0yoTl8x/3gGgKv2mj/D89Gc\nUI9G5wNtEZgzd1orVp58zf79MfX6Xwd2Qb11rrht8EpvlNuXZr3GjskVIPqf2ZWd\nFAA9ySQX4wKBgArA2XO8Eh9qvWIabX1VOk+e2TV9FP6dfM7vzPDbbooAVa31vi37\nC/fPT+VKWa2COvxZAYsfZhjMOAiLKzkJTHZgTQh0zK2kFQkq6N229N3qOq9QaTm3\nKHiee/6tNU8zN8SlT9Zs/gzJ3aErC2/iZHzQxh9GM2f178qgXiR7N+dhAoGAepB2\nhoysRuwdNTBr5Q9NFzy3C0QFrwDukXK8t+YAvGUtJD/o4Mz4Ho3L96QilKacdFgp\nT0zXyR9RXziAFP7AeINo9AykvgJPlVaCo2igu3A8SC5K4HLqiFpbzyGrhdQ/+Ih/\nQlN7s+FDpfknLSHxKIopdP9fD5tNJdQzAAep338CgYBJ0sfhzjF6cJYa7/kq1Ds9\nYkn+zOjU1xCnMqEihDoNYvMwR27rG52k74uUHsIfx80nFZGv/rP4exvqt4xjLsNZ\n8qufgQipIDALPGFBkI/VBCv3tpDnxAppdDjN3vFKAYIU05EOTt79vLp98tJWOlkO\nmjwHRIDo2TvUi/eX0DlpSA==\n-----END PRIVATE KEY-----\n"
# dicionario={
#   "type": "service_account",
#   "project_id": "manutencao747400",
#   "private_key_id": "5706169c3e79c70baa4382deaa85c7ed868838e6",
#   "private_key": variavel,
#   "client_email": "sheets-coinfra@manutencao747400.iam.gserviceaccount.com",
#   "client_id": "106481092352500366115",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/sheets-coinfra%40manutencao747400.iam.gserviceaccount.com"
# }
# escrever_json(dicionario)
#https://pt.linkedin.com/pulse/manipulando-planilhas-do-google-usando-python-renan-pessoa
#documentação -> https://gspread.readthedocs.io/en/latest/api.html#models
#scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
scope = ['https://spreadsheets.google.com/feeds']
k="456"
creds = ServiceAccountCredentials.from_json_keyfile_name("controle.json", scope)

cliente = gspread.authorize(creds)

#sheet = cliente.open("Ciente Limpeza").sheet1 # Open the spreadhseet
sheet=cliente.open_by_key('1J4DAYirEo3fvxMva6iDXx9mpRH6e8HTBIX2CK3svJUQ').get_worksheet(0)
dados = sheet.get_all_records()  # Get a list of all records
df=pd.DataFrame(dados)

def conexao(aba="Ciente Encarregadas",
            chave='1J4DAYirEo3fvxMva6iDXx9mpRH6e8HTBIX2CK3svJUQ'):  # pasta="Transporte e Limpeza de Geladeira (respostas)",
    """
    carrega os dados da planilha do google sheets

    """
    sheet = cliente.open_by_key(chave).worksheet(aba)  # Open the spreadhseet
    dados = sheet.get_all_records()
    df = pd.DataFrame(dados)
    return sheet, dados, df
#print(df)
#nomesServ = ['Aquiles Rhuan Bandeira Neres Pinheiro','Higor Eurípedes Pimentel Fernandes de Araújo','Ismael de Souza Martins Junior','Marcelo Paulino Galhardo','Mônica Regina Vieira Santos','Paulo Cesar de Castro Filho','Samuel de Paula Faria']
#servid=easygui.choicebox("Servidor:","Escolha",nomesServ,0)

#texto=''
# for k in range(len(nomesServ)):
#     texto=texto+'\n'+str(k)+')'+nomesServ[k]
#     #print(texto)
# numero=input('Digite o número correspondente ao seu nome e pressione enter:'+ texto)
# servid=nomesServ[int(numero)]
# print('Nome selecionado:'+servid)
datando=[]
n_solicitacao=[]
nome=[]
telefone=[]
predio=[]
sala=[]
data=[]
observacao=[]
tipo=[]
links = []


#padroes
padrao = '<p style="font-family:Courier; color:Blue; font-size: 15px;">'
infor = '<p style="font-family:Courier; color:Green; font-size: 15px;">'
alerta = '<p style="font-family:Courier; color:Red; font-size: 15px;">'
titulo = '<p style="font-family:Courier; color:Blue; font-size: 20px;">'
subtitulo = '<p style="font-family:Courier; color:Blue; font-size: 17px;">'
cabecalho='<div id="logo" class="span8 small"><a title="Universidade Federal do Tocantins"><img src="https://ww2.uft.edu.br/images/template/brasao.png" alt="Universidade Federal do Tocantins"><span class="portal-title-1"></span><h1 class="portal-title corto">Universidade Federal do Tocantins</h1><span class="portal-description">COINFRA - LIMPEZA PREDIAL</span></a></div>'


todos_status = ['', 'Procedente',
'Pendente',
'Cancelada',
'Pendente Usuário',
'Não Procedente',
'Reclamação Respondida',
'Observação',
'Reclamação',
'Ignorar']

st.sidebar.title('Gestão Limpeza')
a=k
#pg=st.sidebar.selectbox('Selecione a Página',['Solicitações em Aberto','Solicitações a Finalizar','Consulta'])
pg=st.sidebar.radio('',['Solicitações em Aberto','Solicitações a Finalizar','Datas','Consulta','Relatório Fiscalização'])

if (pg=='Solicitações em Aberto'):

    st.markdown(cabecalho,unsafe_allow_html=True)
    st.subheader(pg)
    status_selecionar = st.selectbox('Filtrar por Status:', todos_status)
    sheet, dados, df = conexao()

    for dic in dados:
        if dic['Status'] == status_selecionar and dic['Ciente'] == 'FALSO' and dic['Não é Possível Atender']=='FALSO' and dic['Prédio']!='' and dic['Tipo'] not in ['Limpeza de Geladeira/Freezer/Bebedouro','Limpeza de Geladeira/Freezer']: #'Registro de Reclamação', and dic['Status'] not in ['Ignorar','Cancelada']
            print(dic['Nº da Solicitação'])
            n_solicitacao.append(dic['Nº da Solicitação'])
            tipo.append(dic['Tipo'])
            nome.append(dic['Nome do Solicitante'])
            telefone.append(dic['Telefone'])
            predio.append(dic['Prédio'])
            sala.append(dic['Sala/Local'])
            data.append(dic['Data da Limpeza'])
            observacao.append(dic['Observações'])
            links.append(dic['Foto / Vídeo (Opcional)'])

    selecionado = st.selectbox('Nº da solicitação:',n_solicitacao)
    #print(nome[n_solicitacao.index(selecionado)])
    if (len(n_solicitacao)>0):
        n=n_solicitacao.index(selecionado)
        itens = ''
        cont=1
        for link in links:
            if (link!=''):
                itens += '<p><a href='+link+'>Link '+str(cont)+' </a></p>'
                cont+=1
        #apresentar dados da solicitação

        st.markdown(titulo+'<b>Dados da Solicitação</b></p>',unsafe_allow_html=True)
        #st.text('<p style="font-family:Courier; color:Blue; font-size: 20px;">Nome: '+ nome[n]+'</p>',unsafe_allow_html=True)
        st.markdown(padrao + '<b>Tipo</b>: ' + str(tipo[n]) + '</p>', unsafe_allow_html=True)
        if tipo[n]=='Registro de Reclamação':
            st.markdown(alerta+'<b>Para reclamações, escrever retorno ao usuário na Observação</b></p>',unsafe_allow_html=True)
        st.markdown(padrao+'<b>Nome</b>: '+ str(nome[n])+'</p>',unsafe_allow_html=True)
        st.markdown(padrao+'<b>Telefone</b>: '+ str(telefone[n])+'</p>',unsafe_allow_html=True)
        st.markdown(padrao+'<b>Prédio</b>: '+ str(predio[n])+'</p>',unsafe_allow_html=True)
        st.markdown(padrao+'<b>Sala</b>: '+ str(sala[n])+'</p>',unsafe_allow_html=True)
        st.markdown(padrao+'<b>Data</b>: '+ str(data[n])+'</p>',unsafe_allow_html=True)
        st.markdown(padrao+'<b>Descrição</b>: '+ observacao[n]+'</p>',unsafe_allow_html=True)
        st.markdown(padrao + '<b>Foto/Vídeo</b>: ' + itens + '</p>', unsafe_allow_html=True)

        #status=st.selectbox('Selecione o Status',['Selecionar','Ciente','Não é possível atender'])
        #print(status)

        #Data
        d = '01/01/2023'
        # print('Data Agendamento registrada: ' + d_agend[n])
        if (data[n] != ''):
            d = data[n]
        else:
            # st.text('OS sem agendamento registrado ou com data de agendamento anterior a hoje!')
            print('Sem data registrada')
        d = d.replace('/', '-')

        data_ag = datetime.strptime(d, '%d-%m-%Y')

        if (data_ag == ''):
            data_ag = datetime.strptime("01-01-2023", '%d-%m-%Y')

        data_agendamento = st.date_input('Data de Limpeza (ANO/MÊS/DIA)', value=data_ag)
        #st.markdown('<p id="datepicker--screenreader--message--input" placeholder="DD/MM/YYYY"></p>',unsafe_allow_html=True)
        #data_agendamento.strftime('%d/%m/%Y')
        celula = sheet.find(n_solicitacao[n])
        status=st.radio('Selecione o status:',['-','Ciente','Não é possível atender'])
        texto = st.text_area('Observação: ')
        obr=True
        if tipo[n] == 'Registro de Reclamação' and texto=='':
            obr=False
        s=st.text_input("Senha:",value="", type="password")
        botao=st.button('Registrar')
        if (botao==True and s==a and obr):
            if (status=='Ciente'):
                st.markdown(infor+'<b>Registro efetuado!</b></p>',unsafe_allow_html=True)
                data = data_agendamento
                data_formatada = str(data.day) + '/' + str(data.month) + '/' + str(data.year)
                sheet.update_acell('F' + str(celula.row), data_formatada)
                sheet.update_acell('S'+str(celula.row),'VERDADEIRO')
                sheet.update_acell('R' + str(celula.row), texto)
            elif(status=='Não é possível atender'):
                st.markdown(infor+'<b>Registro efetuado!</b></p>',unsafe_allow_html=True)
                sheet.update_acell('R' + str(celula.row), texto)
                sheet.update_acell('T'+str(celula.row),'VERDADEIRO')
        elif (botao==True and s!=a):
            st.markdown(alerta + '<b>Senha incorreta!</b></p>', unsafe_allow_html=True)
        elif (botao==True and s==a and obr==False):
            st.markdown(alerta + '<b>Por se tratar de uma reclamação, escrever observação/feedback para o usuário!</b></p>', unsafe_allow_html=True)
    else:
        st.markdown(infor + '<b>Não há itens na condição '+ pg +'</b></p>', unsafe_allow_html=True)
elif pg=='Solicitações a Finalizar':

    sheet, dados, df = conexao()
    for dic in dados:
        #print(dic['Nº da Solicitação'] + ' - ' + dic['Status'] + ' - ' + dic['Atendida']) #
        if dic['Não é Possível Atender']=='FALSO' and dic['Atendida']=='FALSO' and dic['Prédio']!='' and dic['Tipo'] not in ['Limpeza de Geladeira/Freezer/Bebedouro','Limpeza de Geladeira/Freezer'] and dic['Status'] not in ['Ignorar','Cancelada']: #'Registro de Reclamação', dic['Ciente'] == 'VERDADEIRO' and
            print(dic['Nº da Solicitação'])
            n_solicitacao.append(dic['Nº da Solicitação'])
            tipo.append(dic['Tipo'])
            nome.append(dic['Nome do Solicitante'])
            telefone.append(dic['Telefone'])
            predio.append(dic['Prédio'])
            sala.append(dic['Sala/Local'])
            data.append(dic['Data da Limpeza'])
            observacao.append(dic['Observações'])
            links.append(dic['Foto / Vídeo (Opcional)'])

    st.markdown(cabecalho,unsafe_allow_html=True)
    st.subheader(pg)
    selecionado = st.selectbox('Nº da solicitação:',n_solicitacao)
    #print(nome[n_solicitacao.index(selecionado)])
    if (len(n_solicitacao) > 0):
        n = n_solicitacao.index(selecionado)
        itens = ''
        cont=1
        for link in links:
            itens += '<a href='+link+'>Link '+str(cont)+' </a>'
            cont+=1
        # apresentar dados da solicitação
        st.markdown(titulo + '<b>Dados da Solicitação</b></p>', unsafe_allow_html=True)
        # st.text('<p style="font-family:Courier; color:Blue; font-size: 20px;">Nome: '+ nome[n]+'</p>',unsafe_allow_html=True)
        st.markdown(padrao + '<b>Tipo</b>: ' + str(tipo[n]) + '</p>', unsafe_allow_html=True)
        st.markdown(padrao + '<b>Nome</b>: ' + str(nome[n]) + '</p>', unsafe_allow_html=True)
        st.markdown(padrao + '<b>Telefone</b>: ' + str(telefone[n]) + '</p>', unsafe_allow_html=True)
        st.markdown(padrao + '<b>Prédio</b>: ' + str(predio[n]) + '</p>', unsafe_allow_html=True)
        st.markdown(padrao + '<b>Sala</b>: ' + str(sala[n]) + '</p>', unsafe_allow_html=True)
        st.markdown(padrao + '<b>Data</b>: ' + str(data[n]) + '</p>', unsafe_allow_html=True)
        st.markdown(padrao + '<b>Descrição</b>: ' + observacao[n] + '</p>', unsafe_allow_html=True)
        st.markdown(padrao + '<b>Foto/Vídeo</b>: ' + itens + '</p>', unsafe_allow_html=True)

        # status=st.selectbox('Selecione o Status',['Selecionar','Ciente','Não é possível atender'])
        # print(status)
        celula = sheet.find(n_solicitacao[n])
        status = st.radio('Selecione o status:', ['-', 'Finalizar','Não Foi possível atender'])
        texto = st.text_area('Observação: ')
        s=st.text_input("Senha:",value="", type="password")
        botao=st.button('Registrar')
        if (botao==True and s==a):
            if (status == 'Finalizar'):
                st.markdown(infor + '<b>Registro efetuado!</b></p>', unsafe_allow_html=True)
                sheet.update_acell('U' + str(celula.row), 'VERDADEIRO')
                sheet.update_acell('R' + str(celula.row), texto)
            elif (status == 'Não Foi possível atender'):
                st.markdown(infor + '<b>Registro efetuado!</b></p>', unsafe_allow_html=True)
                sheet.update_acell('T' + str(celula.row), 'VERDADEIRO')
                sheet.update_acell('R' + str(celula.row),texto)
        elif (botao==True and s!=a):
            st.markdown(alerta + '<b>Senha incorreta!</b></p>', unsafe_allow_html=True)
    else:
        st.markdown(infor + '<b>Não há itens na condição ' + pg + '</b></p>', unsafe_allow_html=True)
elif pg=='Consulta':
    sheet, dados, df = conexao()
    for dic in dados:
        if dic['Prédio']!='':
            print(dic['Nº da Solicitação'])
            n_solicitacao.append(dic['Nº da Solicitação'])
            nome.append(dic['Nome do Solicitante'])
            telefone.append(dic['Telefone'])
            predio.append(dic['Prédio'])
            sala.append(dic['Sala/Local'])
            data.append(dic['Data da Limpeza'])
            observacao.append(dic['Observações'])


    st.markdown(cabecalho,unsafe_allow_html=True)
    st.subheader(pg)
    with st.form(key='form1'):
        filtro=st.selectbox('Selecione o Prédio:',predio)
        btn1=st.form_submit_button('Filtrar')

    if (btn1==True):
        dados=df[['Prédio', 'Sala/Local', 'Tipo', 'Data da Limpeza', 'Observações', 'Nome do Solicitante','Telefone', 'Nº da Solicitação', 'Ciente', 'Não é Possível Atender', 'Atendida']]
        filtrar=dados['Prédio'].isin([filtro])
        st.dataframe(dados[filtrar].head())
    else:
        st.dataframe(df[['Prédio', 'Sala/Local', 'Tipo', 'Data da Limpeza', 'Observações', 'Nome do Solicitante','Telefone', 'Nº da Solicitação', 'Ciente', 'Não é Possível Atender', 'Atendida']])
elif pg=='Datas':
    sheet, dados, df = conexao()
    for dic in dados:
        if dic['Ciente'] == 'VERDADEIRO' and dic['Não é Possível Atender'] == 'FALSO':
            print(dic['Nº da Solicitação'])
            n_solicitacao.append(dic['Nº da Solicitação'])
            tipo.append(dic['Tipo'])
            nome.append(dic['Nome do Solicitante'])
            telefone.append(dic['Telefone'])
            predio.append(dic['Prédio'])
            sala.append(dic['Sala/Local'])
            data.append(dic['Data da Limpeza'])
            observacao.append(dic['Observações'])

    st.markdown(cabecalho, unsafe_allow_html=True)
    st.subheader(pg)

elif pg=='Relatório Fiscalização':
    sheet, dados, df = conexao(aba=pg)

    st.markdown(cabecalho, unsafe_allow_html=True)
    st.subheader(pg)

    predio = []
    sala = []
    fl_critica = []
    fl_grave = []
    fl_outros = []
    op_critica = []
    op_grave = []
    op_outros = []
    fotos = []
    data = []
    status = []
    codigo = []
    observacao = []

    status_opcoes = ['', 'Ciente', 'Manutenção', 'Não pertence ao contrato']
    status_selecionado = st.selectbox('Status da observação:', status_opcoes)
    print(status_selecionado)
    #print(dados)
    def filtro(x):
        if x['status'] == status_selecionado:
            return True
        else:
            return False

    lista = dados
    resultado = filter(filtro, lista)

    #filtrar = dados['status'].isin([status_selecionado])
    dad = resultado #dados[filtrar]

    for dic in dad: #dados
        if dic['Carimbo de data/hora'] != '':
            predio.append(dic['Bloco'])
            sala.append(dic['Sala/Local'])
            fl_critica.append(dic['FALHAS DE NATUREZA CRÍTICA '])
            fl_grave.append(dic['FALHAS DE NATUREZA GRAVE'])
            fl_outros.append(dic['OUTRAS DESCONFORMIDADES'])
            op_critica.append(dic['FALHAS DE NATUREZA CRÍTICA_OP'])
            op_grave.append(dic['FALHAS DE NATUREZA GRAVE _OP'])
            op_outros.append(dic['OUTRAS DESCONFORMIDADES _OP'])
            fotos.append(dic['Fotos'])
            data.append(dic['Data'])
            observacao.append(dic['Observações'])
            status.append(dic['status'])
            codigo.append(dic['codigo'])

    st.markdown(alerta + '<b>'+str(len(predio))+' Registros Encontrados nesse Status</b></p>', unsafe_allow_html=True)
    selecionado = st.selectbox('Código de registro:', codigo)

    if len(predio)>0:
        n = codigo.index(selecionado)

        # apresentar dados da solicitação
        st.markdown(titulo + '<b>Dados do Registro de Fiscalização</b></p>', unsafe_allow_html=True)
        # st.text('<p style="font-family:Courier; color:Blue; font-size: 20px;">Nome: '+ nome[n]+'</p>',unsafe_allow_html=True)
        st.markdown(padrao + '<b>Data</b>: ' + str(data[n]) + '</p>', unsafe_allow_html=True)
        st.markdown(padrao + '<b>Prédio</b>: ' + str(predio[n]) + '</p>', unsafe_allow_html=True)
        st.markdown(padrao + '<b>Sala/Local</b>: ' + str(sala[n]) + '</p>', unsafe_allow_html=True)
        st.markdown(subtitulo + '<b>Limpeza</b></p>', unsafe_allow_html=True)
        if (fl_critica[n]!=''):
            st.markdown(padrao + '<b>Falhas de Natureza Crítica</b>: ' + str(fl_critica[n]) + '</p>', unsafe_allow_html=True)
        if (fl_grave[n] != ''):
            st.markdown(padrao + '<b>Falhas de Natureza Grave</b>: ' + str(fl_grave[n]) + '</p>', unsafe_allow_html=True)
        if (fl_outros[n] != ''):
            st.markdown(padrao + '<b>Outras Desconformidades</b>: ' + str(fl_outros[n]) + '</p>', unsafe_allow_html=True)
        st.markdown(subtitulo + '<b>Apoio Administrativo e Operacionais</b></p>', unsafe_allow_html=True)
        if (op_critica[n] != ''):
            st.markdown(padrao + '<b>Falhas de Natureza Crítica</b>: ' + str(op_critica[n]) + '</p>', unsafe_allow_html=True)
        if (op_grave[n] != ''):
            st.markdown(padrao + '<b>Falhas de Natureza Grave</b>: ' + str(op_grave[n]) + '</p>', unsafe_allow_html=True)
        if (op_outros[n] != ''):
            st.markdown(padrao + '<b>Outras Desconformidades</b>: ' + str(op_outros[n]) + '</p>', unsafe_allow_html=True)
        st.markdown(subtitulo + '<b>Fotos</b></p>', unsafe_allow_html=True)
        # fotos
        cont = 1
        dir = ''
        for link in fotos[n].split(', '):
           link1 = link.split('id=')
           id = link1[1]
           url ='https://drive.google.com/file/d/' + id + '/preview' #'https://drive.google.com/uc?export=view&id=' + id #
           print(url)
           dir+='<iframe src="'+url+'"></iframe><br>'

           #components.iframe(url)
           #st.image(url)
           #htm = '<img src="'+url+'" alt="Foto" width="100" height="100"><br>'
           #components.html(htm + '<br>Foto ' + str(cont))
           cont += 1
        st.write(dir, unsafe_allow_html=True)
        with st.form(key='my_form'):
            stat = st.selectbox('Status',status_opcoes,index=status_opcoes.index(status_selecionado))
            obs = st.text_area('Observação: ',value=observacao[n])
            s = st.text_input("Senha:", value="", type="password")
            botao = st.form_submit_button('Registrar')
            if (botao == True and s == a):
                celula = sheet.find(codigo[n])
                sheet.update_acell('L' + str(celula.row), obs)
                sheet.update_acell('M' + str(celula.row), stat)

                st.success('Registro efetuado!')
            elif (botao == True and s != a):
                st.error('Senha incorreta!')

    # selecionado = st.selectbox('Nº da solicitação:', n_solicitacao)
    # # print(nome[n_solicitacao.index(selecionado)])
    # if (len(n_solicitacao) > 0):
    #     n = n_solicitacao.index(selecionado)
    #
    #     # apresentar dados da solicitação
    #     st.markdown(titulo + '<b>Dados da Solicitação</b></p>', unsafe_allow_html=True)
    #     # st.text('<p style="font-family:Courier; color:Blue; font-size: 20px;">Nome: '+ nome[n]+'</p>',unsafe_allow_html=True)
    #
    #     st.markdown(padrao + '<b>Nome</b>: ' + str(nome[n]) + '</p>', unsafe_allow_html=True)
    #     st.markdown(padrao + '<b>Telefone</b>: ' + str(telefone[n]) + '</p>', unsafe_allow_html=True)
    #     st.markdown(padrao + '<b>Prédio</b>: ' + str(predio[n]) + '</p>', unsafe_allow_html=True)
    #     st.markdown(padrao + '<b>Sala</b>: ' + str(sala[n]) + '</p>', unsafe_allow_html=True)
    #     st.markdown(padrao + '<b>Data</b>: ' + str(data[n]) + '</p>', unsafe_allow_html=True)
    #     st.markdown(padrao + '<b>Descrição</b>: ' + observacao[n] + '</p>', unsafe_allow_html=True)
    #
    #     # status=st.selectbox('Selecione o Status',['Selecionar','Ciente','Não é possível atender'])
    #     # print(status)
    #     celula = sheet.find(n_solicitacao[n])
    #     status = st.radio('Selecione o status:', ['-', 'Finalizar', 'Não Foi possível atender'])
    #     texto = st.text_area('Observação: ')
    #     s = st.text_input("Senha:", value="", type="password")
    #     botao = st.button('Registrar')
    #     if (botao == True and s == a):
    #         if (status == 'Finalizar'):
    #             st.markdown(infor + '<b>Registro efetuado!</b></p>', unsafe_allow_html=True)
    #             sheet.update_acell('U' + str(celula.row), 'VERDADEIRO')
    #             sheet.update_acell('R' + str(celula.row), texto)
    #         elif (status == 'Não Foi possível atender'):
    #             st.markdown(infor + '<b>Registro efetuado!</b></p>', unsafe_allow_html=True)
    #             sheet.update_acell('T' + str(celula.row), 'VERDADEIRO')
    #             sheet.update_acell('R' + str(celula.row), texto)
    #     elif (botao == True and s != a):
    #         st.markdown(alerta + '<b>Senha incorreta!</b></p>', unsafe_allow_html=True)
    # else:
    #     st.markdown(infor + '<b>Não há itens na condição ' + pg + '</b></p>', unsafe_allow_html=True)
