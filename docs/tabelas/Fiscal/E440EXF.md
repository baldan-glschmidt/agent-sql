# E440EXF

## Descrição

Compras - Notas Fiscais de Entrada - Ligação Notas de Frete

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqExf | Number(004,0) | Não | Sequência de composição de notas fiscais de entrada |
| FilRlc | Number(005,0) | Sim | Código da filial da nota fiscal relacionada (entrada ou saída) |
| ForRlc | Number(009,0) | Sim | Código do fornecedor da nota fiscal de entrada relacionada |
| NumRlc | Number(009,0) | Sim | Número da nota fiscal relacionada (entrada ou saída) |
| SnfRlc | String(003) | Sim | Série da nota fiscal relacionada (entrada ou saída) |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqExf

---

## Índices

### E440EXFIndice2

**Tipo:** Não unico

Campos:
- SnfRlc
- NumRlc
- CodEmp
- FilRlc

### E440EXFIndice3

**Tipo:** Não unico

Campos:
- NumRlc
- ForRlc
- CodEmp
- FilRlc

---

## Relacionamentos

### IR_E440EXF_004

**Tabela:** E440NFC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |

