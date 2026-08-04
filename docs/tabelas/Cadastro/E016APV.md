# E016APV

## Descrição

Tabelas - Aplicações de vendas

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
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodApv | String(005) | Não | Código da Aplicação |
| NomApv | String(050) | Sim | Nome da aplicação de venda |
| DesApv | String(100) | Não | Descrição da aplicação de venda |
| SitApv | String(001) | Não | Situação da aplicação de venda |

---

## Chave Primária

- CodEmp
- CodApv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E016APV_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

