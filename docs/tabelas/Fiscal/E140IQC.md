# E140IQC

## Descrição

Vendas - Informações de quantidades da carga

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqCct | Number(004,0) | Não | Seqüência da composição do conhecimento de transporte |
| SeqIqc | Number(004,0) | Não | Sequencia da informação das quantidades da carga |
| MedCte | String(002) | Sim | Unidade de medida da quantidade da carga do CTe |
| TipMed | String(020) | Sim | Tipo da unidade de medida da quantidade da carga do CTe |
| QtdMed | Number(013,4) | Sim | Quantidade da unidade de medida da informação da carga do CTe |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqCct
- SeqIqc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140IQC_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

### IR_E140IQC_004

**Tabela:** E140CCT

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |
| SeqCct | SeqCct |

