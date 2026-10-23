# R124HET

## Descrição

Colaborador - Etapas

---

## Resumo

- Campos: 16
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Candidato |
| CodRqu | Number(009,0) | Não | Código Requisição |
| CodEta | Number(003,0) | Não | Código Etapa |
| SeqEta | Number(003,0) | Não | Sequência Etapa |
| DatEta | Date | Sim | Data da Etapa |
| NotCan | Number(006,2) | Sim | Nota do candidato |
| CodPar | Number(003,0) | Sim | Código do parecer |
| SitEta | Number(001,0) | Sim | Situação da Etapa |
| ComEtp | String(7000) | Sim | Comentário Etapa |
| EmpAva | Number(004,0) | Sim | Empresa do avaliador |
| TclAva | Number(001,0) | Sim | Tipo do Colaborador Avaliador |
| CadAva | Number(009,0) | Sim | Cadastro do Avaliador |
| CodUsu | Number(009,0) | Sim | Usuário responsável pela última modificação da etapa do Candidato |
| DthEma | Number(014,6) | Sim | Data/Hora da última modificação da etapa do Candidato |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodRqu
- CodEta
- SeqEta

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124HET_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R124HET_003

**Tabela:** R126RQU

| Origem | Destino |
|--------|---------|
| CodRqu | CodRqu |

### IR_R124HET_004

**Tabela:** R114ETA

| Origem | Destino |
|--------|---------|
| CodEta | CodEta |

