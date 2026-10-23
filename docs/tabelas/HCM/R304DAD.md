# R304DAD

## Descrição

e-Sfinge - Dados Funcionais do Agente Público Ativo

---

## Resumo

- Campos: 27
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| NumMat | String(016) | Não | Número da Matrícula do Agente Público na Unidade |
| NumCpf | Number(011,0) | Não | Código de Identificação do Contribuinte na Receita Federal do Agente Público |
| VigSit | Date | Não | Data de Início da Nova Situação de Vínculo ou Mudança de Lotação do Agente |
| SeqReg | Number(009,0) | Não | Sequência |
| TipQua | Number(002,0) | Não | Tipo de Quadro |
| CodCar | String(016) | Sim | Código do Cargo ou Função em que o Servidor Foi Contratado |
| VigCar | Date | Sim | Data de Início da Vigência do Cargo ou Função Conforme Dispositivo Legal |
| DesLot | String(100) | Não | Descrever o Local Onde o Agente Público Desempenha as Funções |
| EspVin | Number(002,0) | Não | Tipo de Vínculo do Agente Público com a Unidade |
| TipMov | Number(002,0) | Não | Tipo de Movimentação do Agente Público com a Unidade |
| JorTra | Number(007,0) | Não | Informar a Jornada Semanal de Trabalho Contratada |
| CodEnt | Number(007,0) | Sim | Código do Ente do Destino/Origem |
| UniGes | Number(002,0) | Sim | Tipo de Unidade Gestora do Destino/Origem |
| TipOnu | Number(002,0) | Sim | Tipo de Ônus |
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
- NumMat
- NumCpf
- VigSit
- SeqReg

---

## Índices

### R304DADIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

### IR_R304DAD_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

