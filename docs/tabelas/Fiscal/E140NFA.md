# E140NFA

## Descrição

Vendas - Registros de Faturamento Total Anual

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| AnoEmi | Number(004,0) | Sim | Ano Emissão das notas fiscais |
| DatEmi | Date | Sim | Data final do ano de emissão das notas fiscais |
| TotFat | Number(015,2) | Sim | Valor total do faturamento no ano |
| TotDev | Number(015,2) | Sim | Valor total da devoluções no ano |
| DatGer | Date | Sim | Data da geração da consulta do faturamento |
| HorGer | Number(005,0) | Sim | Hora da geração da consulta do faturamento |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração da consulta do faturamento |

---

## Chave Primária

- IdeUni

---

## Índices

### E140NFAIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- DatEmi

### E140NFAIndice2

**Tipo:** Não unico

Campos:
- IdeUni
- CodEmp

### E140NFAIndice3

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- AnoEmi

---

## Relacionamentos

Nenhum relacionamento cadastrado.
