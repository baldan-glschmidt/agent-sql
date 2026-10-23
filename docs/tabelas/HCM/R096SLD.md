# R096SLD

## Descrição

EPI - Estoque

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodEpi | Number(008,0) | Não | Código do EPI |
| CodOem | Number(008,0) | Não | Código do Fornecedor |
| DatAlt | Date | Não | Data de Alteração do Saldo |
| SeqAlt | Number(003,0) | Não | Sequência da alteração do saldo |
| TipOpe | Number(001,0) | Sim | Tipo de Operação - Entrada/Saída |
| QtdEPI | Number(007,0) | Sim | Quantidade da Operação de Entrada/Saída Realizada |
| OriOpe | Number(001,0) | Sim | Origem da Operação de Entrada/Saída |
| CodJus | Number(003,0) | Sim | Código da justificativa |
| QtdSld | Number(009,0) | Sim | Saldo em Estoque |
| CodUsu | Number(010,0) | Sim | Código do Usuário para o Colaborador |

---

## Chave Primária

- NumEmp
- CodFil
- CodEpi
- CodOem
- DatAlt
- SeqAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R096SLD_002

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

