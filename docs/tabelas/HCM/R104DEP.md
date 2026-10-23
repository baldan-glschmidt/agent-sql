# R104DEP

## Descrição

JR - Recursos

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| DatDep | Date | Não | Data de Depósito |
| ValDep | Number(011,2) | Sim | Valor |
| RecDir | Number(001,0) | Sim | Recurso Dirigido |
| DtRDep | Date | Sim | Data de Retorno Depósito |
| VlRDep | Number(011,2) | Sim | Valor Retorno Depósito |
| SenRec | String(5000) | Sim | Sentença Recurso |
| DtCDep | Date | Sim | Data correção do depósito recursal |
| VlCDep | Number(011,2) | Sim | Valor corrigido do depósito recursal |

---

## Chave Primária

- NumEmp
- CodPrc
- DatDep

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104DEP_001

**Tabela:** R104PRJ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |

