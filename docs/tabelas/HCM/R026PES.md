# R026PES

## Descrição

Percentuais de Seguridade

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSeg | Number(004,0) | Não | Código de Seguridade |
| DatIni | Date | Não | Competência de início do novo percentual |
| PerSeg | Number(007,4) | Sim | Percentual de Seguridade |

---

## Chave Primária

- CodSeg
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R026PES_000

**Tabela:** R026SEG

| Origem | Destino |
|--------|---------|
| CodSeg | CodSeg |

