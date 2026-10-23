# R126HSE

## Descrição

Selecionados Triagem - Colaborador

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| MotEli | Number(002,0) | Não | Motivo da Eliminação |
| SitCan | Number(002,0) | Sim | Situação do Candidato |
| OriSel | Number(001,0) | Sim | Origem Seleção |
| CodJus | Number(003,0) | Sim | Código da justificativa para eliminação/desistência candidato |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- MotEli

---

## Índices

### R126HSEIndice2

**Tipo:** Não unico

Campos:
- MotEli

---

## Relacionamentos

Nenhum relacionamento cadastrado.
