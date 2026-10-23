# R046CEP

## Descrição

Controle de Eventos Periódicos eSocial

---

## Resumo

- Campos: 18
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| CmpFol | Date | Não | Competência |
| TipFol | Number(001,0) | Não | Tipo Folha |
| SeqFol | Number(009,0) | Não | Sequência de abertura da declaração mensal |
| StaFol | Number(001,0) | Sim | Status |
| EvtRem | String(001) | Sim | Possui informações de folha de pagamentos no período de apuração? |
| EvtPgt | String(001) | Sim | Possui pagamentos de rendimentos do trabalho no período de apuração? |
| EvtAPr | String(001) | Sim | Possui informações sobre a aquisição de produto rural pessoa físicas? |
| EvtCPr | String(001) | Sim | Possui informações de comercialização de produção? |
| EvtPor | String(001) | Sim | Contratou por intermédio de sindicato, serviços de trab. avulsos não portuário? |
| EvtCom | String(001) | Sim | Possui inf. de Desoneração de Folha ou Atividades concomitantes? |
| IndExc | String(001) | Sim | Indicativo exclusão de apuração das aquisições de produção rural S-1250. |
| DctWeb | String(001) | Sim | Solicitação de transmissão imediata da DCTFWeb |
| CmpSMo | Date | Sim | Primeira competência a partir da qual não Houve movimento |
| DatFec | Date | Sim | Data de fechamento |
| UsuFec | Number(010,0) | Sim | Usuário que realizou o fechamento |
| ValFec | String(001) | Sim | Não realizar as validações das regras do fechamento? |

---

## Chave Primária

- NumEmp
- FilEmp
- CmpFol
- TipFol
- SeqFol

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
