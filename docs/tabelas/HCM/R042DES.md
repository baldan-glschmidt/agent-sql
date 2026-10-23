# R042DES

## Descrição

HomologNet - Descontos

---

## Resumo

- Campos: 18
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| AdtSal | Number(011,2) | Sim | Adiantamento Salarial |
| Adt13s | Number(011,2) | Sim | Adiantamento 13° Salário |
| FalDsr | Number(002,0) | Sim | Faltas/DSR |
| ValAli | Number(011,2) | Sim | Valor Vale Alimentação |
| ValVtr | Number(011,2) | Sim | Valor Vale Transporte |
| ReeAli | Number(011,2) | Sim | Reembolso de Vale Alimentação |
| ReeVtr | Number(011,2) | Sim | Reembolso de vale Transporte |
| SldDev | Number(011,2) | Sim | Saldo Devedor Empréstimo Consignado |
| ValInd | Number(011,2) | Sim | Valor Indenização (Art. 480 CLT) |
| PrePri | Number(011,2) | Sim | Contribuições Para Entidades de Previdência Privada |
| ValFap | Number(011,2) | Sim | Valor Vale Alimentação |
| DesIrf | Number(011,2) | Sim | Dedução Base de IRRF |
| CtrSin | Number(011,2) | Sim | Contribuição Sindical Laboral |
| VlrFer | Number(011,2) | Sim | Valor Compensação Dias Salário Férias Mês Afastamento |
| VlrIRF | Number(011,2) | Sim | Valor Complementação IRRF Rendimento Mês Quitação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R042DES_002

**Tabela:** R042COL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

