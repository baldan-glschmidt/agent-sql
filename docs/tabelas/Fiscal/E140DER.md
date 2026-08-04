# E140DER

## Descrição

Vendas - Notas Fiscais de Saída - Deduções e Reduções IBS/CBS

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Série da nota fiscal |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqDer | Number(003,0) | Não | Sequência da dedução/redução |
| TipDer | Number(002,0) | Não | Tipo da dedução/redução |
| DesDer | String(150) | Sim | Descrição da dedução/redução |
| VlrDer | Number(015,2) | Não | Valor da dedução/redução |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqDer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140DER_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

