# R046IRF

## Descrição

Imposto de Renda Retido

---

## Resumo

- Campos: 22
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CmpIrf | Date | Não | Competência do IRF |
| SeqIrf | Number(002,0) | Não | Sequência do IR no Mês |
| OriIrf | Number(002,0) | Sim | Rotina Origem (1 a 10) |
| TipIrf | String(001) | Sim | Tipo de Imposto Renda |
| DatPag | Date | Sim | Data do Pagto |
| BasCal | Number(011,2) | Sim | Base de Cálculo do IRF |
| IrfRet | Number(011,2) | Sim | Valor IRF Retido do Empregado |
| IrfRec | Number(011,2) | Sim | Valor IRF Recolhido Relatório |
| CorIrf | Number(011,2) | Sim | Valor Correção IRF Relatório |
| IrRein | Number(011,2) | Sim | Valor IRF a ser recolhido pela EFD-Reinf |
| DedSim | Number(011,2) | Sim | Base dedução simplificada |
| SitRec | String(001) | Sim | Situação Recolhimento (S,N) |
| DepIrf | Number(002,0) | Sim | Qtde de Dependentes do IRF |
| DatRec | Date | Sim | Data Recolhimento no Relatório |
| DatRf1 | Date | Sim | Data de Referência 1 |
| DatRf2 | Date | Sim | Data de Referência 2 |
| DatRf3 | Date | Sim | Data de Referência 3 |
| CodCal | Number(005,0) | Sim | Código Cálculo Gerador |
| SeqVal | Number(002,0) | Sim | Sequência do Vale no Dia |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpIrf
- SeqIrf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R046IRF_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

