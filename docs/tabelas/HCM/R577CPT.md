# R577CPT

## Descrição

Competência - Cadastro

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCpt | Number(009,0) | Não | Código da Competência |
| IdeCpt | String(031) | Sim | Identificador da competência |
| DesCpt | String(200) | Sim | Descrição reduzida da competência |
| CodTpC | Number(004,0) | Sim | Permite classificar as competências através de um Tipo |
| DatCri | Date | Sim | Informe a data de criação da Competência |
| DatExt | Date | Sim | Informe a data de extinção da Competência |
| ObsCpt | String(7000) | Sim | Permite informar observações da Competência |

---

## Chave Primária

- CodCpt

---

## Índices

### R577CPTIndice1

**Tipo:** Unico

Campos:
- IdeCpt

---

## Relacionamentos

### IR_R577CPT_003

**Tabela:** R577TPC

| Origem | Destino |
|--------|---------|
| CodTpC | CodTpC |

