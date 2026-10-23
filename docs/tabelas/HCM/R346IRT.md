# R346IRT

## Descrição

eSocial JR - Informações de Tributos - Informações complementares relacionadas a rendimentos tributáveis

---

## Resumo

- Campos: 18
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
| VlrRtr | Number(015,2) | Sim | Valor do rendimento tributável mensal do Imposto de Renda |
| VlrR13 | Number(015,2) | Sim | Valor do rendimento tributável do Imposto de Renda referente ao 13º salário |
| VlrMog | Number(015,2) | Sim | Valor do rendimento isento por ser portador de moléstia grave atestada por laudo médico |
| VlrR65 | Number(015,2) | Sim | Valor de parcela isenta de aposentadoria para beneficiário de 65 anos ou mais |
| VlrJur | Number(015,2) | Sim | Juros de mora recebidos, atraso no pagamento de remuneração por exercício de emprego, cargo ou função |
| VlrRNt | Number(015,2) | Sim | Valor de outros rendimentos isentos ou não tributáveis |
| DesRNt | String(060) | Sim | Descrição do rendimento isento ou não tributável |
| VlrPre | Number(015,2) | Sim | Valor referente à previdência oficial |
| VlMo13 | Number(015,2) | Sim | Valor relativo ao Imposto sobre a renda retido na fonte para o código de receita - 13º Salário |
| VlAp13 | Number(015,2) | Sim | Valor de parcela isenta de aposentadoria para beneficiário de 65 anos ou mais 13º |
| VlJu13 | Number(015,2) | Sim | Juros de mora recebidos, atraso no pagamento de remuneração por exercício de emprego, cargo ou função 13º |
| VlPr13 | Number(015,2) | Sim | Valor referente à previdência oficial 13º |

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
