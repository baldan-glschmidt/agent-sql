# R098USO

## Descrição

Histórico de uso de equipamentos

---

## Resumo

- Campos: 10
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
| InsUso | String(001) | Sim | Instruções de Uso (S,N) |
| DatTer | Date | Sim | Data de término da habilitação |
| ObsUso | String(080) | Sim | Observação |
| CodUsu | Number(010,0) | Sim | Código do usuário que alterou as informações do histórico de uso |

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

### IR_R098USO_003

**Tabela:** R098TEQ

| Origem | Destino |
|--------|---------|
| TipEqp | TipEqp |

### IR_R098USO_004

**Tabela:** R098EQP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipEqp | TipEqp |
| CodEqp | CodEqp |

