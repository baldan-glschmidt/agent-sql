# E055AGR

## Descrição

Cadastros - Tributos - Parâmetros de Impostos por Família

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| DatBas | Date | Não | Data base inicial de validade para apuração do valor base do imposto |
| CodFam | String(006) | Não | Código da família de produto |
| CodDrf | Number(006,0) | Sim | Código para documento de arrecadação |

---

## Chave Primária

- CodEmp
- CodFil
- CodImp
- DatBas
- CodFam

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E055AGR_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E055AGR_002

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

### IR_E055AGR_004

**Tabela:** E012FAM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFam | CodFam |

