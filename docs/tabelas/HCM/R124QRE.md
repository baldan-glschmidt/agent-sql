# R124QRE

## Descrição

Colaborador - Respostas do Questionário

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Entrevistado |
| NumCad | Number(009,0) | Não | Cadastro do Entrevistado |
| CodQue | Number(002,0) | Não | Código do Questionário |
| DatQue | Date | Não | Data da Resposta do Questionário |
| TipEnt | Number(001,0) | Sim | Tipo Entrevistador |
| CadEnt | Number(009,0) | Sim | Cadastro do Entrevistador |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodQue
- DatQue

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124QRE_003

**Tabela:** R117QUE

| Origem | Destino |
|--------|---------|
| CodQue | CodQue |

