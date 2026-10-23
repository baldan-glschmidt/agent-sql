# R304AGE

## Descrição

e-Sfinge Online - Identificação de Agente Público Ativo/Inativo e Pensionista

---

## Resumo

- Campos: 26
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| NumMat | String(016) | Não | Número da Matrícula na Unidade |
| SeqReg | Number(009,0) | Não | Sequência |
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
| CodNac | Number(002,0) | Não | Nacionalidade |
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
- SeqReg

---

## Índices

### R304AGEIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

### IR_R304AGE_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

