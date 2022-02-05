#Emilly Maryelle Xavier Pereira N 519378

f = open('nota.txt', 'media.txt')
delimiter = ','
x = {}
nomes=[]
notas=[]

def media():
  somando_as_medias = lambda x:sum([float(z) for z in x.values() ])

  maior_media = lambda x:max([(float(z[1]),z[0]) for z in x.items() ])

  menor_media = lambda x:min([(float(z[1]),z[0]) for z in x.items() ])

  comparando_as_notas = lambda al, media:[(x[0],x[1]) for x in al.items() if float(x[1]) > media]
  
  alunos = dict(zip(nomes,notas))
  print(alunos)
  s = somando_as_medias(alunos)
  mediageral = s / len(alunos)
  mx = maior_media(alunos)
  mn = menor_media(alunos)
  acima = comparando_as_notas(alunos,mediageral)
  print('Média Turma: {0:.2f}'.format(mediageral))
  print('Maior Média: {0:.2f}  Aluno: {1}'.format(mx[0],mx[1]))
  print('Menor Média: {0:.2f}  Aluno: {1}'.format(mn[0],mn[1]))
  print('Alunos com as médias acima Media da Turma')
  print('   Aluno                Média')

  for linha in f:
    nomes.append((linha.replace("\n","")).split(delimiter)[0])
    notas.append((linha.replace("\n","")).split(delimiter)[1])
  for i in acima:
      print('  ',i[0], ' '*(20-len(i[0])), i[1])
print(media)