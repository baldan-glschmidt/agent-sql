# R138OCP

## Descrição

Orçamento por Centro de Custo - Participantes do Curso

---

## Resumo

- Campos: 12
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCcu | String(018) | Não | Código Centro Custo Contábil |
| AnoBas | Number(004,0) | Não | Ano Base do Orçamento |
| MesBas | Number(002,0) | Não | Mês Base do Orçamento |
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| SeqCus | Number(003,0) | Não | Sequência de Custos |
| EmpPar | Number(004,0) | Não | Código da empresa do participante |
| TipCol | Number(001,0) | Não | Tipo Colaborador do Curso |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| ObjCur | String(1000) | Sim | Objetivo do curso |
| ResCur | String(1000) | Sim | Resultado esperado com o curso |
| CodMcu | Number(003,0) | Sim | Tipo de Motivo |

---

## Chave Primária

- NumEmp
- CodCcu
- AnoBas
- MesBas
- CodCua
- SeqCus
- EmpPar
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R138OCP_005

**Tabela:** R138OCC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |
| AnoBas | AnoBas |
| MesBas | MesBas |
| CodCua | CodCua |
| SeqCus | SeqCus |

