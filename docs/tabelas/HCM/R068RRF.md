# R068RRF

## Descrição

Coletores do Refeitório

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRft | Number(004,0) | Não | Código do Refeitório |
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor do Refeitório |

---

## Chave Primária

- CodRft
- CodPlt
- CodRlg

---

## Índices

### R068RRFIndice2

**Tipo:** Não unico

Campos:
- CodPlt
- CodRlg

---

## Relacionamentos

### IR_R068RRF_000

**Tabela:** R068RFT

| Origem | Destino |
|--------|---------|
| CodRft | CodRft |

### IR_R068RRF_001

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R068RRF_002

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

