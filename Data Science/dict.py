dicionario = {'pessoa_1':{'nome':'Peterson','sobrenome':'Almeida'},'pessoa_2':{'nome':'Maria','sobrenome':'Silva'},'pessoa_3':{'nome':'Jose','sobrenome':'Santos'}}
print(["'"+x['nome']+x['sobrenome']+"'" for i,x in dicionario.items()])

s = []
for i,x in dicionario.items():
    s.append(x['nome']+x['sobrenome'])
print(s)


print(', '.join(list(map(lambda x: x[1]['nome']+x[1]['sobrenome'], dicionario.items()))))
