# R046HOL

## Descrição

Informações holerite - Colaborador

---

## Resumo

- Campos: 54
- Chave Primária: 4 campo(s)
- Índices: 3
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colabolador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| FilMat | Number(006,0) | Sim | Código da Filial |
| RazSoc | String(100) | Sim | Razão Social |
| TInMat | Number(001,0) | Sim | Tipo de Inscrição Matriz |
| DInMat | String(010) | Sim | Descrição Tipo de Inscrição Matriz |
| InsMat | Number(015,0) | Sim | Número da Inscrição Matriz |
| CfjMat | String(014) | Sim | Número da Inscrição Matriz |
| CodFil | Number(006,0) | Sim | Código da Filial |
| TipIns | Number(001,0) | Sim | Tipo de Inscrição |
| DTpIns | String(010) | Sim | Descrição Tipo de Inscrição |
| NumIns | Number(015,0) | Sim | Número da Inscrição |
| CfjIns | String(014) | Sim | Número da Inscrição |
| NomCom | String(080) | Sim | Nome Completo |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| NumCid | String(016) | Sim | Número da Carteira de Identidade |
| DatNas | Date | Sim | Data de Nascimento |
| NomMae | String(070) | Sim | Nome da mãe do trabalhador |
| NomPai | String(070) | Sim | Nome do Pai do Trabalhador |
| NumTel | String(030) | Sim | Número do Telefone |
| NmTel2 | String(030) | Sim | Número do Telefone 2 |
| NumCel | String(030) | Sim | Número do Celular |
| EmaCom | String(100) | Sim | Endereço do Correio Eletrônico (E-mail) Comercial |
| EmaPar | String(100) | Sim | Endereço do Correio Eletrônico (E-mail) Particular |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo |
| TitCar | String(100) | Sim | Título do Cargo |
| PerRef | Date | Sim | Competência do Cálculo |
| DatPag | Date | Sim | Data do Pagamento |
| SalBas | Number(013,4) | Sim | Salário Base |
| ValLiq | Number(013,4) | Sim | Valor líquido |
| BasIns | Number(011,2) | Sim | Base INSS Cálculo |
| BasIrf | Number(011,2) | Sim | Base de Cálculo do IRF |
| BasFgt | Number(011,2) | Sim | Base do FGTS Mensal |
| FgtMes | Number(011,2) | Sim | Valor FGTS do Mês |
| CodFai | Number(003,0) | Sim | Faixa de Desconto do Imposto de Renda |
| DepIrf | Number(002,0) | Sim | Dependentes IRRF |
| DepSaf | Number(002,0) | Sim | Número de Dependentes do Salário Família |
| ModPag | String(001) | Sim | Modo de Pagamento do Salário |
| DMdPag | String(065) | Sim | Descrição Modo Pagto |
| TotVen | Number(011,2) | Sim | Total de vencimentos(+) |
| TotDes | Number(011,2) | Sim | Total de descontos(-) |
| TipCal | Number(002,0) | Sim | Tipo do Cálculo |
| DTpCal | String(030) | Sim | Descrição Tipo de Cálculo |
| DatHor | Number(014,6) | Sim | Data e Hora de geração |
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

### R046HOLIndice2

**Tipo:** Não unico

Campos:
- EstCar
- CodCar

### R046HOLIndice3

**Tipo:** Não unico

Campos:
- PerRef

### R046HOLIndice4

**Tipo:** Não unico

Campos:
- NumEmp
- CodFil

---

## Relacionamentos

### IR_R046HOL_026

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R046HOL_027

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

