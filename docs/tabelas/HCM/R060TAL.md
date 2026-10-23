# R060TAL

## Descrição

Gestão de Incidentes - Tipos de Incidente para Acerto

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
| CodTAl | Number(002,0) | Não | Código do Tipo de Alerta para Acerto |
| DesTAl | String(060) | Sim | Descrição do Tipo de Alerta para Acerto |
| TipAle | Number(002,0) | Sim | Tipo de Alerta para Acerto |
| ObsTAl | String(2499) | Sim | Observação do tipo de alerta para acerto |
| TolExt | Number(005,0) | Sim | Tolerância Limite Extras |
| ConDig | String(001) | Sim | Considerar Digitadas |
| SomDsr | String(001) | Sim | Considerar somente horário DSR |
| AbrSit | String(1000) | Sim | Abrangência Situações(+) |
| PriInc | Number(002,0) | Sim | Prioridade do incidente |
| QtDsrD | Number(002,0) | Sim | Quantidade domingos no mês que coincidem com DSR |
| ConDom | Number(001,0) | Sim | Tipo de contagem de domingos |
| QtdSem | Number(002,0) | Sim | Contagem de semanas para validar DSR |

---

## Chave Primária

- CodTAl

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
