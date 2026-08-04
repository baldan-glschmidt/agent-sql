# E085DEP

## Descrição

Cadastros - Clientes - Dependentes

---

## Resumo

- Campos: 15
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do Cliente |
| CodDpd | Number(009,0) | Não | Código do dependente |
| NomDep | String(100) | Não | Nome do dependente |
| CpfDep | Number(011,0) | Sim | CPF do Dependente |
| DocIde | String(030) | Sim | Documento de identidade do dependente |
| DatNas | Date | Sim | Data de Nascimento do Dependente |
| EstCiv | Number(001,0) | Sim | Estado Civil do Dependente |
| GraPar | Number(001,0) | Sim | Grau de parentesco do dependente |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| IndPrd | String(001) | Sim | Identifica se o dependente é produtor rural |

---

## Chave Primária

- CodCli
- CodDpd

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
