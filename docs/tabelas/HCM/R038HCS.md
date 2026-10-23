# R038HCS

## Descrição

Histórico Categoria SEFIP

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAlt | Date | Não | Data da Alteração da Categoria SEFIP |
| CatSef | Number(002,0) | Sim | Categoria Sefip |
| StaHis | Number(001,0) | Sim | Status do Histórico |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

### R038HCSIndice2

**Tipo:** Não unico

Campos:
- DatAlt
- NumEmp
- TipCol
- NumCad

---

## Relacionamentos

Nenhum relacionamento cadastrado.
