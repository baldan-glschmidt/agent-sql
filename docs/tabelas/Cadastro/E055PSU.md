# E055PSU

## Descrição

Cadastros - Tributos - Parâmetro de Configuração do Subsídio

---

## Resumo

- Campos: 16
- Chave Primária: 6 campo(s)
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
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| CodCli | Number(009,0) | Não | Código do cliente da nota fiscal de saída |
| SeqOrd | Number(004,0) | Não | Ordem preferencial do cálculo do subsídio |
| CtaDev | Number(007,0) | Sim | Conta contábil devedora |
| CtaCre | Number(007,0) | Sim | Conta contábil credora |
| PagFor | Number(009,0) | Sim | Fornecedor padrão para gerar título de imposto a pagar no financeiro |
| PagTti | String(003) | Sim | Tipo de título padrão para geração do título de imposto a pagar no financeiro |
| PagTri | String(005) | Sim | Transação padrão para geração do título de imposto a pagar no financeiro |
| AutFin | String(001) | Sim | Indicativo se gera título automaticamente no cálculo do imposto |
| AtuGri | String(001) | Sim | Atualiza guias de recolhimento de imposto |
| CodGri | Number(004,0) | Sim | Código da guia de recolhimento |
| CodFct | String(005) | Sim | Código da forma de contabilização |

---

## Chave Primária

- CodEmp
- CodFil
- CodImp
- DatBas
- CodFor
- CodCli

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E055PSU_002

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

