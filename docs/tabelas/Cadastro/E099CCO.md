# E099CCO

## Descrição

Cadastros - Usuários - Cotas de Compra por Competência

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodUsu | Number(010,0) | Não | Código do usuário |
| CcoCpr | Date | Não | Mês e ano da competência para controle de cotas de compra |
| CodAgc | String(005) | Não | Código do agrupamento de produtos para comercial |
| VlrCco | Number(015,2) | Sim | Cota de compra estabelecida para a competência |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodUsu
- CcoCpr
- CodAgc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E099CCO_001

**Tabela:** E099USU

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodUsu | CodUsu |

