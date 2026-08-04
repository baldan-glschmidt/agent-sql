# E140LAC

## Descrição

Vendas - Nota Fiscal de Saída - Lacres

---

## Resumo

- Campos: 13
- Chave Primária: 11 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(005,0) | Não | Código da Filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqLac | Number(004,0) | Não | Sequência do lacre |
| SeqUnt | Number(004,0) | Não | Sequência da unidade de transporte |
| TipUnt | Number(001,0) | Não | Tipo da unidade de transporte |
| CodIdt | String(040) | Não | Código de identificação da unidade de transporte |
| SeqUnc | Number(004,0) | Não | Sequência da unidade de carga |
| TipUnc | Number(001,0) | Não | Tipo da unidade de carga |
| CodIdc | String(040) | Não | Código de identificação da unidade de carga |
| SeqCct | Number(004,0) | Sim | Sequência da composição da nota fiscal de saída no CT-e/MDF-e |
| CodLac | String(040) | Não | Código do Lacre |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqLac
- SeqUnt
- TipUnt
- CodIdt
- SeqUnc
- TipUnc
- CodIdc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140LAC_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

