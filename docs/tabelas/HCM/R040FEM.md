# R040FEM

## Descrição

Recibo de Férias - Mestre

---

## Resumo

- Campos: 39
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| IniPer | Date | Não | Data Início do Período |
| IniFer | Date | Não | Data Início das Férias |
| TipFer | String(001) | Sim | N=Normais ou C=Coletivas |
| Opc13s | String(001) | Sim | Opção 13° Salário |
| PagMul | String(001) | Sim | Pagar Multa (S,N) |
| GerAdt | String(001) | Sim | Gerar Adto de Férias (S,N) |
| DatPag | Date | Sim | Data Pagto do Recibo |
| DiaFer | Number(004,2) | Sim | Dias de Férias |
| DiaAbo | Number(004,2) | Sim | Dias de Abono |
| PrvDes | Number(004,2) | Sim | % Prov. Descontos |
| ReaSal | Number(004,2) | Sim | % Reajuste Salário |
| PctAdt | Number(005,2) | Sim | % Adto Pagto Parcial |
| DiaLic | Number(004,2) | Sim | Dias Lic.Rem.Fer.Col |
| MinFed | Number(010,0) | Sim | Minutos Férias Diurno |
| MinFen | Number(010,0) | Sim | Minutos Férias Noturno |
| MinAbo | Number(010,0) | Sim | Total Minutos Abono Recibo |
| MinAbn | Number(010,0) | Sim | Minutos Abono Noturno |
| IntFer | Number(005,0) | Sim | Código Cálculo Integração Férias |
| Int13s | Number(005,0) | Sim | Código Cálculo Integração 13° Salário |
| QtdPar | Number(002,0) | Sim | Quantidade de Parcelas |
| TodInt | String(001) | Sim | Flag Que Indica Se Recibo Todo Integrado |
| DiaAbn | Number(004,2) | Sim | Dias Abonados |
| TipCau | Number(001,0) | Sim | Tipo de Férias |
| CalHfe | String(001) | Sim | Calcular Horas Férias |
| CalAdf | String(001) | Sim | Calcular Adt Férias |
| CalTfe | String(001) | Sim | Calcular 1/3 Férias |
| CalAbo | String(001) | Sim | Calcular Abono Férias |
| CalAAb | String(001) | Sim | Calcular Adic. Abono Férias |
| CalTAb | String(001) | Sim | Calcular 1/3 Abono Férias |
| FimFer | Date | Sim | Fim Férias |
| SalBas | Number(013,4) | Sim | Salário Base |
| LicRem | Number(004,2) | Sim | Dias Licença Remunerada |
| IniLic | Date | Sim | Inicio Licença Remunerada Férias |
| IntAbo | Number(001,0) | Sim | Tipo Cálculo Abono Pecuniário |
| QtdDep | Number(002,0) | Sim | Qtd. Dependentes |
| DedSim | Number(011,2) | Sim | Dedução IR Simplificado |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniPer
- IniFer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R040FEM_003

**Tabela:** R040PER

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| IniPer | IniPer |

