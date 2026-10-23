# R301EVE

## Descrição

Tabela auxiliar para listar registros da seção K300 do MANAD

---

## Resumo

- Campos: 16
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PidGer | String(021) | Não | ID da geração |
| SeqReg | Number(015,0) | Não | Sequência do registro |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do colaborador |
| NumCgc | Number(015,0) | Sim | Número da Inscrição |
| TipFol | Number(001,0) | Sim | Tipo da Folha |
| CodLoc | String(150) | Sim | Código do Local do Organograma |
| DatCmp | Date | Sim | Competência |
| CodEve | Number(004,0) | Sim | Código do Evento |
| ValEve | Number(011,2) | Sim | Valor do Evento |
| TipEve | String(001) | Sim | Tipo do Evento |
| IndIrf | Number(001,0) | Sim | Incidência Base IRRF |
| IndIns | Number(001,0) | Sim | Incidência Base INSS |
| TipCal | Number(002,0) | Sim | Tipo do Cálculo |
| DatReg | Date | Sim | Data da geração |
| CfjIns | String(014) | Sim | Número da Inscrição |

---

## Chave Primária

- PidGer
- SeqReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
