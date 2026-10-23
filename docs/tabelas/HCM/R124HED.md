# R124HED

## Descrição

Colaborador - Emprego Anterior - Disciplinas

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| SeqAdm | Number(002,0) | Não | Sequência da Admissão na Data |
| SeqDis | Number(002,0) | Não | Sequência da Disciplina |
| DinDis | Date | Sim | Data de Início da Disciplina |
| DfiDis | Date | Sim | Data de Término Disciplina |
| CodAcn | Number(008,0) | Sim | Área de Conhecimento |
| NomDis | String(060) | Sim | Nome da Disciplina |
| ObsDis | String(250) | Sim | Observação |
| TipDis | Number(001,0) | Sim | Tipo Disciplina |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- SeqAdm
- SeqDis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124HED_003

**Tabela:** R124HEA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| SeqAdm | SeqAdm |

### IR_R124HED_007

**Tabela:** R171ACN

| Origem | Destino |
|--------|---------|
| CodAcn | CodAcn |

