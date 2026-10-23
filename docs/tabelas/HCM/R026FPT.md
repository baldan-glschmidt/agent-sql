# R026FPT

## Descrição

Códigos do FPAS - Valores dos Terceiros

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodFpa | Number(003,0) | Não | Código do FPAS |
| TipGrp | Number(001,0) | Não | Tipo da GPS |
| DatFpa | Date | Não | Data de Início da Vigência |
| TerFpa | Number(004,0) | Não | Código do Terceiro do FPAS |
| PerFpa | Number(007,4) | Sim | Percentual de Contribuição para o Terceiro |

---

## Chave Primária

- CodFpa
- TipGrp
- DatFpa
- TerFpa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R026FPT_002

**Tabela:** R026FPV

| Origem | Destino |
|--------|---------|
| CodFpa | CodFpa |
| TipGrp | TipGrp |
| DatFpa | DatFpa |

