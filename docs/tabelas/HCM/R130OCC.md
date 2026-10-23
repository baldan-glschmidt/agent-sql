# R130OCC

## Descrição

Orçamento Local - Participantes do Curso

---

## Resumo

- Campos: 13
- Chave Primária: 10 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| AnoBas | Number(004,0) | Não | Ano Base do Orçamento |
| MesBas | Number(002,0) | Não | Mês Base do Orçamento |
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| SeqCus | Number(002,0) | Não | Sequência de Custos |
| EmpPar | Number(004,0) | Não | Código da empresa do participante |
| TipCol | Number(001,0) | Não | Tipo Colaborador do Curso |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| ObjCur | String(1000) | Sim | Objetivo do curso |
| ResCur | String(1000) | Sim | Resultado esperado com o curso |
| CodMcu | Number(003,0) | Sim | Tipo de Motivo |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- AnoBas
- MesBas
- CodCua
- SeqCus
- EmpPar
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R130OCC_006

**Tabela:** R130OCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| AnoBas | AnoBas |
| MesBas | MesBas |
| CodCua | CodCua |
| SeqCus | SeqCus |

### IR_R130OCC_009

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| EmpPar | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

