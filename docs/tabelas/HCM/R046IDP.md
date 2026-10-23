# R046IDP

## Descrição

Informações demonstrativo pagamento - valores

---

## Resumo

- Campos: 28
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colabolador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| PerRef | Date | Sim | Competência do Cálculo |
| DatPag | Date | Sim | Data do Pagamento |
| SalBas | Number(013,4) | Sim | Salário Base |
| ValLiq | Number(013,4) | Sim | Valor líquido |
| BasIns | Number(011,2) | Sim | Base INSS Cálculo |
| BasIrf | Number(011,2) | Sim | Base de Cálculo do IRF |
| BasFgt | Number(011,2) | Sim | Base do Fgts Mensal |
| FgtMes | Number(011,2) | Sim | Valor Fgts do Mês |
| CodFai | Number(003,0) | Sim | Faixa de Desconto do Imposto de Renda |
| DepIrf | Number(002,0) | Sim | Dependentes IRRF |
| DepSaf | Number(002,0) | Sim | Número de Dependentes do Salário Família |
| ModPag | String(001) | Sim | Modo de Pagamento do Salário |
| TotVen | Number(011,2) | Sim | Total de vencimentos(+) |
| TotDes | Number(011,2) | Sim | Total de descontos(-) |
| DatGer | Date | Sim | Data da geração |
| HorGer | Number(005,0) | Sim | Hora da geração |
| BasIpe | Number(011,2) | Sim | Base IPE Cálculo |
| DifEco | Number(011,2) | Sim | Valor não descontado do Crédito do Trabalhador |
| ValEco | Number(011,2) | Sim | Valor descontado do Crédito do Trabalhador |
| MsgEco | String(100) | Sim | Mensagem sobre o valor não descontado do Crédito do Trabalhador |
| CmpAu1 | Number(011,2) | Sim | Campo auxiliar 1 |
| CmpAu2 | Number(011,2) | Sim | Campo auxiliar 2 |
| CmpAu3 | Date | Sim | Campo auxiliar 3 |
| CmpAu4 | Number(009,0) | Sim | Campo auxiliar 4 |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
