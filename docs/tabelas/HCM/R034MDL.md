# R034MDL

## Descrição

Indicação para os Módulos

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| CodMod | Number(002,0) | Não | Código do módulo |
| IndCon | String(001) | Sim | Considera o tipo de colaborador no módulo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodMod

---

## Índices

### R034MDLIndice2

**Tipo:** Não unico

Campos:
- IndCon

---

## Relacionamentos

Nenhum relacionamento cadastrado.
