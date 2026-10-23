# R212COM

## Descrição

Entrevista de Desligamento - Comunicação de Desligamento

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa do Colaborador Desligado |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatCom | Date | Não | Data da Comunicação de Desligamento |
| SitCom | Number(001,0) | Sim | Situação da comunicação de desligamento |
| IniEmp | String(001) | Sim | Indica se a iniciativa de desligamento partiu da empresa |
| CodRmd | Number(003,0) | Sim | Código do Motivo da Demissão |
| CauDem | Number(002,0) | Sim | Causa da Demissão |
| ObsSol | String(2000) | Sim | Anotações |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatCom

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
