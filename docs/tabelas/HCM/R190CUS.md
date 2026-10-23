# R190CUS

## Descrição

CBHPM - Custos da CBHPM

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCBH | Number(008,0) | Não | Classificação Hierarquizada de Procedimentos Médicos |
| DatAlt | Date | Não | Data da Alteração das Informações da CBHPM |
| CodPor | String(003) | Sim | Código do Porte dos Procedimentos Médicos |
| PesPor | Number(005,2) | Sim | Peso do Porte |
| PorAne | Number(001,0) | Sim | Código do Porte Anestésico |
| NroInc | Number(003,0) | Sim | Incidência do Procedimento Médico |
| CusOpe | Number(010,4) | Sim | Custo Operacional |
| CusFil | Number(010,4) | Sim | Custo com Filmes |
| NroAux | Number(003,0) | Sim | Número de Auxiliares |

---

## Chave Primária

- CodCBH
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R190CUS_000

**Tabela:** R190CBH

| Origem | Destino |
|--------|---------|
| CodCBH | CodCBH |

