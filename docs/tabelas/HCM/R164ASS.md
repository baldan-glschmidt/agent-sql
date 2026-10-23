# R164ASS

## Descrição

BS - Assinalamento Plano

---

## Resumo

- Campos: 14
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CodOem | Number(008,0) | Não | Codigo da Seguradora |
| CodPla | Number(003,0) | Não | Código do Plano |
| MesInc | Date | Não | Data Inclusão no Plano |
| MesExc | Date | Sim | Data Exclusão do Plano |
| DscExc | String(001) | Sim | Descontar Mês Exclusão do Plano de Saúde |
| ValIns | Number(011,2) | Sim | Valor Inscrição |
| CnaSad | String(022) | Sim | Cadastro Nacional de Saúde |
| MatPla | String(020) | Sim | Matrícula plano de saúde |
| IniAtu | Date | Sim | Início da atuação do Colaborador no Posto de trabalho |
| SeqHis | Number(002,0) | Sim | Sequência do Histórico |
| IncExc | String(001) | Sim | Tipo de operação do registro na troca de posto de trabalho |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodOem
- CodPla
- MesInc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R164ASS_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R164ASS_004

**Tabela:** R164PLA

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |
| CodPla | CodPla |

