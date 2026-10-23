# R303DAD

## Descrição

e-Sfinge - Dados Funcionais do Agente Público Ativo

---

## Resumo

- Campos: 17
- Chave Primária: 8 campo(s)
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
| NumMat | String(016) | Não | Número da Matrícula do Agente Público na Unidade |
| NumCpf | Number(011,0) | Não | Código de Identificação do Contribuinte na Receita Federal do Agente Público |
| VigSit | Date | Não | Data de Início da Nova Situação de Vínculo ou Mudança de Lotação do Agente |
| TipQua | Number(002,0) | Sim | Tipo de Quadro |
| CodCar | String(016) | Sim | Código do Cargo ou Função em que o Servidor Foi Contratado |
| VigCar | Date | Sim | Data de Início da Vigência do Cargo ou Função Conforme Dispositivo Legal |
| DesLot | String(100) | Não | Descrever o Local Onde o Agente Público Desempenha as Funções |
| EspVin | Number(002,0) | Não | Especificação do Vínculo do Agente Público com a Unidade |
| JorTra | Number(002,0) | Não | Informar a Jornada Semanal de Trabalho Contratada |
| CodEnt | Number(007,0) | Sim | Código do Ente do Destino/Origem |
| UniGes | Number(002,0) | Sim | Tipo de Unidade Gestora do Destino/Origem |
| OriReg | String(001) | Sim | Origem do Registro (G-Gerado, D-Digitado, I-Importado) |

---

## Chave Primária

- NumEmp
- AnoBas
- BimAno
- TipCol
- NumCad
- NumMat
- NumCpf
- VigSit

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R303DAD_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

