# R600PSC

## Descrição

Pendências Smart Card

---

## Resumo

- Campos: 11
- Chave Primária: 0 campo(s)
- Índices: 4
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdtReg | String(014) | Sim | Identificador do Registro de Atualização |
| DatPen | Date | Sim | Data de Envio da Pendência |
| HorPen | Number(005,0) | Sim | Hora de Envio da Pendência |
| TipPsc | Number(001,0) | Sim | Tipo de Pendência |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| CodCon | Number(002,0) | Sim | Código do campo a ser atualizado |
| InfPen | String(056) | Sim | Informação a ser atualizada |
| DatExp | Date | Sim | Data de Expiração da Pendência |
| StaPen | Number(002,0) | Sim | Status da Pendências |

---

## Chave Primária

Não possui.

---

## Índices

### R600PSCIndice1

**Tipo:** Não unico

Campos:
- IdtReg

### R600PSCIndice2

**Tipo:** Não unico

Campos:
- NumCra

### R600PSCIndice3

**Tipo:** Não unico

Campos:
- DatPen
- HorPen

### R600PSCIndice4

**Tipo:** Não unico

Campos:
- CodPlt
- CodRlg

---

## Relacionamentos

### IR_R600PSC_004

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

