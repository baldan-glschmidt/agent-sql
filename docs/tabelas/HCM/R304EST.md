# R304EST

## Descrição

e-Sfinge Online - Ingresso Estatutário

---

## Resumo

- Campos: 44
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| NumAto | String(016) | Não | Número do Ato que Admitiu ou Nomeou o Servidor |
| NumMat | String(016) | Não | Número da Matrícula do Servidor na Unidade |
| SeqReg | Number(009,0) | Não | Sequência |
| VigAto | Date | Não | Data em que o Ato de Admissão Passa a Viger |
| PubAto | Date | Não | Data de Publicação do Ato |
| TipQua | Number(002,0) | Não | Tipo de Quadro |
| CarFun | String(016) | Não | Código do cargo em que o servidor foi nomeado |
| VigCar | Date | Não | Data de Início da Vigência do Cargo |
| DesLot | String(100) | Sim | Local Onde Desempenhará as Funções do Cargo |
| NumEdi | String(016) | Sim | Número do Edital de Concurso Público em que o Servidor se Habilitou para o Cargo |
| NumIns | String(016) | Sim | Número de Inscrição do Servidor no Concurso |
| DatPos | Date | Não | Data em que o Servidor Tomou Posse |
| DatExe | Date | Não | Data em que o servidor entrou em exercício no cargo |
| TipAto | Number(002,0) | Não | Tipo de Ato |
| DatAto | Date | Não | Data do Ato de Admissão ou Nomeação |
| DscHab | String(100) | Sim | Descrição da habilitação do servidor admitido ou nomeado |
| TipEsc | Number(002,0) | Não | Escolaridade |
| DatLau | Date | Não | Data do Laudo de Saúde |
| IndApt | String(001) | Não | Indica se o Funcionário Está Apto para o Exercício do Cargo com Relação à Saúde |
| IndAcu | String(001) | Não | Indica se o Funcionário Admitido ou Nomeado Acumula Cargo |
| NomCar | String(100) | Sim | Descrição do Cargo Acumulado |
| CodEsf | Number(002,0) | Sim | Código da Esfera Governamental do Cargo Acumulado |
| TipCHr | Number(002,0) | Sim | Tipo da carga horária |
| QtdCHr | Number(007,0) | Sim | Quantidade numérica conforme a carga horária descrita |
| IndEle | String(001) | Não | Indica se o Funcionário Está Em Dia Com Suas Obrigações Eleitorais |
| DatBen | Date | Não | Data da Declaração de Bens Apresentada Pelo Funcionário Admitido ou Nomeado |
| IndPen | String(001) | Não | Indicativo de Penalidade disciplinar no exercício de função pública |
| NumDec | String(026) | Sim | Número da Decisão Judicial |
| DatDec | Date | Sim | Data da Decisão Judicial |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo |
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
- NumAto
- NumMat
- SeqReg

---

## Índices

### R304ESTIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

### IR_R304EST_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

