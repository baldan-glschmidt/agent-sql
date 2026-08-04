# E140PSI

## Descrição

Vendas - Notas Fiscais de Saída - Controle de eventos de prorrogação de suspensão de ICMS

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeEve | String(100) | Sim | Identificação do evento |
| SeqNfi | Number(004,0) | Sim | Sequência do item na nota fiscal impressa |
| QtdPrg | Number(014,5) | Sim | Quantidade do item com prorrogação de prazo de suspensão de ICMS |
| SitEve | Number(002,0) | Não | Situação do evento |
| ObsRet | String(2000) | Sim | Observação referente ao retorno do evento de prorrogação de suspensão de ICMS |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdeUni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
