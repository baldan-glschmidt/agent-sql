# E140DLS

## Descrição

Vendas - Notas Fiscais de Saída - Entrada, Vencimento, Lote, Série

---

## Resumo

- Campos: 17
- Chave Primária: 6 campo(s)
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
| SeqIpv | Number(003,0) | Não | Sequência do item na nota fiscal de saída |
| SeqDls | Number(006,0) | Não | Sequência de movimento de item |
| CodDep | String(010) | Sim | Código do depósito |
| DatEnt | Date | Sim | Data da entrada do produto no depósito |
| DatVlt | Date | Sim | Data de validade do produto no depósito |
| CodLot | String(050) | Sim | Código do Lote de Fabricação para estocagem |
| NumSep | String(050) | Sim | Número de série do produto |
| QtdEst | Number(014,5) | Sim | Quantidade a ser movimentada do estoque |
| ObsDls | String(250) | Sim | Texto da observação |
| SerCcl | String(003) | Sim | Série do certificado de classificação |
| NumCcl | String(015) | Sim | Número do certificado de classificação |
| DatFab | Date | Sim | Data de fabricação do lote |
| IndEst | String(001) | Sim | Indicativo se o lote ou série movimentaram estoque |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIpv
- SeqDls

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140DLS_004

**Tabela:** E140IPV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |
| SeqIpv | SeqIpv |

