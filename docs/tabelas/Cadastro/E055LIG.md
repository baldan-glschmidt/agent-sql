# E055LIG

## Descrição

Tabelas - Impostos - Ligação entre Impostos

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| DatBas | Date | Não | Data base inicial de validade para apuração do valor base do imposto |
| SeqLig | Number(003,0) | Não | Sequencial de parametrização do imposto |
| ImpLig | String(003) | Não | Código do imposto de ligação |
| ParLig | String(001) | Não | Tipo de imposto a considerar na base de cálculo do imposto |

---

## Chave Primária

- CodEmp
- CodFil
- CodImp
- DatBas
- SeqLig

---

## Índices

### E055LIGIndice1

**Tipo:** Não unico

Campos:
- ImpLig

---

## Relacionamentos

### IR_E055LIG_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E055LIG_002

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

### IR_E055LIG_005

**Tabela:** E051IMP

| Origem | Destino |
|--------|---------|
| ImpLig | CodImp |

