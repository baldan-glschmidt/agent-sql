# R046INF

## Descrição

Informação do Colaborador no Cálculo

---

## Resumo

- Campos: 20
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| DepIrf | Number(002,0) | Sim | Dependentes IRRF |
| DepSaf | Number(002,0) | Sim | Dependentes Sal. Família |
| DatPag | Date | Sim | Data do Pagamento |
| IniCmp | Date | Sim | Data Início Período Folha |
| FimCmp | Date | Sim | Data Final Período Folha |
| PerRef | Date | Sim | Competência do Cálculo |
| TipSal | Number(001,0) | Sim | Tipo de Salário |
| SalEmp | Number(013,4) | Sim | Salário Base |
| ValCon | Number(013,4) | Sim | Valor pago de contribuição sindical |
| TipCon | Number(001,0) | Sim | Tipo de recolhimento contribuição sindical |
| TipCal | Number(002,0) | Sim | Tipo do Cálculo |
| ApoEsp | Number(002,0) | Sim | Número Anos p/ Aposentadoria Especial |
| BasIns | Number(011,2) | Sim | Base INSS Cálculo |
| IntRcs | String(001) | Sim | Integrou Rescisão |
| QtDepFP | Number(002,0) | Sim | Quantidade de Dependentes RPPS |
| DedSim | Number(011,2) | Sim | Dedução IR Simplificado |

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
