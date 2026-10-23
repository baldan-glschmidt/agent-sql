# R103PLA

## Descrição

PSS - Inspeções - Planos de ação

---

## Resumo

- Campos: 12
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodPss | Number(003,0) | Não | Código do grupo de PSS |
| CodIns | Number(004,0) | Não | Número da Inspeção |
| SeqNco | Number(003,0) | Não | Número sequencial da Não-conformidade |
| SeqPla | Number(003,0) | Não | Número sequencial do Plano de ação |
| DesAca | String(200) | Sim | Descrição da Ação |
| EmpRes | Number(004,0) | Sim | Código da empresa do responsável |
| TipCol | Number(001,0) | Sim | Tipo do Responsável |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador Responsável |
| PraDia | Number(004,0) | Sim | Definição do prazo em dias |
| DesAco | String(200) | Sim | Acompanhamento |
| DatPra | Date | Sim | Prazo para solucionar o plano de ação |

---

## Chave Primária

- NumEmp
- CodPss
- CodIns
- SeqNco
- SeqPla

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R103PLA_003

**Tabela:** R103NCO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPss | CodPss |
| CodIns | CodIns |
| SeqNco | SeqNco |

