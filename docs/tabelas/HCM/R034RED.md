# R034RED

## Descrição

Registro de Documentos

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| TipDoc | Number(004,0) | Não | Código do Tipo de Documento |
| DatRef | Date | Não | Data de Referência |
| DatGer | Date | Sim | Data de Geração |
| DatRet | Date | Sim | Data de Entrega |
| NumDoc | String(025) | Sim | Número do Documento |
| Status | String(001) | Sim | Status Documento |
| CodMot | Number(004,0) | Sim | Código do Motivo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TipDoc
- DatRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
