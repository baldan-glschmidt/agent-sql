# R791EXP

## Descrição

Central alertas - Contrato Experiência - Vencimento Próximo

---

## Resumo

- Campos: 7
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
| DatVen | Date | Não | Data de vencimento calculada do contrato de experiência |
| DiaVen | Number(003,0) | Não | Dias para vencer na data do Cálculo |
| InsLev | Number(001,0) | Não | Nível de severidade da ocorrência |
| DatGer | Date | Não | Data de geração do registro |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

### R791EXPIndice1

**Tipo:** Não unico

Campos:
- InsLev

---

## Relacionamentos

Nenhum relacionamento cadastrado.
