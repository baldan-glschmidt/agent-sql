# E440UNT

## Descrição

Compras - Notas Fiscais de Entrada - Itens de Manifesto Unidades de Transporte

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| SeqImd | Number(003,0) | Não | Sequência do item no manifesto |
| SeqUnt | Number(004,0) | Não | Sequência da unidade de transporte |
| TipUnt | Number(001,0) | Não | Tipo da unidade de transporte |
| CodIdt | String(040) | Não | Código de identificação da unidade de transporte |
| VlrRat | Number(006,3) | Sim | Valor da quantidade rateada (Peso, Volume) |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfc
- SeqImd
- SeqUnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440UNT_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

