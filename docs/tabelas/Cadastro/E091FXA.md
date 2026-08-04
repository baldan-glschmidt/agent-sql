# E091FXA

## Descrição

Tabelas - Plano Financeiro - Relacionamento Contas X Assuntos

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CtaFin | Number(007,0) | Não | Conta Financeira |
| RatAss | Number(004,0) | Não | Código do Assunto utilizado para rateios |
| CodRat | Number(004,0) | Não | Código do Rateio Padrão |
| SitFxa | String(001) | Não | Situação do relacionamento |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CtaFin
- RatAss

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E091FXA_001

**Tabela:** E091PLF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CtaFin | CtaFin |

