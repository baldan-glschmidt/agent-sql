# R100MEB

## Descrição

Membros da Cipa

---

## Resumo

- Campos: 14
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
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| FunMeb | Number(001,0) | Sim | Função do Membro |
| FunCom | Number(001,0) | Sim | Função Complementar do Membro |
| OriMeb | String(001) | Sim | Origem do Membro |
| DatEnt | Date | Sim | Data de Entrada |
| DatSai | Date | Sim | Data de Saída |
| MotSai | Number(001,0) | Sim | Motivo de Saída |
| TipSpl | Number(001,0) | Sim | Tipo Colaborador Suplente |
| CadSpl | Number(009,0) | Sim | Cadastro Colaborador Suplente |

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

### IR_R100MEB_002

**Tabela:** R100MAN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodMan | CodMan |

### IR_R100MEB_003

**Tabela:** R100ELE

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodMan | CodMan |
| SeqEle | SeqEle |

### IR_R100MEB_005

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

