# R064SHE

## Descrição

Solicitação de Horas Extras

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCcu | String(018) | Não | Código Centro Custo para a Solicitação |
| CodVin | Number(003,0) | Não | Código do Vínculo |
| DatIni | Date | Não | Data Inicial da Solicitação de Hora Extra |
| HorIni | Number(005,0) | Não | Hora Inicial da Solicitação |
| DatFim | Date | Sim | Data Final da Solicitação de Hora Extra |
| HorFim | Number(005,0) | Sim | Hora Inicial da Solicitação |
| QtdSol | Number(004,0) | Sim | Qtde de Pessoas Solicitadas para Extras |
| MotSol | String(030) | Sim | Motivo da Solicitação de Horas Extras. |
| QtdApr | Number(004,0) | Sim | Qtde de Pessoas Aprovadas para Extra no Período |
| DatApr | Date | Sim | Data de Análise da Solicitação |

---

## Chave Primária

- NumEmp
- CodCcu
- CodVin
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R064SHE_001

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

