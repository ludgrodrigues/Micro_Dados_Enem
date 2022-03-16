#!/usr/bin/env python
# coding: utf-8

# # Microdados Enem

# In[86]:


import pandas as pd


# In[87]:


microdadosEnem = pd.read_csv("/home/luana/Dados/MICRODADOS_ENEM_2019.csv", sep = ";", encoding = 'ISO-8859-1', nrows=100000)


# In[88]:


microdadosEnem.head()


# In[89]:


microdadosEnem


# Descobrindo o nome das colunas

# In[90]:


microdadosEnem.columns.values


# Selecionando colunas que são interessantes para uma primeira análise:

# In[91]:


colunasSelecionadasEnem = ('NO_MUNICIPIO_RESIDENCIA', 'SG_UF_RESIDENCIA',
       'NU_IDADE', 'TP_SEXO', 'TP_ESTADO_CIVIL', 'TP_COR_RACA',
       'TP_NACIONALIDADE', 'NO_MUNICIPIO_NASCIMENTO', 'SG_UF_NASCIMENTO',
       'IN_BAIXA_VISAO', 'IN_CEGUEIRA', 'IN_SURDEZ',
       'IN_DEFICIENCIA_AUDITIVA', 'IN_SURDO_CEGUEIRA',
       'IN_DEFICIENCIA_FISICA', 'IN_DEFICIENCIA_MENTAL',
       'IN_DEFICIT_ATENCAO', 'IN_DISLEXIA', 'IN_DISCALCULIA',
       'IN_AUTISMO', 'IN_VISAO_MONOCULAR', 'IN_OUTRA_DEF', 'IN_GESTANTE',
       'IN_LACTANTE', 'IN_IDOSO', 'IN_ESTUDA_CLASSE_HOSPITALAR',
       'IN_SEM_RECURSO', 'IN_BRAILLE', 'IN_AMPLIADA_24', 'IN_AMPLIADA_18',
       'IN_LEDOR', 'IN_ACESSO', 'IN_TRANSCRICAO', 'IN_LIBRAS',
       'IN_TEMPO_ADICIONAL', 'IN_LEITURA_LABIAL', 'IN_MESA_CADEIRA_RODAS',
       'IN_MESA_CADEIRA_SEPARADA', 'IN_APOIO_PERNA', 'IN_GUIA_INTERPRETE',
       'IN_COMPUTADOR', 'IN_CADEIRA_ESPECIAL', 'IN_CADEIRA_CANHOTO',
       'IN_CADEIRA_ACOLCHOADA', 'IN_PROVA_DEITADO', 'IN_MOBILIARIO_OBESO',
       'IN_LAMINA_OVERLAY', 'IN_PROTETOR_AURICULAR', 'IN_MEDIDOR_GLICOSE',
       'IN_MAQUINA_BRAILE', 'IN_SOROBAN', 'IN_MARCA_PASSO', 'IN_SONDA',
       'IN_MEDICAMENTOS', 'IN_SALA_INDIVIDUAL', 'IN_SALA_ESPECIAL',
       'IN_SALA_ACOMPANHANTE', 'IN_MOBILIARIO_ESPECIFICO',
       'IN_MATERIAL_ESPECIFICO', 'IN_NOME_SOCIAL')


# In[92]:


microdadosEnemSelecionados = microdadosEnem.filter(items = colunasSelecionadasEnem)


# In[93]:


microdadosEnemSelecionados.head ()


# # Quantidade de candidados por município

# In[94]:


coluna_NO_MUNICIPIO_RESIDENCIA = microdadosEnemSelecionados['NO_MUNICIPIO_RESIDENCIA']


# In[95]:


coluna_NO_MUNICIPIO_RESIDENCIA.value_counts().sort_index()


# # Quantidade de candidados por idade

# In[96]:


coluna_NU_IDADE = microdadosEnemSelecionados['NU_IDADE']


# In[97]:


coluna_NU_IDADE.value_counts().sort_index()


#  Importando matplotlib para colocar um histograma de Idade para melhor visualização:

# In[98]:


import matplotlib


# In[99]:


coluna_NU_IDADE.hist(bins=30)


# # Quantos candidatos por estado?

# In[100]:


coluna_SG_UF_RESIDENCIA = microdadosEnemSelecionados['SG_UF_RESIDENCIA']


# In[101]:


coluna_SG_UF_RESIDENCIA.value_counts().sort_index()


# # Quantos homens e quantas mulheres?

# In[108]:


coluna_TP_SEXO = microdadosEnemSelecionados['TP_SEXO']


# In[109]:


coluna_TP_SEXO.value_counts().sort_index()


# In[110]:


DistribuicaoTPSexo = coluna_TP_SEXO.value_counts().sort_index()


# In[111]:


DistribuicaoTPSexo


# In[112]:


percentTPSexo = [100*x/DistribuicaoTPSexo.sum() for x in DistribuicaoTPSexo]


# In[113]:


percentTPSexo


# # Tem Gestante no Enem?

# Olhar geral, sem distinção de sexo

# In[102]:


coluna_IN_GESTANTE = microdadosEnemSelecionados['IN_GESTANTE']


# In[103]:


coluna_IN_GESTANTE.value_counts().sort_index()


# In[104]:


DistribuicaoInGestante = coluna_IN_GESTANTE.value_counts().sort_index()


# In[105]:


DistribuicaoInGestante


# In[106]:


percentInGestante = [100*x/DistribuicaoInGestante.sum() for x in DistribuicaoInGestante]


# In[107]:


percentInGestante


# Qual o percentual de gestante no Enem olhando apenas ṕara o sexo feminimo?

# In[114]:


sexoF = DistribuicaoTPSexo[0]


# In[115]:


NuGest = DistribuicaoInGestante [1]


# In[116]:


percentGestantes = 100*NuGest/sexoF


# In[117]:


percentGestantes


# In[118]:


percentNGestantes = 100 - percentGestantes


# In[189]:


percentNGestantes


# # Notas Homens e Mulheres na  (máximo, mínimo, média, mediana)

# In[190]:


colunasSelecionadas = ['TP_SEXO', 'NU_NOTA_REDACAO']


# In[121]:


micEnemSexRed = microdadosEnem.filter(items = colunasSelecionadas)


# In[122]:


micEnemSexRed.head()


# In[123]:


micEnemSexRed = micEnemSexRed.dropna()


# In[124]:


micEnemSexRed.head()


# In[125]:


micEnemSexRed.groupby('TP_SEXO').count()


# In[126]:


micEnemSexRed.groupby('TP_SEXO').max()


# In[127]:


micEnemSexRed.groupby('TP_SEXO').min()


# In[128]:


micEnemSexRed [micEnemSexRed. NU_NOTA_REDACAO>0].groupby('TP_SEXO').min()


# In[129]:


micEnemSexRed.groupby('TP_SEXO').mean()


# In[130]:


micEnemSexRed.groupby('TP_SEXO').median()


# In[131]:


micEnemSexRed.groupby('TP_SEXO').hist()


# In[132]:


micEnemSexRed.groupby('TP_SEXO').describe()


# # A Escolaridade dos pais afetam nas notas dos filhos?

# In[133]:


colSelecionadas=['NU_INSCRICAO','NU_NOTA_MT','NU_NOTA_REDACAO','Q001','Q002']


# In[134]:


micEnemSel = microdadosEnem.filter(items=colSelecionadas)


# In[135]:


micEnemSel.head()


# In[136]:


micEnemSel = micEnemSel.dropna()


# In[137]:


micEnemSel.head()


# Q001 - Até que série seu pai, ou o homem responsável por você, estudou?

# Q002 - Até que série sua mãe, ou a mulher responsável por você, estudou?

# # Passo 1 - Definindo um dicionário: 

# In[138]:


q001eq002Dicionario = {'A':'Nunca estudou',
                      'B':'Não completou a 4ª série/5º ano do Ensino Fundamental',
                      'C':'Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental',
                      'D':'Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio',
                      'E':'Completou o Ensino Médio, mas não completou a faculdade',
                      'F':'Completou a faculdade, mas não completou a Pós-graduação',
                      'G':'Completou a Pós-graduação',
                      'H':'Não sei'}


# # Passo 2 - Criar novas colunas no DataFrame

# Inserindo coluna NO_Q001:

# In[139]:


micEnemSel ['NO_Q001'] = [q001eq002Dicionario[resp] for resp in micEnemSel.Q001]


# In[140]:


micEnemSel.head()


# Inserindo coluna NO_Q002:

# In[141]:


micEnemSel ['NO_Q002'] = [q001eq002Dicionario[resp] for resp in micEnemSel.Q002]


# In[142]:


micEnemSel.head()


# # Passo 3 - Comparando a distribuição do nível de escolaridade PAI X Mãe no conjunto de dados

# 1 - distribuição dos candidatos do Enem por escolaridade do Pai:

# In[145]:


micEnemSel.filter(items=['NU_INSCRICAO', 'NO_Q001']).groupby('NO_Q001').count().sort_values(by='NU_INSCRICAO', ascending=False)


# 2 - distribuição dos candidatos do Enem por escolaridade da Mãe:

# In[146]:


micEnemSel.filter(items=['NU_INSCRICAO', 'NO_Q002']).groupby('NO_Q002').count().sort_values(by='NU_INSCRICAO', ascending=False)


# # Passo 4 - Olhando o desempenho em matemática segundo a escolariade dos Pais:

# 1 - Por Escolaridade do Pai:

# In[150]:


micEnemSel.filter(items=['NU_NOTA_MT', 'NO_Q001']).groupby('NO_Q001').mean().sort_values(by='NU_NOTA_MT', ascending=False)


# 2 - Por Escolaridade da Mãe:

# In[151]:


micEnemSel.filter(items=['NU_NOTA_MT', 'NO_Q002']).groupby('NO_Q002').mean().sort_values(by='NU_NOTA_MT', ascending=False)


# # Passo 5 Olhando o desempenho em redação segundo a escolariade dos Pais:

# 1 - Por Escolaridade do Pai:

# In[152]:


micEnemSel.filter(items=['NU_NOTA_REDACAO', 'NO_Q001']).groupby('NO_Q001').mean().sort_values(by='NU_NOTA_REDACAO', ascending=False)


# 2 - Por Escolaridade da Mãe:

# In[153]:


micEnemSel.filter(items=['NU_NOTA_REDACAO', 'NO_Q002']).groupby('NO_Q002').mean().sort_values(by='NU_NOTA_REDACAO', ascending=False)


# # O Quadro Socioeconmico por Estado afeta o desempenho dos alunos?

# 1 - Selecionando colunas de interresse:

# In[154]:


colSelectEstado = ['NU_INSCRCAO', 'SG_UF_RESIDENCIA', 'NU_NOTA_MT', 'NU_NOTA_REDACAO', 'Q001', 'Q002']


# In[156]:


micEnemSel['SG_UF_RESIDENCIA'] = microdadosEnem.SG_UF_RESIDENCIA


# In[157]:


micEnemSel.head()


# In[168]:


micEnemSel.filter(items=['NU_NOTA_REDACAO','NO_Q002']).groupby('NO_Q002').mean().sort_values(by='NU_NOTA_REDACAO', ascending=False)


# In[160]:


micEnemSel.filter(items=['NU_NOTA_REDACAO','NO_Q002']).where(microdadosEnem.SG_UF_RESIDENCIA == 'RJ').groupby('NO_Q002').mean().sort_values(by='NU_NOTA_REDACAO', ascending=False)


# In[167]:


micEnemSel.filter(items=['NU_NOTA_REDACAO','NO_Q002']).where(microdadosEnem.SG_UF_RESIDENCIA == 'SP').groupby('NO_Q002').mean().sort_values(by='NU_NOTA_REDACAO', ascending=False)


# In[169]:


micEnemSel.filter(items=['SG_UF_RESIDENCIA','NU_NOTA_REDACAO','NO_Q002']).groupby(['SG_UF_RESIDENCIA','NO_Q002']).mean()


# In[179]:


import matplotlib.pyplot as plt


# In[180]:


fig, ax = plt.subplots(figsize=(20,10))
plt.suptitle('Nota Redação x Escolaridade x Estado')

micEnemSel.filter(items=['SG_UF_RESIDENCIA','Q002','NU_NOTA_REDACAO']).groupby(['Q002', 'SG_UF_RESIDENCIA']).mean().sort_values(by='NU_NOTA_REDACAO', ascending=False).unstack().plot(ax=ax, )


# # Deixando o Gráfico melhor visualmente 

# In[188]:


# fig, ax = plt.subplots(figsize=(16,8))
# plt.suptitle('Nota Redação x Escolaridade x Estado')

ax = micEnemSel.filter(items=['SG_UF_RESIDENCIA','Q002','NU_NOTA_REDACAO']).groupby(['Q002', 'SG_UF_RESIDENCIA']).mean().sort_values(by='NU_NOTA_REDACAO', ascending=False).unstack().plot(figsize=(20,10), grid=True)

ax.set_title('Nota Redação x Escolaridade x Estado', fontsize=20)
# ax.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0.)

handles, labels = ax.get_legend_handles_labels()

import re
edited_labels = [re.search(',\s(.+?)\)', label).group(1) for label in labels]
ax.legend(edited_labels,bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0.)

textdictq002 = ""
for key,value in q001eq002Dicionario.items():
    textdictq002 = textdictq002 + "{k} : {v}\n".format(k=key,v=value)
    
ax.text(0.02,0.65, textdictq002, transform=ax.transAxes, fontsize=12,
       bbox={'boxstyle' : 'round', "facecolor":'darkturquoise', 'alpha':0.3})


# In[ ]:





# In[ ]:




