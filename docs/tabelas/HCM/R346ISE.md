# R346ISE

## Descrição

eSocial JR - Processo Trabalhista - Rendimentos Isentos exclusivos do CR 0561

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodPro | Number(009,0) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| CmpPag | Date | Não | Mês/ano em que é devida a obrigação de pagar a parcela prevista no acordo/sentença |
| CodRec | Number(006,0) | Não | Código de Receita - CR relativo a Imposto de Renda Retido na Fonte |
| VlrDia | Number(015,2) | Sim | Valor relativo a diárias |
| VlrAju | Number(015,2) | Sim | Valor relativo à ajuda de custo |
| VlrRes | Number(015,2) | Sim | Valor relativo à indenização e rescisão de contrato, inclusive a título de PDV e acidentes de trabalho |
| VlrPec | Number(015,2) | Sim | Valor relativo ao abono pecuniário |
| VlrMor | Number(015,2) | Sim | Valor relativo ao auxílio-moradia |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPro
- CmpPag
- CodRec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R346ISE_005

**Tabela:** R346IIR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodPro | CodPro |
| CmpPag | CmpPag |
| CodRec | CodRec |

