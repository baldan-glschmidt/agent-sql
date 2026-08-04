# E140UNT

## Descrição

Vendas - Nota Fiscal de Saída - Composição do Conhecimento de Transporte - Unidades de Transporte

---

## Resumo

- Campos: 9
- Chave Primária: 8 campo(s)
- Índices: 0
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
| SeqUnt | Number(004,0) | Não | Sequência da unidade de transporte |
| TipUnt | Number(001,0) | Não | Tipo da unidade de transporte |
| CodIdt | String(040) | Não | Código de identificação da unidade de transporte |
| VlrRat | Number(006,3) | Sim | Valor da quantidade rateada (Peso, Volume) |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqCct
- SeqUnt
- TipUnt
- CodIdt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140UNT_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

