# E097VMO

## Descrição

Cadastro - Pendências de Montagem - Valores

---

## Resumo

- Campos: 12
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumMon | Number(008,0) | Não | Número do controle da montagem |
| SeqMon | Number(004,0) | Não | Sequência do documento de montagem |
| SeqVmo | Number(006,0) | Não | Sequência de movimento da diária |
| DebCre | String(001) | Sim | Indicativo do tipo do movimento (débito/crédito) |
| VlrAbe | Number(015,2) | Sim | Valor em aberto da montagem |
| ObsMon | String(250) | Sim | Observação do movimento da montagem |
| DatGer | Date | Sim | Data da geração da ocorrência |
| HorGer | Number(005,0) | Sim | Hora da geração da ocorrência |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração da ocorrência |
| DatLan | Date | Sim | Data do lançamento |

---

## Chave Primária

- CodEmp
- CodFil
- NumMon
- SeqMon
- SeqVmo

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
