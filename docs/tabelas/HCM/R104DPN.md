# R104DPN

## Descrição

JR - Recursos - Ação Dependente (Apensada)

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
- Índices: 2
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| DatDep | Date | Não | Data de Depósito |
| EmpAca | Number(004,0) | Não | Empresa da ação dependente |
| CodAca | Number(007,0) | Não | Código da ação dependente |

---

## Chave Primária

- NumEmp
- CodPrc
- DatDep
- EmpAca
- CodAca

---

## Índices

### R104DPNIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CodPrc

### R104DPNIndice3

**Tipo:** Não unico

Campos:
- EmpAca
- CodAca

---

## Relacionamentos

### IR_R104DPN_001

**Tabela:** R104PRJ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |

### IR_R104DPN_002

**Tabela:** R104DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |
| DatDep | DatDep |

### IR_R104DPN_004

**Tabela:** R104PRJ

| Origem | Destino |
|--------|---------|
| EmpAca | NumEmp |
| CodAca | CodPrc |

