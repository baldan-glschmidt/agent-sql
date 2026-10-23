# R054CMG

## Descrição

Compensações da GPS - Mestre

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRat | Number(009,0) | Não | Código do Rateio |
| ComCmp | Date | Não | Competência da Compensação |
| OriCom | Number(001,0) | Não | Origem da Compensação |
| DatRec | Date | Sim | Data de Recolhimento |
| CmpOri | Number(011,2) | Sim | Valor a Compensar Original |
| ObsCmp | String(050) | Sim | Observação da Compensação |
| AcoPar | String(001) | Sim | Acordo Parcelamento |

---

## Chave Primária

- NumEmp
- CodFil
- CodRat
- ComCmp
- OriCom

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R054CMG_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

