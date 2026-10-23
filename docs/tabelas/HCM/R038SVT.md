# R038SVT

## Descrição

Saldo Vale Transporte

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAlt | Date | Não | Data do Saldo |
| CodLin | Number(005,0) | Não | Código da Linha |
| ValSal | Number(011,2) | Sim | Saldo do Vale Transporte |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt
- CodLin

---

## Índices

### R038SVTIndice1

**Tipo:** Não unico

Campos:
- CodLin

---

## Relacionamentos

Nenhum relacionamento cadastrado.
