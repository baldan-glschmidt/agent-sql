# E140REN

## Descrição

Vendas - Relacionamentos entre Notas Fiscais de Saída

---

## Resumo

- Campos: 12
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqRel | Number(004,0) | Não | Sequência de relacionamento |
| EmpRel | Number(004,0) | Não | Código da empresa da nota fiscal de saída relacionada |
| FilRel | Number(005,0) | Não | Código da filial da nota fiscal de saída relacionada |
| SnfRel | String(003) | Não | Código da série da nota fiscal de saída relacionada |
| NfvRel | Number(009,0) | Não | Número da nota fiscal de saída relacionada |
| TipRel | Number(001,0) | Sim | Indica o tipo do relacionamento das notas |
| MotSub | Number(002,0) | Sim | Motivo da substituição |
| DesMot | String(255) | Sim | Descrição do motivo da substituição |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqRel

---

## Índices

### E140RENIndice1

**Tipo:** Não unico

Campos:
- EmpRel
- FilRel
- SnfRel
- NfvRel

---

## Relacionamentos

### IR_E140REN_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

### IR_E140REN_008

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| EmpRel | CodEmp |
| FilRel | CodFil |
| SnfRel | CodSnf |
| NfvRel | NumNfv |

