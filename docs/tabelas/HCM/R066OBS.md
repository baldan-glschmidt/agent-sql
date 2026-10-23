# R066OBS

## Descrição

Observação Apuração Colaborador

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatApu | Date | Não | Data da Apuração |
| CodSit | Number(003,0) | Não | Código da Situação Apurada |
| CodRat | Number(009,0) | Não | Código de Rateio da Situação |
| DesObs | String(100) | Sim | Observação na Apuração Colaborador |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatApu
- CodSit
- CodRat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R066OBS_004

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

