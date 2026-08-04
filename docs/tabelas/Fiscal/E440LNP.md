# E440LNP

## Descrição

Compras - Ligação Entre Itens de Produto de Notas Fiscais de Entrada

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
| SeqIpc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| SeqLnp | Number(004,0) | Não | Sequência de ligação |
| EmpRlc | Number(004,0) | Não | Empresa da Nota Fiscal Relacionada |
| FilRlc | Number(005,0) | Não | Filial da Nota Fiscal Relacionada |
| ForRlc | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada Relacionada |
| NfcRlc | Number(009,0) | Não | Número da nota fiscal de entrada relacionada |
| SnfRlc | String(003) | Não | Código da série da nota fiscal de entrada relacionada |
| IpcRlc | Number(003,0) | Não | Sequência do item de produto relacionado |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqIpc
- SeqLnp

---

## Índices

### E440LNPIndice1

**Tipo:** Não unico

Campos:
- EmpRlc
- FilRlc
- ForRlc
- NfcRlc
- SnfRlc

---

## Relacionamentos

### IR_E440LNP_005

**Tabela:** E440IPC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |
| SeqIpc | SeqIpc |

### IR_E440LNP_011

**Tabela:** E440NFC

| Origem | Destino |
|--------|---------|
| EmpRlc | CodEmp |
| FilRlc | CodFil |
| ForRlc | CodFor |
| NfcRlc | NumNfc |
| SnfRlc | CodSnf |

