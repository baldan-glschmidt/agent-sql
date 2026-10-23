# R346IVL

## Descrição

eSocial JR - Informações de Tributos - Informações de valores relacionados à não retenção de tributos ou a depósitos judiciais

---

## Resumo

- Campos: 14
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 0

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
| NumPro | Number(009,0) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| CodSus | Number(014,0) | Não | Código Suspensão |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| VlrNre | Number(015,2) | Sim | Valor da retenção que deixou de ser efetuada em função de processo administrativo ou judicial |
| VlrDju | Number(015,2) | Sim | Valor do depósito judicial em função de processo administrativo ou judicial |
| VlrAnc | Number(015,2) | Sim | Valor da compensação relativa ao ano calendário em função de processo judicial |
| VlrAnt | Number(015,2) | Sim | Valor da compensação relativa a anos anteriores em função de processo judicial |
| VlrSus | Number(015,2) | Sim | Valor do rendimento com exigibilidade suspensa |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPro
- CmpPag
- CodRec
- NumPro
- CodSus
- IndApu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
