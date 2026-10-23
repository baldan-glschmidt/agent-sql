# R051VMU

## Descrição

Informe/DIRF - Pagamento de valores Imunes/Isentos

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| AnoBas | Number(004,0) | Não | Ano |
| TipIns | Number(001,0) | Não | Código correspondente ao tipo de inscrição |
| NumIns | Number(015,0) | Não | Número de Inscrição |
| CmpRen | Date | Não | Competência |
| RenImu | Number(011,2) | Sim | Rendimento Imune |
| RenIse | Number(011,2) | Sim | Rendimento Isento |

---

## Chave Primária

- NumEmp
- CodFil
- AnoBas
- TipIns
- NumIns
- CmpRen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R051VMU_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R051VMU_004

**Tabela:** R051IMU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| AnoBas | AnoBas |
| TipIns | TipIns |
| NumIns | NumIns |

