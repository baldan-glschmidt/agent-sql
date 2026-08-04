# E012LFE

## Descrição

Cadastros - Ligação Família X Estágios Produção

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
| CodFam | String(006) | Não | Código da Família do Produto |
| CodEtg | Number(004,0) | Não | Código do Estágio de Produção |
| SeqLfe | Number(004,0) | Não | Ordenação sequencial  dos estágios |

---

## Chave Primária

- CodEmp
- CodFam
- CodEtg

---

## Índices

### E012LFEIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodEtg

---

## Relacionamentos

### IR_E012LFE_001

**Tabela:** E012FAM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFam | CodFam |

### IR_E012LFE_002

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

