# R340EXP

## Descrição

Exigibilidade Suspensa - S-1210 - Deduções Previdência, FAPI e Funpresp

---

## Resumo

- Campos: 14
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CmpPag | Date | Não | Competência Pagamento |
| CodRec | Number(006,0) | Não | Código de receita relativo ao IRRF sobre rendimentos do trabalho |
| CodPro | Number(009,0) | Não | Código do Processo |
| CodSus | Number(014,0) | Não | Código Suspensão |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| SeqExp | Number(003,0) | Não | Sequência |
| TipDed | Number(001,0) | Sim | Indicativo do tipo de dedução |
| VlrDed | Number(014,2) | Sim | Valor da dedução da base de cálculo do IR com exigibilidade suspensa |
| CnpjEn | Number(014,0) | Sim | Número de inscrição da entidade de previdência complementar |
| CfjIns | String(014) | Sim | Número de inscrição da entidade de previdência complementar |
| VlrPat | Number(014,2) | Sim | Valor da contribuição do ente público patrocinador Funpresp |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpPag
- CodRec
- CodPro
- CodSus
- IndApu
- SeqExp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R340EXP_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R340EXP_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

