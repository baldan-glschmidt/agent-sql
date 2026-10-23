# R791ATC

## Descrição

Central alertas - Afastamentos - Recorrência e Atestados

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| TotDias | Number(003,0) | Não | Total de dias de atestados somados no período |
| InsLev | Number(001,0) | Não | Nível de severidade da ocorrência |
| DatGer | Date | Não | Data de geração do registro |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

### R791ATCIndice1

**Tipo:** Não unico

Campos:
- InsLev

---

## Relacionamentos

Nenhum relacionamento cadastrado.
