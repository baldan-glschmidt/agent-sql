# R126CSE

## Descrição

Selecionados Triagem - Candidato

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Número do Candidato |
| MotEli | Number(002,0) | Não | Motivo da Eliminação |
| SitCan | Number(002,0) | Sim | Situação do Candidato |
| OriSel | Number(001,0) | Sim | Origem Seleção |
| CodJus | Number(003,0) | Sim | Código da justificativa para eliminação/desistência candidato |

---

## Chave Primária

- NumCan
- MotEli

---

## Índices

### R126CSEIndice2

**Tipo:** Não unico

Campos:
- MotEli

---

## Relacionamentos

### IR_R126CSE_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

