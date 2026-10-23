# R104PED

## Descrição

JR - Pedidos - Ação

---

## Resumo

- Campos: 7
- Chave Primária: 0 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Sim | Empresa |
| CodPrc | Number(007,0) | Sim | Código da Ação |
| DatIni | Date | Sim | Data do Pedido |
| DatFim | Date | Sim | Data do Final do Pedido |
| CodMtj | Number(003,0) | Sim | Código do Motivo do Pedido |
| VlrRec | Number(011,2) | Sim | Valor Reclamado |
| PedPro | String(001) | Sim | Pedido Procedente |

---

## Chave Primária

Não possui.

---

## Índices

### R104PEDIndice1

**Tipo:** Não unico

Campos:
- NumEmp
- CodPrc

---

## Relacionamentos

### IR_R104PED_001

**Tabela:** R104PRJ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |

### IR_R104PED_004

**Tabela:** R104MTJ

| Origem | Destino |
|--------|---------|
| CodMtj | CodMtj |

