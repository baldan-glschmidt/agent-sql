# R303ADM

## Descrição

e-Sfinge - Admissão por Nomeação

---

## Resumo

- Campos: 32
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| AnoBas | Number(004,0) | Não | Ano |
| BimAno | Number(001,0) | Não | Código Bimestre Ano |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| NumAto | String(016) | Não | Número do Ato que Admitiu ou Nomeou o Servidor |
| VigAto | Date | Não | Data em que o Ato de Admissão Passa a Viger |
| PubAto | Date | Não | Data de Publicação do Ato |
| NumMat | String(016) | Não | Número da Matrícula do Servidor na Unidade |
| TipQua | Number(002,0) | Não | Tipo de Quadro |
| CodCar | String(016) | Não | Código do Cargo em que o Servidor Foi Admitido ou Nomeado |
| VigCar | Date | Não | Data de Início da Vigência do Cargo |
| DesLot | String(100) | Sim | Local Onde Desempenhará as Funções do Cargo |
| NumEdi | String(016) | Sim | Número do Edital de Concurso Público em que o Servidor se Habilitou para o Cargo |
| InsApr | Number(016,0) | Sim | Número de Inscrição do Servidor no Concurso |
| DatPos | Date | Não | Data em que o Servidor Tomou Posse |
| DatPro | Date | Sim | Data em que o Servidor Solicitou a Prorrogação da Posse |
| ValVen | Number(014,2) | Sim | Valor do Vencimento do Servidor |
| TipAto | Number(002,0) | Não | Tipo de Ato |
| DatAto | Date | Não | Data do Ato de Admissão ou Nomeação |
| DesEsc | String(100) | Sim | Descrição da habilitação ou da escolaridade do funcionário admitido ou nomeado |
| DatLau | Date | Sim | Data do Laudo de Saúde |
| IndApt | String(001) | Não | Indica se o Funcionário Está Apto para o Exercício do Cargo com Relação à Saúde |
| IndAcu | String(001) | Não | Indica se o Funcionário Admitido ou Nomeado Acumula Cargo |
| NomCar | String(100) | Sim | Descrição do Cargo Acumulado |
| CodEsf | Number(002,0) | Sim | Código da Esfera Governamental do Cargo Acumulado |
| DesCar | String(020) | Sim | Carga Horária do Cargo Acumulado |
| QtdCar | Number(007,0) | Sim | Quantidade Numérica Conforme a Carga Horária Descrita para o Cargo Acumulado |
| IndEle | String(001) | Não | Indica se o Funcionário Está Em Dia Com Suas Obrigações Eleitorais |
| DatDec | Date | Não | Data da Declaração de Bens Apresentada Pelo Funcionário Admitido ou Nomeado |
| IndPar | String(001) | Sim | Controle Interno Especifica o Parecer da Admissão de Servidores Efetivos |
| OriReg | String(001) | Sim | Origem do Registro (G-Gerado, D-Digitado, I-Importado) |

---

## Chave Primária

- NumEmp
- AnoBas
- BimAno
- TipCol
- NumCad
- NumAto
- NumMat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R303ADM_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

