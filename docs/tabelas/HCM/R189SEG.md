# R189SEG

## Descrição

PLR - Segmentos

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| DatIni | Date | Não | Data Início da Validade do Segmento |
| DatFim | Date | Sim | Data Final da Validade do Segmento |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R189SEG_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R189SEG_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

