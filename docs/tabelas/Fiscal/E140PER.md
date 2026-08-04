# E140PER

## Descrição

Vendas - Nota Fiscal de Saída - Dados do Conhecimento de Transporte OS - Informações do percurso do CT-e

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| UfsPer | String(002) | Não | Sigla do estado |
| SeqPer | Number(004,0) | Sim | Sequência do percurso do CT-e |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- UfsPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140PER_003

**Tabela:** E140CTE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

