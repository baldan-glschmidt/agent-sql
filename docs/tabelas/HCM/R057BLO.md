# R057BLO

## Descrição

Benefícios Bloqueados

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
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Titular |
| DatBlo | Date | Não | Data do Bloqueio do Benefício |
| HorBlo | Number(005,0) | Não | Hora do Bloqueio do Benefício |
| CodBnf | Number(002,0) | Não | Código do Benefício Bloqueado |
| EmpAut | Number(004,0) | Sim | Código da Empresa do Autorizador da Liberação |
| TClAut | Number(001,0) | Sim | Tipo de Colaborador do Autorizador da Liberação |
| CadAut | Number(009,0) | Sim | Cadastro do Autorizador da Liberação |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Bloqueou o Colaborador |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| DatLib | Date | Sim | Data de Liberação |
| HorLib | Number(005,0) | Sim | Hora de Liberação |
| ObsBlo | String(080) | Sim | Observação Bloqueio/Liberação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatBlo
- HorBlo
- CodBnf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R057BLO_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R057BLO_005

**Tabela:** R057BNF

| Origem | Destino |
|--------|---------|
| CodBnf | CodBnf |

