# R088LRB

## Descrição

Lançamentos de Reembolso

---

## Resumo

- Campos: 12
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa do Colabolador Usuário do Veículo |
| TipCol | Number(001,0) | Não | Tipo do Colabolador Usuário do Veículo |
| NumCad | Number(009,0) | Não | Cadastro do Colabolador Usuário do Veículo |
| MedIni | Date | Não | Medição Inicial do Reembolso |
| MedFim | Date | Sim | Medição Final do Reembolso |
| ValRec | Number(015,3) | Sim | Valor à Receber de Reembolso |
| ValPar | Number(015,3) | Sim | Valor à Particular de Reembolso (Desconto) |
| ValLiq | Number(015,3) | Sim | Valor Líquido à Receber de Reembolso |
| SitLrb | Number(001,0) | Sim | Situação do Reembolso de Comodatário |
| DatLrb | Date | Sim | Data de Lançamento do Reembolso |
| DatApr | Date | Sim | Data de Aprovação do Reembolso |
| DatExp | Date | Sim | Data de Exportação do Reebolso |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- MedIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088LRB_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

