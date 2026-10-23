# R100PPO

## Descrição

Mandatos - Participantes da Posse

---

## Resumo

- Campos: 7
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
| FunCol | Number(001,0) | Sim | Função do Participante na Eleição |

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

### IR_R100PPO_002

**Tabela:** R100MAN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodMan | CodMan |

### IR_R100PPO_003

**Tabela:** R100ELE

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodMan | CodMan |
| SeqEle | SeqEle |

### IR_R100PPO_005

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

