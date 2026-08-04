# E000MCX

## Descrição

Tabelas - Integrações - Movimentos do Caixa

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodEqu | Number(003,0) | Não | Código do equipamento fiscal |
| DatMov | Date | Não | Data do movimento da conta |
| SeqMov | Number(006,0) | Não | Sequência na data do movimento da conta |
| TipMov | Number(001,0) | Não | Tipo de Movimento do Caixa |
| DatGer | Date | Sim | Data da geração do movimento |
| HorGer | Number(005,0) | Sim | Hora da geração do movimento |
| IdeUni | String(050) | Sim | Identificador único alfanumérico |

---

## Chave Primária

- CodEmp
- CodFil
- CodEqu
- DatMov
- SeqMov

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E000MCX_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E000MCX_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E000MCX_002

**Tabela:** E050EQF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodEqu | CodEqu |

