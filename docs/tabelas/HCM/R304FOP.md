# R304FOP

## Descrição

e-Sfinge - Folha de Pagamento - Dados Provento/Desconto Servidor

---

## Resumo

- Campos: 24
- Chave Primária: 10 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| NumCpf | Number(011,0) | Não | Código de identificação do contribuinte na Receita Federal |
| NumMat | String(016) | Não | Número da matrícula na Unidade |
| AnoMes | Date | Não | Mês e Ano da Folha de Pagamento |
| SeqFop | Number(002,0) | Não | Número Sequencial da Folha de Pagamento |
| CodCom | String(008) | Não | Código do Componente da Folha de Pagamento Conforme Tabela Componentes da Folha Pagamento |
| IndVer | String(001) | Não | Indicativo de verba paga ou descontada do servidor - Provento ou Desconto (P,D) |
| SeqReg | Number(009,0) | Não | Sequência Registro Dados Provento/Desconto Servidor |
| ValCom | Number(014,2) | Não | Valor lançado (pago ou descontado) para o componente na folha de pagamento |
| CodCal | Number(005,0) | Sim | Código de Cálculo correspondente no sistema |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Sim | Código do Evento |
| PidSta | String(030) | Sim | Pid Status |
| CmpAu1 | Date | Sim | Campo Auxiliar 1 |
| CmpAu2 | Date | Sim | Campo Auxiliar 2 |
| CmpAu3 | Number(008,0) | Sim | Campo Auxiliar 3 |
| CmpAu4 | Number(008,0) | Sim | Campo Auxiliar 4 |
| CmpAu5 | Number(008,0) | Sim | Campo Auxiliar 5 |
| CmpAu6 | Number(008,0) | Sim | Campo Auxiliar 6 |
| CmpAu7 | String(002) | Sim | Campo Auxiliar 7 |
| CmpAu8 | String(002) | Sim | Campo Auxiliar 8 |
| CmpAu9 | String(2000) | Sim | Campo Auxiliar 9 |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- NumCpf
- NumMat
- AnoMes
- SeqFop
- CodCom
- IndVer
- SeqReg

---

## Índices

### R304FOPIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

### IR_R304FOP_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

