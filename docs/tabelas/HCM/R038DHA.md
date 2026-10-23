# R038DHA

## Descrição

Documentos do Historico Anotação

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| DatNot | Date | Não | Data Anotação Registro |
| SeqNot | Number(002,0) | Não | Sequência |
| SeqDoc | Number(002,0) | Não | Sequência do Documento |
| DocCol | Image | Sim | Documento do Colaborador |
| NomArq | String(251) | Sim | Nome Arquivo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatNot
- SeqNot
- SeqDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038DHA_004

**Tabela:** R038NOT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatNot | DatNot |
| SeqNot | SeqNot |

