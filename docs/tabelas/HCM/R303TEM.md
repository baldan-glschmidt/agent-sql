# R303TEM

## Descrição

e-Sfinge - Contratação Temporária

---

## Resumo

- Campos: 34
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
| NumAto | String(016) | Não | Número do Ato que Contratou o Servidor |
| VigAto | Date | Não | Data em que o Ato de Contratação Passa a Viger |
| DatFim | Date | Sim | Data em que Encerrará o Contrato (Contratos temporários) |
| PubAto | Date | Não | Data de Publicação do Ato |
| FunLeg | String(255) | Sim | Fundamento Legal da Contratação |
| NumMat | String(016) | Não | Número da Matrícula do Servidor na Unidade |
| TipQua | Number(002,0) | Não | Tipo de Quadro |
| CodCar | String(016) | Não | Código do Cargo ou Emprego que o Servidor Foi Contratado |
| VigCar | Date | Não | Data de Início da Vigência do Cargo ou Emprego |
| DesLot | String(100) | Sim | Descrição da Lotação do Servidor |
| NumCtp | String(016) | Sim | Número da Carteira de Trabalho e Previdência Social |
| SerCtp | String(006) | Sim | Número de Série da Carteira de Trabalho e Previdência Social |
| NumEdi | String(016) | Sim | Número do Edital de Seleção em que o Servidor se Habilitou para o Cargo |
| InsApr | Number(016,0) | Sim | Número de Inscrição do Servidor no Concurso |
| ValVen | Number(014,2) | Sim | Valor do Vencimento do Servidor |
| TipAto | Number(002,0) | Não | Tipo de Ato |
| DatAto | Date | Não | Data do Ato de Contratação |
| DesEsc | String(100) | Não | Descrição da Habilitação ou da Escolaridade do Funcionário Contratado |
| DatLau | Date | Sim | Data do Laudo de Saúde |
| IndApt | String(001) | Não | Indica se o Funcionário Está Apto para o Exercício do Cargo com Relação à Saúde |
| IndAcu | String(001) | Não | Indica se o Funcionário Contratado Acumula Cargo |
| NomCar | String(100) | Sim | Descrição do Cargo Acumulado |
| CodEsf | Number(002,0) | Sim | Código da Esfera Governamental do Cargo Acumulado |
| DesCar | String(020) | Sim | Carga Horária do Cargo Acumulado |
| QtdCar | Number(007,0) | Sim | Quantidade Numérica Conforme a Carga Horária Descrita para o Cargo Acumulado |
| IndEle | String(001) | Não | Indica se o Funcionário Está Em Dia Com Suas Obrigações Eleitorais |
| DatDec | Date | Sim | Data da Declaração de Bens Apresentada Pelo Funcionário Contratado |
| IndPar | String(001) | Sim | Controle Interno Especifica o Parecer da Contratação Temporária |
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

### IR_R303TEM_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

