# E055PAE

## Descrição

Cadastros - Tributos - Parametros da Apuração de Encerramento

---

## Resumo

- Campos: 29
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodImp | String(003) | Não | Código do imposto |
| DatRef | Date | Não | Competência Início |
| DiaVct | Number(003,0) | Sim | Quantidade de dias após data apuração final para vencimento |
| AntPos | String(001) | Não | Indicativo do critério de definição de vencimento do imposto |
| IniCon | Number(001,0) | Sim | Critério de início de contagem dos dias de vencimento |
| CodDrf | Number(006,0) | Sim | Código para documento de arrecadação |
| VlrMin | Number(015,2) | Sim | Valor mínimo do imposto a ser gerado |
| TipAcu | String(001) | Sim | Indicativo se acumula ou não o imposto até atingir o valor mínimo |
| CtaDev | Number(007,0) | Sim | Conta contábil devedora |
| CtaCre | Number(007,0) | Sim | Conta contábil credora |
| PagFil | Number(005,0) | Sim | Filial padrão para gerar título de imposto a pagar no financeiro |
| PagFor | Number(009,0) | Sim | Fornecedor padrão para gerar título de imposto a pagar no financeiro |
| PagTti | String(003) | Sim | Tipo de título padrão para geração do título de imposto a pagar no financeiro |
| PagTri | String(005) | Sim | Transação padrão para geração do título de imposto a pagar no financeiro |
| AutFin | String(001) | Sim | Indicativo se gera título automaticamente no cálculo do imposto |
| AtuGri | String(001) | Sim | Atualiza guias de recolhimento de imposto |
| CodGri | Number(004,0) | Sim | Código da guia de recolhimento |
| CodFct | String(005) | Sim | Código da forma de contabilização |
| VlrMpa | Number(015,2) | Sim | Valor mínimo para parcelar o imposto |
| QtdPar | Number(003,0) | Sim | Quantidade de parcelas para parcelar o imposto |
| UltDba | Date | Sim | Última data base utilizada nos parâmetros de formação da base de cálculo |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- CodImp
- DatRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E055PAE_002

**Tabela:** E055PAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodImp | CodImp |

