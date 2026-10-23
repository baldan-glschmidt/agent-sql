# R064SIH

## Descrição

Solicitação Individual de Horas Extras

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
| NumEmp | Number(004,0) | Não | Código da Empresa para Autorização de Extra |
| TipCol | Number(001,0) | Não | Tipo Colaborador para Autorização de Extra |
| NumCad | Number(009,0) | Não | Cadastro Colaborador para Autorização de Extra |
| DatIni | Date | Não | Data Inicial da Hora Extra |
| HorIni | Number(005,0) | Não | Hora Inicial da Hora Extra |
| HorFim | Number(005,0) | Sim | Hora Final da Hora Extra |
| DatFim | Date | Sim | Data Final da Hora Extra |
| EmpSol | Number(004,0) | Sim | Código da Empresa do Solicitante |
| TClSol | Number(001,0) | Sim | Tipo de Colaborador que Solicitou a Hora Extra |
| CadSol | Number(009,0) | Sim | Cadastro do Solicitante |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Autorização |
| MotSol | String(030) | Sim | Motivo da Solicitação de Horas Extras. |
| SolApr | String(001) | Sim | Solicitação Individual de Horas Extras Aprovada |
| DatApr | Date | Sim | Data de Análise da Solicitação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R064SIH_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

