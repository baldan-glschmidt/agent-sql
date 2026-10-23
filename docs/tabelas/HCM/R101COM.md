# R101COM

## Descrição

Avaliação de Resultado - Comportamentos - Notas

---

## Resumo

- Campos: 11
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CodCic | Number(003,0) | Não | Código do ciclo de avaliação |
| TipAva | Number(002,0) | Não | Sequência do tipo de avaliação |
| SeqAva | Number(002,0) | Não | Sequência da avaliação |
| CodHpe | String(004) | Não | Código da Habilidade Pessoal |
| NotAva | Number(005,2) | Sim | Nota da avaliação da habilidade |
| MetAva | Number(005,2) | Sim | Meta para a próxima avaliação |
| ComChe | String(1500) | Sim | Comentário do avaliador que justifica a nota |
| ComEmp | String(1500) | Sim | Comentário do avaliado |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCic
- TipAva
- SeqAva
- CodHpe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R101COM_005

**Tabela:** R101AVA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodCic | CodCic |
| TipAva | TipAva |
| SeqAva | SeqAva |

### IR_R101COM_006

**Tabela:** R079HPE

| Origem | Destino |
|--------|---------|
| CodHpe | CodHpe |

