# R189ISE

## Descrição

PLR - Itens de Segmentos

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
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
| LocSeg | Number(009,0) | Não | Código do Local Pertencente ao Segmento |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- DatIni
- LocSeg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R189ISE_003

**Tabela:** R189SEG

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| DatIni | DatIni |

### IR_R189ISE_004

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| LocSeg | NumLoc |

