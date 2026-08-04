# E440RAC

## Descrição

Compras - Notas Fiscais de Entrada - Registro de Aquisição de Cana

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| CodSaf | String(010) | Não | Código da safra |
| DatCpt | Date | Sim | Mês e ano de competência |
| TotMes | Number(015,4) | Sim | Quantidade Total do Mês |
| TotAnt | Number(015,4) | Sim | Quantidade Total do Mês Anterior |
| TotGer | Number(015,4) | Sim | Quantidade Total Geral |
| VlrFor | Number(015,2) | Sim | Valor dos Fornecimentos |
| TotDed | Number(015,2) | Sim | Valor Total da Dedução |
| LiqFor | Number(015,2) | Sim | Valor Liquido dos Fornecimentos |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440RAC_002

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

### IR_E440RAC_004

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E440RAC_005

**Tabela:** E113SAF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodSaf | CodSaf |

