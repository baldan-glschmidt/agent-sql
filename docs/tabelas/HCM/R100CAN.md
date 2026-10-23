# R100CAN

## Descrição

Candidatos Cipa

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodMan | Number(004,0) | Não | Código do Mandato |
| SeqEle | Number(002,0) | Não | Sequência da eleição |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| DatCan | Date | Sim | Data Candidatura |
| CurCip | String(001) | Sim | Curso Cipa (S,N) |
| VotObt | Number(004,0) | Sim | Votos Obtidos |
| DatExc | Date | Sim | Data de Término da Candidatura |
| MotExc | Number(001,0) | Sim | Motivo da Exclusão |
| CipSca | Number(001,0) | Sim | Situação do Candidato |

---

## Chave Primária

- NumEmp
- CodFil
- CodMan
- SeqEle
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R100CAN_002

**Tabela:** R100MAN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodMan | CodMan |

### IR_R100CAN_003

**Tabela:** R100ELE

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodMan | CodMan |
| SeqEle | SeqEle |

### IR_R100CAN_005

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

