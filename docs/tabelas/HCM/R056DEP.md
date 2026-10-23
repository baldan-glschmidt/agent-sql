# R056DEP

## Descrição

Depósitos FGTS p/ Colaborador

---

## Resumo

- Campos: 30
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CmpFgt | Date | Não | Competência |
| FgtBas | Number(011,2) | Sim | Base do Fgts Mensal |
| FgtMes | Number(011,2) | Sim | Valor Fgts do Mês |
| FgtBar | Number(011,2) | Sim | Base do Fgts Recolhido |
| FgtRec | Number(011,2) | Sim | Valor Fgts Recolhido |
| FgtAdc | Number(011,2) | Sim | Valor Fgts Adicional Mês |
| FgtAdr | Number(011,2) | Sim | Valor Fgts Adicional Recolhido |
| FgtDat | Date | Sim | Data Recolhimento Fgts do Mês |
| FgtPag | String(001) | Sim | FGTS Pago |
| F13Bas | Number(011,2) | Sim | Base do Fgts de 13° Salário |
| F13Mes | Number(011,2) | Sim | Valor Fgts 13° Salário |
| F13Bar | Number(011,2) | Sim | Base do Fgts de 13° Salário Recolhido |
| F13Rec | Number(011,2) | Sim | Fgts 13° Salário Recolhido |
| F13Adc | Number(011,2) | Sim | Valor Fgts Adicional 13° Salário |
| F13Adr | Number(011,2) | Sim | Fgts Adicional 13° Salário Recolhido |
| F13Dat | Date | Sim | Data Recolhimento Fgts 13° Salário |
| F13Pag | String(001) | Sim | FGTS 13° Salário Pago |
| OriDep | String(001) | Sim | Origem do Depósito de FGTS |
| SitRec | Number(001,0) | Sim | Situação |
| DisMes | Number(011,2) | Sim | Valor Dissídio Mês |
| Dis13s | Number(011,2) | Sim | Valor Dissídio 13° Salário |
| RecMes | Number(011,2) | Sim | Valor Reclamatória Mês |
| Rec13s | Number(011,2) | Sim | Valor Reclamatória 13° Salário |
| BfgAtm | Number(011,2) | Sim | Base FGTS Acidente Trabalho Mês |
| VfgAtm | Number(011,2) | Sim | Valor FGTS Acidente Trabalho Mês |
| BfgAtd | Number(011,2) | Sim | Base FGTS Acidente Trabalho 13º Salário |
| VfgAtd | Number(011,2) | Sim | Valor FGTS Acidente Trabalho 13º Salário |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpFgt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R056DEP_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

