# R064SFO

## Descrição

Programação de Folga - TC

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatIni | Date | Não | Data Inicial |
| IniSub | Date | Não | Início da Substituição |
| EmpSub | Number(004,0) | Sim | Código da Empresa do Substituto |
| TClSub | Number(001,0) | Sim | Tipo de Colaborador Substituto |
| CadSub | Number(009,0) | Sim | Cadastro do Substituto |
| FimSub | Date | Sim | Fim da Substituição |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- IniSub

---

## Índices

### R064SFOIndice2

**Tipo:** Não unico

Campos:
- EmpSub
- TClSub
- CadSub

---

## Relacionamentos

Nenhum relacionamento cadastrado.
