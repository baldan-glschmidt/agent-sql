# R017NEC

## Descrição

Postos de Trabalho - Características - Deficiências

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Código do Posto de Trabalho |
| DatIni | Date | Não | Define o início da validade das Características do posto |
| CodDef | Number(002,0) | Não | Indica a deficiência permitida para atuar no posto de trabalho |

---

## Chave Primária

- EstPos
- PosTra
- DatIni
- CodDef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017NEC_002

**Tabela:** R017CAR

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |
| DatIni | DatIni |

### IR_R017NEC_003

**Tabela:** R022DEF

| Origem | Destino |
|--------|---------|
| CodDef | CodDef |

