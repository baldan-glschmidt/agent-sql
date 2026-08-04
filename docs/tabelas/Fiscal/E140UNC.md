# E140UNC

## Descrição

Vendas - Nota Fiscal de Saída - Composição do Conhecimento de Transporte - Unidades de Carga

---

## Resumo

- Campos: 12
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqCct | Number(004,0) | Não | Sequência da composição da nota fiscal de saída no CT-e/MDF-e |
| SeqUnc | Number(004,0) | Não | Sequência da unidade de carga |
| TipUnc | Number(001,0) | Não | Tipo da unidade de carga |
| CodIdc | String(040) | Não | Código de identificação da unidade de carga |
| SeqUnt | Number(004,0) | Sim | Sequência da unidade de transporte |
| TipUnt | Number(001,0) | Sim | Tipo da unidade de transporte |
| CodIdt | String(040) | Sim | Código de identificação da unidade de transporte |
| VlrRat | Number(006,3) | Sim | Valor da quantidade rateada (Peso, Volume) |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqCct
- SeqUnc
- TipUnc
- CodIdc

---

## Índices

### E140UNCE140UNT

**Tipo:** Não unico

Campos:
- SeqUnt
- CodIdt
- TipUnt

---

## Relacionamentos

### IR_E140UNC_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

