# R034MAT

## Descrição

Matrícula do Colaborador

---

## Resumo

- Campos: 15
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatGer | Date | Sim | Data de Geração |
| MatEso | String(030) | Sim | Matrícula eSocial |
| Layout | String(006) | Sim | Leiaute eSocial |
| AdmFec | String(001) | Sim | Indica se foi efetuado o fechamento da admissão do colaborador |
| RecEso | String(001) | Sim | Indica se o leiaute inicial do colaborador foi recebido pelo eSocial |
| CodUsu | Number(009,0) | Sim | Código do Usuário para o Colaborador |
| DatFec | Date | Sim | Data do fechamento da admissão |
| DatSST | Date | Sim | Data do fechamento do SST |
| LayOri | String(006) | Sim | Leiaute de Origem eSocial |
| TraDes | Number(001,0) | Sim | Transferência Descentralizada |
| DatTre | Date | Sim | Data de envio dos Treinamentos |
| StaMig | Number(001,0) | Sim | Informe o status atual da migração do eSocial |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
