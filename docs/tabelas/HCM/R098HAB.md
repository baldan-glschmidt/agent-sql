# R098HAB

## Descrição

Habilitação

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| TipEqp | Number(003,0) | Não | Código Tipo de Equipamento |
| CodEqp | Number(006,0) | Não | Código do Equipamento |
| DatIni | Date | Não | Data de início da habilitação |
| NecTre | String(001) | Sim | Necessário realização de treinamento para considerar habilitado |
| NecExa | String(001) | Sim | Necessário realização de exame para considerar habilitado |
| DatTer | Date | Sim | Data de término da habilitação |
| ObsHab | String(080) | Sim | Observação |
| CodUsu | Number(010,0) | Sim | Código do usuário que alterou as informações da habilitação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TipEqp
- CodEqp
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R098HAB_003

**Tabela:** R098TEQ

| Origem | Destino |
|--------|---------|
| TipEqp | TipEqp |

### IR_R098HAB_004

**Tabela:** R098EQP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipEqp | TipEqp |
| CodEqp | CodEqp |

