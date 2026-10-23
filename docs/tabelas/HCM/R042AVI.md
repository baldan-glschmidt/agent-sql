# R042AVI

## Descrição

Aviso Prévio Colaborador

---

## Resumo

- Campos: 17
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| DatAvi | Date | Não | Data do Aviso Prévio |
| DatDem | Date | Sim | Data da Demissão |
| DatPag | Date | Sim | Data Pagto da Rescisão |
| FinAvi | Date | Sim | Data Final do Aviso |
| QtdAvi | Number(005,2) | Sim | Dias Aviso Prévio |
| QtdAcr | Number(005,2) | Sim | Dias Acréscimo Aviso Prévio |
| TipAvi | Number(001,0) | Sim | Tipo de Aviso Prévio |
| CauDem | Number(002,0) | Sim | Causa da Demissão |
| TipeSo | Number(001,0) | Sim | Tipo de Aviso Prévio para o eSocial |
| ObsAvi | String(255) | Sim | Observação do Aviso Prévio |
| TipGra | Number(001,0) | Sim | Tipo Gravação |
| DatCan | Date | Sim | Data Cancelamento |
| MotCan | Number(001,0) | Sim | Motivo Cancelamento |
| ObsCan | String(255) | Sim | Observação Cancelamento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAvi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R042AVI_010

**Tabela:** R042CAU

| Origem | Destino |
|--------|---------|
| CauDem | CauDem |

