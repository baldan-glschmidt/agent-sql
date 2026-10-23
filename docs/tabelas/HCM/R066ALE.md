# R066ALE

## Descrição

Gestão de Incidentes - Alertas do colaborador

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
| DatApu | Date | Não | Data da Apuração |
| CodTAl | Number(002,0) | Não | Código do Tipo de Alerta para Acerto (Incidente) |
| PerRef | Date | Sim | Competência do Cálculo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatApu
- CodTAl

---

## Índices

### R066ALEIndice1

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- PerRef

---

## Relacionamentos

Nenhum relacionamento cadastrado.
