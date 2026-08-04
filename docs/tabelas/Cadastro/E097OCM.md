# E097OCM

## Descrição

Cadastro - Pendências de Montagem - Ocorrências

---

## Resumo

- Campos: 11
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
| SeqOcm | Number(006,0) | Não | Sequência de ocorrência na montagem |
| CodMot | Number(006,0) | Sim | Código do motivo da observação ou situação |
| ObsOcm | String(250) | Sim | Observação do movimento da montagem |
| DatGer | Date | Sim | Data da geração da ocorrência |
| HorGer | Number(005,0) | Sim | Hora da geração da ocorrência |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração da ocorrência |
| DatOce | Date | Sim | Data da ocorrência |

---

## Chave Primária

- CodEmp
- CodFil
- NumMon
- SeqMon
- SeqOcm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
