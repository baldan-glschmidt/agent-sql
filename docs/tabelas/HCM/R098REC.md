# R098REC

## Descrição

Revisões Equipamentos - Checklist

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipEqp | Number(003,0) | Não | Código Tipo de Equipamento |
| CodEqp | Number(006,0) | Não | Código do Equipamento |
| TipSvc | Number(003,0) | Não | Código Tipo de Serviço |
| DatRev | Date | Não | Data da Revisão |
| CodCkl | Number(003,0) | Não | Código |
| SitCkl | String(001) | Sim | Indica se o item está com alguma anormalidade(S/N) |
| ObsCkl | String(700) | Sim | Observações sobre o item que foi checado |
| SelPro | String(001) | Sim | Seleção do procedimento para manutenção do equipamento. |

---

## Chave Primária

- NumEmp
- TipEqp
- CodEqp
- TipSvc
- DatRev
- CodCkl

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R098REC_004

**Tabela:** R098REV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipEqp | TipEqp |
| CodEqp | CodEqp |
| TipSvc | TipSvc |
| DatRev | DatRev |

### IR_R098REC_005

**Tabela:** R098CKL

| Origem | Destino |
|--------|---------|
| CodCkl | CodCkl |

