# R126CPE

## Descrição

Aceitos Preenchimento

---

## Resumo

- Campos: 14
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRqu | Number(009,0) | Não | Código Requisição |
| SeqCan | Number(005,0) | Não | Sequência dos Candidatos Aprovados p/ Admissão |
| EmpRqu | Number(004,0) | Sim | Código de Empresa da Requisição |
| TipCan | Number(001,0) | Sim | Tipo do Candidato |
| NumCan | Number(007,0) | Sim | Cadastro Candidatos |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo do Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro Colaborador |
| DatAdm | Date | Sim | Data Admissão |
| CanEfe | String(001) | Sim | Indica se o candidato foi efetivado no Rubi |
| EmpEfe | Number(004,0) | Sim | Empresa em que o candidato foi efetivado |
| TipEfe | Number(001,0) | Sim | Tipo de colaborador em que o candidato foi efetivado |
| CadEfe | Number(009,0) | Sim | Cadastro em que o candidato foi efetivado |
| PreAdm | String(036) | Sim | Contém o identificador único da pré-admissão no módulo G7 Onboarding |

---

## Chave Primária

- CodRqu
- SeqCan

---

## Índices

### R126CPEIndice2

**Tipo:** Não unico

Campos:
- CodRqu

---

## Relacionamentos

### IR_R126CPE_000

**Tabela:** R126RQU

| Origem | Destino |
|--------|---------|
| CodRqu | CodRqu |

### IR_R126CPE_002

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| EmpRqu | NumEmp |

