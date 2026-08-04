# E012FME

## Descrição

Cadastros - Ligação Família X Máscara Endereçamento Produto

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
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFam | String(006) | Não | Código da família do produto |
| CodMep | String(008) | Não | Código da máscara endereçamento produto |
| SeqFme | Number(004,0) | Não | Ordenação sequencial das máscaras |

---

## Chave Primária

- CodEmp
- CodFam
- CodMep

---

## Índices

### E012FMEIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodMep

---

## Relacionamentos

### IR_E012FME_001

**Tabela:** E012FAM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFam | CodFam |

### IR_E012FME_002

**Tabela:** E084MEP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMep | CodMep |

