# R046PRF

## Descrição

Provisões c/ Rateio - Contas Financeiras

---

## Resumo

- Campos: 48
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| MesAno | Date | Não | Competência das Provisões |
| CodRat | Number(009,0) | Não | Código do Rateio |
| ConFin | Number(007,0) | Não | Conta Financeira |
| Bas13s | Number(011,2) | Sim | Base Provisão 13° Salário |
| Pan13s | Number(011,2) | Sim | Provisão 13° Salário Anterior |
| Pan13i | Number(011,2) | Sim | Provisão INSS 13° Salário Anterior |
| Pan13f | Number(011,2) | Sim | Provisão FGTS 13° Salário Anterior |
| Pan13p | Number(011,2) | Sim | Provisão Pis 13° Salário Anterior |
| Prv13s | Number(011,2) | Sim | Provisão 13° Salário do Mês |
| Ins13s | Number(011,2) | Sim | Provisão INSS sobre 13° Salário |
| Fgt13s | Number(011,2) | Sim | Provisão FGTS sobre 13° Salário |
| Pis13s | Number(011,2) | Sim | Provisão PIS sobre 13° Salário |
| Asl13s | Number(011,2) | Sim | Ajuste Saldo Provisão 13° Salário |
| Ain13s | Number(011,2) | Sim | Ajuste Saldo provisão INSS 13° salário |
| Afg13s | Number(011,2) | Sim | Ajuste Saldo Provisão FGTS 13° Salário |
| Api13s | Number(011,2) | Sim | Ajuste Saldo provisão PIS 13° salário |
| BasFer | Number(011,2) | Sim | Base Provisão de Férias |
| PanFer | Number(011,2) | Sim | Provisão Férias Anterior |
| PanFet | Number(011,2) | Sim | Provisão 1/3 Férias Anterior |
| PanFei | Number(011,2) | Sim | Provisão INSS Férias Anterior |
| PanFef | Number(011,2) | Sim | Provisão FGTS Férias Anterior |
| PanFep | Number(011,2) | Sim | Provisão PIS Férias Anterior |
| PrvFer | Number(011,2) | Sim | Provisão de Férias do Mês |
| TerFer | Number(011,2) | Sim | Provisão 1/3 Férias do Mês |
| InsFer | Number(011,2) | Sim | Provisão INSS Férias do Mês |
| FgtFer | Number(011,2) | Sim | Provisão FGTS Férias do Mês |
| PisFer | Number(011,2) | Sim | Provisão PIS Férias do Mês |
| AslFer | Number(011,2) | Sim | Ajuste Saldo provisão férias |
| AteFer | Number(011,2) | Sim | Ajuste saldo provisão 1/3 férias |
| AinFer | Number(011,2) | Sim | Ajuste saldo provisão INSS férias |
| AfgFer | Number(011,2) | Sim | Ajuste saldo provisão FGTS férias |
| ApiFer | Number(011,2) | Sim | Ajuste saldo provisão PIS férias |
| PagFer | Number(011,2) | Sim | Valor das Férias Pagas |
| PagTer | Number(011,2) | Sim | Valor do 1/3 de Férias Pago |
| PagIns | Number(011,2) | Sim | Valor do Inss s/ Férias Pagas |
| PagFgt | Number(011,2) | Sim | Valor do Fgts s/ Férias Pagas |
| PagPis | Number(011,2) | Sim | Valor do Pis s/ Férias Pagas |
| Pag13s | Number(011,2) | Sim | 13° Salário Pago do Mês |
| PIn13s | Number(011,2) | Sim | INSS sobre 13° Salário Pago |
| PFg13s | Number(011,2) | Sim | FGTS sobre 13° Salário Pago |
| PPi13s | Number(011,2) | Sim | PIS 13° Salário Pago |
| Ind13s | Number(011,2) | Sim | 13° Salário Ind. do Mês |
| IFg13s | Number(011,2) | Sim | FGTS sobre 13° Salário Ind. |
| IPi13s | Number(011,2) | Sim | PIS 13° Salário Ind. |
| Adt13s | Number(011,2) | Sim | 13° Salário Adto. do Mês |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- MesAno
- CodRat
- ConFin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R046PRF_004

**Tabela:** R046PRR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| MesAno | MesAno |
| CodRat | CodRat |

