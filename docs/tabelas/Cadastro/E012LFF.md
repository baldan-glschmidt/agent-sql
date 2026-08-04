# E012LFF

## Descrição

Cadastros - Ligação Faixas da Grade X Famílias

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFam | String(006) | Não | Código da família de produtos |
| CodFxa | String(015) | Não | Código da Faixa da Grade |
| SitLff | String(001) | Não | Situação |

---

## Chave Primária

- CodEmp
- CodFam
- CodFxa

---

## Índices

### E012LFFIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFxa

---

## Relacionamentos

### IR_E012LFF_001

**Tabela:** E012FAM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFam | CodFam |

### IR_E012LFF_002

**Tabela:** E084FXA

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFxa | CodFxa |

