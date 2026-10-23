# R071AGE

## Descrição

Agendamento da Autorização de Entrada

---

## Resumo

- Campos: 14
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatPrv | Date | Não | Data Prevista da Autorização de Entrada |
| HorPrv | Number(005,0) | Não | Hora Prevista da Autorização de Entrada |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodPrm | Number(005,0) | Sim | Código da Permissão da Autorização de Entrada |
| DatVal | Date | Sim | Data de Validade da Autorização |
| HorVal | Number(005,0) | Sim | Hora de Validade da Autorização |
| EmpAut | Number(004,0) | Sim | Código da Empresa do Autorizador do Agendamento |
| TClAut | Number(001,0) | Sim | Tipo de Colaborador do Autorizador do Agendamento |
| CadAut | Number(009,0) | Sim | Cadastro do Autorizador do Agendamento |
| ObsAgA | String(080) | Sim | Observação do Agendamento |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou o Agendamento |
| AenUti | String(001) | Sim | Agendamento foi realizado. |

---

## Chave Primária

- DatPrv
- HorPrv
- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R071AGE_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

