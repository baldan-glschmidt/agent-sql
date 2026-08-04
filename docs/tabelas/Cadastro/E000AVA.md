# E000AVA

## Descrição

Cadastros - Definição de avalistas para os documentos de contrato, pedido e nota fiscal

---

## Resumo

- Campos: 31
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| SeqAva | Number(008,0) | Não | Sequência Avalista |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuApr | Number(010,0) | Sim | Usuário responsável pela aprovação do avalista |
| DatApr | Date | Sim | Data de aprovação do avalista |
| HorApr | Number(005,0) | Sim | Hora de aprovação do avalista |
| EmpCtr | Number(004,0) | Sim | Código da empresa do contrato de venda |
| FilCtr | Number(005,0) | Sim | Código da filial do contrato de venda |
| NumCtr | Number(006,0) | Sim | Número do Contrato |
| EmpPed | Number(004,0) | Sim | Código da empresa do pedido |
| FilPed | Number(005,0) | Sim | Código da filial do pedido |
| NumPed | Number(008,0) | Sim | Número do pedido |
| EmpNfv | Number(004,0) | Sim | Código da empresa da nota fiscal de saída |
| FilNfv | Number(005,0) | Sim | Código da filial da nota fiscal de saída |
| CodSnf | String(003) | Sim | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Sim | Número da nota fiscal de saída |
| CodAva | Number(008,0) | Não | Código do avalista C-cliente/R-representante |
| TipAva | String(001) | Não | Determina qual o tipo do avalista pode ser C-cliente/R-representante |
| Origem | String(003) | Não | Determina onde foram definidos os avalistas contrato, pedido ou na nota fiscal |
| SitAva | String(003) | Sim | Determina a situação da avaliação do avalista |
| ObsAva | String(999) | Sim | Texto da observação da avaliação do avalista |
| PerAva | Number(005,2) | Sim | Percentual no qual o avalista é responsável |
| VlrAva | Number(015,2) | Sim | Valor avalizado |
| VlrOri | Number(015,2) | Sim | Valor original avalizado do item |
| SeqOri | Number(004,0) | Sim | Sequência original do item avalizado |

---

## Chave Primária

- CodEmp
- CodFil
- SeqAva

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
