# R351IRT

## Descrição

S-2501 - eSocial - Informações complementares relacionadas a rendimentos tributáveis

---

## Resumo

- Campos: 22
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| NumPro | String(020) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| PerApu | Date | Não | Mês/ano em que é devida a obrigação de pagar a parcela prevista no acordo/sentença |
| SeqTpt | Number(009,0) | Não | Sequência |
| SeqPar | Number(005,0) | Não | Sequência parcial |
| SeqItp | Number(009,0) | Não | Sequência Trabalhador |
| SeqIrr | Number(009,0) | Não | Sequência Informações de Imposto de Renda Retido na Fonte |
| SeqIrt | Number(009,0) | Não | Sequência Rendimentos Tributáveis |
| VlrRtr | Number(015,2) | Sim | Valor do rendimento tributável mensal do Imposto de Renda |
| VlrR13 | Number(015,2) | Sim | Valor do rendimento tributável mensal do Imposto de Renda referente ao 13º salário |
| VlrMog | Number(015,2) | Sim | Valor do rendimento isento por ser portador de moléstia grave atestada por laudo médico |
| VlrR65 | Number(015,2) | Sim | Valor de parcela isenta de aposentadoria para beneficiário de 65 anos ou mais |
| VlrJur | Number(015,2) | Sim | Juros de mora recebidos, atraso no pagamento de remuneração por exercício de emprego, cargo ou função |
| VlrRNt | Number(015,2) | Sim | Valor de outros rendimentos isentos ou não tributáveis |
| DesRNt | String(060) | Sim | Descrição do rendimento isento ou não tributável |
| VlrPre | Number(015,2) | Sim | Valor referente a previdência oficial |
| VlMo13 | Number(015,2) | Sim | Valor relativo ao Imposto sobre a renda retido na fonte para o código de receita - 13º Salário |
| VlAp13 | Number(015,2) | Sim | Valor de parcela isenta de aposentadoria para beneficiário de 65 anos ou mais 13º |
| VlJu13 | Number(015,2) | Sim | Juros de mora recebidos, atraso no pagamento de remuneração por exercício de emprego, cargo ou função 13º |
| VlPr13 | Number(015,2) | Sim | Valor referente à previdência oficial 13º |
| PidExc | String(050) | Não | Identificador da pendência para execução |

---

## Chave Primária

- NumEmp
- FilEmp
- NumPro
- PerApu
- SeqTpt
- SeqPar
- SeqItp
- SeqIrr
- SeqIrt

---

## Índices

### R351IRTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
