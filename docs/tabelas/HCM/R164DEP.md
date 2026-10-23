# R164DEP

## Descrição

BS - Assinalamento Plano - Dependentes

---

## Resumo

- Campos: 15
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Número do Colaborador |
| CodDep | Number(002,0) | Não | Código do Dependente |
| CodOem | Number(008,0) | Não | Código da Seguradora |
| CodPla | Number(003,0) | Não | Código do Plano |
| MesInc | Date | Não | Data Inclusão |
| MesExc | Date | Sim | Data Exclusão |
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
- CodDep
- CodOem
- CodPla
- MesInc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R164DEP_003

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

### IR_R164DEP_005

**Tabela:** R164PLA

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |
| CodPla | CodPla |

