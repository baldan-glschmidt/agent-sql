# R346IIR

## Descrição

eSocial JR - Informações de Tributos - Imposto de Renda Retido na Fonte

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
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
| ValRec | Number(015,2) | Sim | Valor relativo ao Imposto sobre a renda retido na fonte para o código da receita - rendimento mensal |
| DesRra | String(050) | Sim | Descrição dos Rendimentos Recebidos Acumuladamente (RRA) |
| QtdMes | Number(004,1) | Sim | Número de meses relativo aos Rendimentos Recebidos Acumuladamente (RRA) |
| VlrCus | Number(015,2) | Sim | Valor das despesas com custas judiciais |
| VlrAdv | Number(015,2) | Sim | Valor das despesas com advogados |
| VlrC13 | Number(015,2) | Sim | Valor relativo ao Imposto sobre a renda retido na fonte para o código de receita - 13º Salário |

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

Nenhum relacionamento cadastrado.
