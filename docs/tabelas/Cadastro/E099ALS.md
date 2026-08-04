# E099ALS

## Descrição

Cadastros - Usuários - Agrupamentos Liberados para Compras

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodUsu | Number(010,0) | Não | Código do Usuário |
| CodAgc | String(005) | Não | Código de agrupamento de produtos para comercial |
| DatIni | Date | Sim | Data início da validade do agrupamento para o usuário |
| DatFim | Date | Sim | Data final da validade do agrupamento para o usuário |

---

## Chave Primária

- CodEmp
- CodUsu
- CodAgc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E099ALS_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E099ALS_001

**Tabela:** E099USU

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodUsu | CodUsu |

