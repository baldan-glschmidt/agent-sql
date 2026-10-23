# R124HRQ

## Descrição

Colaborador - Resposta Questionário

---

## Resumo

- Campos: 9
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador Candidato |
| NumCad | Number(009,0) | Não | Cadastro do Candidato |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodGrq | Number(003,0) | Não | Código do Grupo Questionário |
| DatGrq | Date | Não | Data da Resposta Questionário |
| CodItq | Number(003,0) | Não | Código do Item do Questionário |
| CodRsp | Number(003,0) | Sim | Código Resposta |
| AnoRsp | String(2000) | Sim | Anotações da Resposta |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- EstCar
- CodGrq
- DatGrq
- CodItq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124HRQ_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R124HRQ_006

**Tabela:** R118GRI

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodGrq | CodGrq |
| CodItq | CodItq |

### IR_R124HRQ_007

**Tabela:** R118ITR

| Origem | Destino |
|--------|---------|
| CodItq | CodItq |
| CodRsp | CodRsp |

