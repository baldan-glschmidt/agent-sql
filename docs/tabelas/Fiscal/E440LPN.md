# E440LPN

## Descrição

Compras - Ligação Entre Itens de Produto de Notas Fiscais de Entrada e Saída

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
| SeqIpc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| SeqLpn | Number(004,0) | Não | Sequência de ligação |
| EmpRlc | Number(004,0) | Não | Empresa da nota fiscal relacionada |
| FilRlc | Number(005,0) | Não | Filial da nota fiscal relacionada |
| NfvRlc | Number(009,0) | Não | Número da nota fiscal de saída relacionada |
| SnfRlc | String(003) | Não | Código da série da nota fiscal de saída relacionada |
| IpvRlc | Number(003,0) | Não | Sequência do item de produto relacionado |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqIpc
- SeqLpn

---

## Índices

### E440LPNIndice1

**Tipo:** Não unico

Campos:
- EmpRlc
- FilRlc
- SnfRlc
- NfvRlc
- IpvRlc

---

## Relacionamentos

### IR_E440LPN_005

**Tabela:** E440IPC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |
| SeqIpc | SeqIpc |

### IR_E440LPN_011

**Tabela:** E140IPV

| Origem | Destino |
|--------|---------|
| EmpRlc | CodEmp |
| FilRlc | CodFil |
| SnfRlc | CodSnf |
| NfvRlc | NumNfv |
| IpvRlc | SeqIpv |

