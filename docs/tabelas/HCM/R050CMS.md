# R050CMS

## Descrição

Compensações DARF

---

## Resumo

- Campos: 12
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRec | Number(004,0) | Não | Código da Receita |
| DatApu | Date | Não | Data da Apuração |
| NumPar | Number(002,0) | Não | Número da Parcela |
| ApuCmp | Date | Não | Data de Apuração da Compensação |
| ParCmp | Number(002,0) | Não | Número da Parcela da Compensação |
| VenCmp | Date | Sim | Data de Vencimento da Compensação |
| SldCor | Number(011,2) | Sim | Valor do Saldo Corrigido |
| ValCmp | Number(011,2) | Sim | Valor Compensado |
| CorCmp | Number(011,2) | Sim | Compensação Corrigida |
| ValSld | Number(011,2) | Sim | Valor do Saldo da Compensação |

---

## Chave Primária

- NumEmp
- CodFil
- CodRec
- DatApu
- NumPar
- ApuCmp
- ParCmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R050CMS_004

**Tabela:** R050CMG

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodRec | CodRec |
| DatApu | DatApu |
| NumPar | NumPar |

