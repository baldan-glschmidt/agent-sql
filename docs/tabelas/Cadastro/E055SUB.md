# E055SUB

## Descrição

Tabelas - Impostos - Parâmetro por Estado para Substituição Tributária

---

## Resumo

- Campos: 25
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| DatBas | Date | Não | Data base inicial de validade para apuração do valor base do imposto |
| SigUfs | String(002) | Não | Sigla do estado da apuração do ICMS substituição tributária |
| SeqOrd | Number(004,0) | Não | Ordem preferencial do cálculo por estado |
| DiaVct | Number(003,0) | Sim | Quantidade de dias após data apuração final para vencimento |
| IniCon | Number(001,0) | Sim | Critério de início de contagem dos dias de vencimento |
| AntPos | String(001) | Não | Indicativo do critério de definição de vencimento do imposto |
| CodDrf | Number(006,0) | Sim | Código para documento de arrecadação |
| VlrMin | Number(015,2) | Sim | Valor mínimo do imposto a ser gerado |
| TipAcu | String(001) | Sim | Indicativo se acumula ou não o imposto até atingir o valor mínimo |
| VlrAcu | Number(015,2) | Sim | Valor acumulado do imposto a ser comparado com valor mínimo |
| UltDba | Date | Sim | Última data base utilizada nos parâmetros de formação da base de cálculo |
| CtaDev | Number(007,0) | Sim | Conta contábil devedora |
| CtaCre | Number(007,0) | Sim | Conta contábil credora |
| PagFor | Number(009,0) | Sim | Fornecedor padrão para gerar título de imposto a pagar no financeiro |
| PagTti | String(003) | Sim | Tipo de título padrão para geração do título de imposto a pagar no financeiro |
| PagTri | String(005) | Sim | Transação padrão para geração do título de imposto a pagar no financeiro |
| AutFin | String(001) | Sim | Indicativo se gera título automaticamente no cálculo do imposto |
| AtuGri | String(001) | Sim | Atualiza guias de recolhimento de imposto |
| CodGri | Number(004,0) | Sim | Código da guia de recolhimento |
| CodFct | String(005) | Sim | Código da forma de contabilização |
| FatGer | Number(001,0) | Sim | Data do fato gerador para geração do título |
| IndIee | String(001) | Não | Indicativo se a empresa possui inscrição estadual para a unidade federativa |

---

## Chave Primária

- CodEmp
- CodFil
- CodImp
- DatBas
- SigUfs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E055SUB_002

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

