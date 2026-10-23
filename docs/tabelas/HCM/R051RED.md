# R051RED

## Descrição

Informe/DIRF - Reembolso Plano de Saúde - Dependente

---

## Resumo

- Campos: 14
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| AnoBas | Number(004,0) | Não | Ano |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| CodOem | Number(008,0) | Não | Código da Seguradora |
| CodDep | Number(002,0) | Não | Código do Dependente |
| TipIns | Number(001,0) | Não | Tipo de Inscrição do Prestador |
| NumIns | Number(015,0) | Sim | Número de Inscrição do Prestador |
| CfjIns | String(014) | Não | Número de Inscrição do Prestador |
| NomPre | String(060) | Sim | Nome Prestador |
| ValAno | Number(011,2) | Sim | Valor Ano |
| ValAnt | Number(011,2) | Sim | Valor Ano Anterior |
| IndOri | Number(001,0) | Sim | Indicativo da origem do reembolso |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- AnoBas
- CodCal
- CodOem
- CodDep
- TipIns
- CfjIns

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R051RED_006

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

