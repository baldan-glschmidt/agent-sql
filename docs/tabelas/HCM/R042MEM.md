# R042MEM

## Descrição

HomologNet - Movimento do Empregado

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| MotMov | String(003) | Não | Motivo Movimento |
| DatMov | Date | Não | Data Movimento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- MotMov
- DatMov

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R042MEM_002

**Tabela:** R042COL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

