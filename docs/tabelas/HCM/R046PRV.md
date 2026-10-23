# R046PRV

## Descrição

Provisões

---

## Resumo

- Campos: 81
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| MesAno | Date | Não | Competência Provisões |
| Bas13s | Number(011,2) | Sim | Base Provisão 13° Salário |
| B13Sal | Number(011,2) | Sim | Base Provisão 13° Salário - Sal.Fixo |
| B13Adi | Number(011,2) | Sim | Base Provisão 13° Salário - Adicionais |
| B13Mhe | Number(011,2) | Sim | Base Provisão 13° Salário - M.H.Extras |
| B13Mvv | Number(011,2) | Sim | Base Provisão 13° Salário - M.V.Variav |
| Ben13s | Number(011,2) | Sim | Base Provisão 13° Salário - Encargos |
| Pan13s | Number(011,2) | Sim | Provisão 13° salário Anterior |
| Pan13i | Number(011,2) | Sim | Provisão INSS 13° salário Anterior |
| Pan13f | Number(011,2) | Sim | Provisão FGTS 13° Salário Anterior |
| Pan13p | Number(011,2) | Sim | Provisão PIS 13° Salário Anterior |
| Prv13s | Number(011,2) | Sim | Provisão 13° Salário do Mês |
| Ins13s | Number(011,2) | Sim | Provisão INSS sobre 13° Salário |
| Fgt13s | Number(011,2) | Sim | Provisão FGTS sobre 13° Salário |
| Pis13s | Number(011,2) | Sim | Provisão PIS 13° Salário |
| Asl13s | Number(011,2) | Sim | Ajuste Saldo provisão 13° salário |
| Ain13s | Number(011,2) | Sim | Ajuste Saldo provisão INSS 13° salário |
| Afg13s | Number(011,2) | Sim | Ajuste Saldo Provisão FGTS 13° Salário |
| Api13s | Number(011,2) | Sim | Ajuste Saldo provisão PIS 13° salário |
| BasFer | Number(011,2) | Sim | Remuneração p/ Provisão de Férias |
| BasTer | Number(011,2) | Sim | Base Adicional 1/3 de Férias |
| BfeSal | Number(011,2) | Sim | Base Provisão Férias - Salário Fixo |
| BfeAdi | Number(011,2) | Sim | Base Provisão Férias - Adicionais |
| BfeMhe | Number(011,2) | Sim | Base Provisão Férias - Média Horas Extras |
| BfeMvv | Number(011,2) | Sim | Base Provisão Férias - Média Valores Variáveis |
| BenFer | Number(011,2) | Sim | Base Provisão Férias - Encargos |
| PanFer | Number(011,2) | Sim | Saldo Anterior da Provisão de Férias |
| PanFet | Number(011,2) | Sim | Saldo Anterior Provisão 1/3 Férias |
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
| PgmFer | Number(011,2) | Sim | Valor das Férias Pagas a Maior |
| PgmTer | Number(011,2) | Sim | Valor do 1/3 Pago a Maior |
| PgmIns | Number(011,2) | Sim | Valor do Inss s/ Férias Pagas a Maior |
| PgmFgt | Number(011,2) | Sim | Valor do Fgts s/ Férias Pagas a Maior |
| PgmPis | Number(011,2) | Sim | Valor do Pis s/ Férias Pagas a Maior |
| OriFer | String(001) | Sim | Origem Provisão (C,D,I) |
| Ori13s | String(001) | Sim | Origem Provisão (C,D,I) |
| Avo13s | Number(002,0) | Sim | Avos 13° Salário |
| SldFer | Number(005,2) | Sim | Saldo Último Período |
| QtdDir | Number(005,2) | Sim | Direito Último Período |
| IniPri | Date | Sim | Início do Primeiro Período de Férias c/ Saldo |
| UltPer | Date | Sim | Início do Último Período de Férias c/ Saldo |
| FimUlt | Date | Sim | Fim do Último Período de Férias |
| AvoPer | Number(002,0) | Sim | Avos Último Período Férias |
| PerFgt | Number(004,2) | Sim | % Provisão FGTS |
| PerIns | Number(006,4) | Sim | % Provisão INSS |
| PerPis | Number(004,2) | Sim | % Provisão PIS |
| PrvBai | String(001) | Sim | Provisão Baixa |
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
| AssPag | String(001) | Sim | Assinalamento - Pago (S,N) |
| ApgFer | Number(011,2) | Sim | Ajuste Férias Pagas a Maior |
| ApgTer | Number(011,2) | Sim | Ajuste 1/3 Pago a Maior |
| ApgIns | Number(011,2) | Sim | Ajuste Inss s/ Férias Pagas a Maior |
| ApgFgt | Number(011,2) | Sim | Ajuste Fgts s/ Férias Pagas a Maior |
| ApgPis | Number(011,2) | Sim | Ajuste Pis s/ Férias Pagas a Maior |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- MesAno

---

## Índices

### R046PRVIndice2

**Tipo:** Não unico

Campos:
- MesAno
- NumEmp
- TipCol
- NumCad

### R046PRVIndice3

**Tipo:** Não unico

Campos:
- NumCad
- MesAno

---

## Relacionamentos

### IR_R046PRV_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

