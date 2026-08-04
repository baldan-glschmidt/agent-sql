# E140CMP

## Descrição

Vendas - Nota Fiscal de Saída - Dados do Conhecimento de Transporte - Componentes do Valor da Prestação

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(005,0) | Não | Código da Filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqCmp | Number(004,0) | Não | Sequência de componentes |
| NomCmp | String(030) | Sim | Nome do componente que compõe o cálculo |
| VlrCmp | Number(015,2) | Sim | Valor do componente que compõe o cálculo |
| SeqMtr | Number(004,0) | Sim | Sequência (ordem) do modal |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqCmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140CMP_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E140CMP_003

**Tabela:** E140CTE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

