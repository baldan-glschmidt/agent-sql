# E440LNS

## Descrição

Compras - Ligação Entre Itens de Serviço de Notas Fiscais de Entrada

---

## Resumo

- Campos: 13
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
| SeqLns | Number(004,0) | Não | Sequência de ligação |
| EmpRlc | Number(004,0) | Não | Código da Empresa da Nota Fiscal Relacionada |
| FilRlc | Number(005,0) | Não | Código da filial da Nota Fiscal Relacionada |
| ForRlc | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada relacionada |
| NfcRlc | Number(009,0) | Não | Número da Nota Fiscal Relacionada |
| SnfRlc | String(003) | Não | Código da Série da Nota Fiscal Relacionada |
| IscRlc | Number(003,0) | Não | Sequência do Item de Serviço Relacionado |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqIsc
- SeqLns

---

## Índices

### E440LNSIndice1

**Tipo:** Não unico

Campos:
- EmpRlc
- FilRlc
- ForRlc
- NfcRlc
- SnfRlc
- IscRlc

---

## Relacionamentos

### IR_E440LNS_005

**Tabela:** E440ISC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |
| SeqIsc | SeqIsc |

### IR_E440LNS_012

**Tabela:** E440ISC

| Origem | Destino |
|--------|---------|
| EmpRlc | CodEmp |
| FilRlc | CodFil |
| ForRlc | CodFor |
| NfcRlc | NumNfc |
| SnfRlc | CodSnf |
| IscRlc | SeqIsc |

