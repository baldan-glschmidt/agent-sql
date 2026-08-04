# E140PAS

## Descrição

Vendas - Nota Fiscal de Saída - Dados do Conhecimento de Transporte - Previsão do Fluxo da Carga - Passagens

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da Filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqPas | Number(004,0) | Não | Sequência das passagens do fluxo |
| CodPas | String(030) | Sim | Código da passagem do fluxo |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqPas

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140PAS_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E140PAS_003

**Tabela:** E140CTE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

