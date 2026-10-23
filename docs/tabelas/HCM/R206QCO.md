# R206QCO

## Descrição

PLR Paquetá - Quesitos Atingidos p/ Colaborador

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CmpRef | Date | Não | Competência de Referência |
| CodQst | Number(004,0) | Não | Código do Quesito |
| QstAtg | String(001) | Sim | Indicador de Quesito Atingido (S,N) |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpRef
- CodQst

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R206QCO_004

**Tabela:** R206QST

| Origem | Destino |
|--------|---------|
| CodQst | CodQst |

