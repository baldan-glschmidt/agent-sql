# E140VTR

## Descrição

Vendas - Nota Fiscal de Saída - Dados do Conhecimento de Transporte - Veículos Transportados

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
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
| SeqVtr | Number(004,0) | Não | Sequência de veículos transportados |
| CodCor | String(008) | Sim | Código da cor em cada montadora |
| DesCor | String(050) | Sim | Descrição da cor |
| ChaVei | String(050) | Sim | Chassi do veículo |
| CodMmo | String(012) | Sim | Código da Marca/Modelo conforme tabela RENAVAM |
| VlrVei | Number(015,2) | Sim | Valor unitário do veículo transportado |
| VlrFre | Number(015,2) | Sim | Valor unitário do frete |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqVtr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140VTR_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E140VTR_003

**Tabela:** E140CTE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

