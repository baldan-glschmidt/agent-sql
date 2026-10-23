# R340EXS

## Descrição

Exigibilidade Suspensa - S-1210

---

## Resumo

- Campos: 14
- Chave Primária: 8 campo(s)
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
| StaInf | Number(001,0) | Sim | Status Informações |
| VlrRet | Number(014,2) | Sim | Valor da retenção que deixou de ser efetuada - processo admin. ou judicial. |
| VlDepJ | Number(014,2) | Sim | Valor do depósito judicial em função de processo administrativo ou judicial |
| VlrAno | Number(014,2) | Sim | Valor da compensação relativa ao ano calendário em função de processo judicial |
| VlrAnt | Number(014,2) | Sim | Valor da compensação relativa a anos anteriores em função de processo judicial |
| VlrRen | Number(014,2) | Sim | Valor do rendimento com exigibilidade suspensa |

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

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R340EXS_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R340EXS_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

