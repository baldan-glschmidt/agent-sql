# R303AGE

## Descrição

e-Sfinge - Agente Público Ativo/Inativo e Pensionista

---

## Resumo

- Campos: 17
- Chave Primária: 6 campo(s)
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
| NumMat | String(016) | Não | Número da Matrícula na Unidade |
| NomPes | String(100) | Não | Nome Completo da Pessoa |
| DatNas | Date | Não | Data de Nascimento |
| NomMae | String(100) | Não | Nome Completo da Mãe |
| NomPai | String(100) | Sim | Nome Completo do Pai |
| NumCpf | Number(011,0) | Não | Código de Identificação do Contribuinte na Receita Federal |
| NumIde | String(016) | Sim | Número da Carteira de Identidade |
| NumTit | String(016) | Sim | Número do Título Eleitoral |
| NumRes | String(016) | Sim | Número do Certificado de Reservista ou da Dispensa de Incorporação |
| NumPis | Number(011,0) | Sim | Número do PIS ou PASEP |
| CodSex | Number(002,0) | Não | Código do Sexo |
| OriReg | String(001) | Sim | Origem do Registro (G-Gerado, D-Digitado, I-Importado) |

---

## Chave Primária

- NumEmp
- AnoBas
- BimAno
- TipCol
- NumCad
- NumMat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R303AGE_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

