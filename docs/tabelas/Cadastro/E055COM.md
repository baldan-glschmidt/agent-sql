# E055COM

## Descrição

Tabelas - Impostos - Composição Imposto

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
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| DatBas | Date | Não | Data base inicial de validade para apuração do valor base do imposto |
| SeqCom | Number(003,0) | Não | Sequencial de parametrização do imposto |
| CodSql | Number(009,0) | Não | Código da forma de busca de dados |
| ParOpe | String(001) | Não | Tipo de imposto a considerar na base de cálculo do imposto |

---

## Chave Primária

- CodEmp
- CodFil
- CodImp
- DatBas
- SeqCom

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E055COM_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E055COM_002

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

