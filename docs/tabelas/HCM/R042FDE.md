# R042FDE

## Descrição

eSocial - S-2299, S-2399 - Fechamento de Demissão

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| TipDem | Number(001,0) | Sim | Origem da demissão |
| DatPag | Date | Sim | Data Pagto da Rescisão |
| DatAfa | Date | Sim | Data do Afastamento |
| HorAfa | Number(005,0) | Sim | Hora do Afastamento |
| CauDem | Number(002,0) | Sim | Causa da Demissão |
| DatFec | Date | Sim | Data de fechamento de demissão |
| DatEnv | Date | Sim | Data limite para o envio do leiaute |
| StaFec | Number(001,0) | Sim | Status |
| GerPen | String(001) | Sim | Indicar se a alteração deve gerar uma nova pendência (S,N) |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
