# E000ETK

## Descrição

Tabelas - Eventos - Tracking

---

## Resumo

- Campos: 16
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqEtk | Number(009,0) | Não | Sequência do evento |
| TipEtk | Number(002,0) | Não | Tipo de evento |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| TipDoc | String(030) | Não | Tipo de documento |
| NumDoc | String(020) | Não | Número do documento |
| SerDoc | String(020) | Sim | Série do documento |
| DocExt | String(030) | Sim | Número do documento externo |
| CodPla | Number(006,0) | Sim | Código do plano |
| CodFas | Number(006,0) | Sim | Código da fase |
| MsgNot | String(1000) | Sim | Mensagem enviada na notificação |
| EncTrk | String(001) | Sim | Indicativo se encerra o tracking |
| SitEtk | String(001) | Sim | Situação do evento |
| QtdCns | Number(003,0) | Sim | Quantidade de vezes que o evento foi consumido |
| DatGer | Date | Não | Data da geração do registro |
| HorGer | Number(005,0) | Não | Hora da geração do registro |

---

## Chave Primária

- SeqEtk

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
