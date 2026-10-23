# R100CEL

## Descrição

Mandatos - Convidados da Eleição

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodMan | Number(004,0) | Não | Código do Mandato |
| SeqEle | Number(002,0) | Não | Sequência da eleição |
| SeqCon | Number(004,0) | Não | Sequência que individualiza o participante |
| NomCon | String(040) | Sim | Nome do convidado |
| IdeCon | String(030) | Sim | Identificação do convidado |

---

## Chave Primária

- NumEmp
- CodFil
- CodMan
- SeqEle
- SeqCon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R100CEL_002

**Tabela:** R100MAN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodMan | CodMan |

### IR_R100CEL_003

**Tabela:** R100ELE

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodMan | CodMan |
| SeqEle | SeqEle |

