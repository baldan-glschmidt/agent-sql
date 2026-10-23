# R096ECO

## Descrição

Epi por Colaborador

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| CodEpi | Number(008,0) | Não | Código do EPI |
| DiaVal | Number(004,0) | Sim | Dias de validade do Epi |
| DiaRev | Number(004,0) | Sim | Dias de revisão do Epi |
| USU_SubEpi | Number(008,0) | Sim | EPI Substituido |
| USU_QtdEpi | Number(003,0) | Sim | Quantidade EPI |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodEpi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R096ECO_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R096ECO_003

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

