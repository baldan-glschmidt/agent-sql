# R030ATI

## Descrição

Ativação de rotinas com bloqueio

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipAti | Number(003,0) | Não | Tipo de Ativação |
| CodUsu | Number(009,0) | Não | Código do Usuário |
| DatHor | Number(014,6) | Não | Data e Hora que o registro foi incluído/alterado. |
| SenAti | String(030) | Sim | Senha de Ativação |

---

## Chave Primária

- NumEmp
- TipAti

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030ATI_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

