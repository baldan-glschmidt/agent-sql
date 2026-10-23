# R032PNI

## Descrição

Pagamentos Não Identificados

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CmpPNI | Date | Não | Competência |
| SeqPNI | Number(004,0) | Não | Sequência |
| DatPag | Date | Sim | Data de Pagamento |
| CmpRef | Date | Sim | Competência Referência |
| VlrLiq | Number(014,2) | Sim | Valor Líquido |
| VlrRea | Number(014,2) | Sim | Valor Reajustado |
| VlrIrr | Number(014,2) | Sim | Valor IRRF |

---

## Chave Primária

- NumEmp
- CodFil
- CmpPNI
- SeqPNI

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R032PNI_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

