# E440LSN

## Descrição

Compras - Ligação Entre Itens de Serviço de Notas Fiscais de Entrada e Saída

---

## Resumo

- Campos: 12
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqIsc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| SeqLsn | Number(004,0) | Não | Sequência de ligação |
| EmpRlc | Number(004,0) | Não | Código da empresa da nota fiscal relacionada |
| FilRlc | Number(005,0) | Não | Código da filial da nota fiscal relacionada |
| NfvRlc | Number(009,0) | Não | Número da nota fiscal de saída relacionada |
| SnfRlc | String(003) | Não | Código da série da nota fiscal de saída relacionada |
| IsvRlc | Number(003,0) | Não | Sequência do item de serviço relacionado |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqIsc
- SeqLsn

---

## Índices

### E440LSNIndice1

**Tipo:** Não unico

Campos:
- EmpRlc
- FilRlc
- SnfRlc
- NfvRlc
- IsvRlc

---

## Relacionamentos

### IR_E440LSN_005

**Tabela:** E440ISC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |
| SeqIsc | SeqIsc |

### IR_E440LSN_011

**Tabela:** E140ISV

| Origem | Destino |
|--------|---------|
| EmpRlc | CodEmp |
| FilRlc | CodFil |
| SnfRlc | CodSnf |
| NfvRlc | NumNfv |
| IsvRlc | SeqIsv |

