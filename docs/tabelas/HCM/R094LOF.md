# R094LOF

## Descrição

Localizador - Fones

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Localizado |
| FonPro | String(020) | Não | Fone Procura |
| DscLoc | String(025) | Sim | Descrição do Local para Fone |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- FonPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R094LOF_002

**Tabela:** R094LOC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

