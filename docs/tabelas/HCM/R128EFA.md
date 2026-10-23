# R128EFA

## Descrição

Custos Reembolso Específico - Faixa Salarial

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRee | Number(004,0) | Não | Código do reembolso específico |
| CmpCus | Date | Não | Competência do Item de Custo |
| AbrSub | String(030) | Não | Subsídios |
| VlrAte | Number(011,2) | Não | Faixa de Valor Até |
| PerCus | Number(005,2) | Sim | Percentual Custo |

---

## Chave Primária

- CodRee
- CmpCus
- AbrSub
- VlrAte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128EFA_000

**Tabela:** R128RES

| Origem | Destino |
|--------|---------|
| CodRee | CodRee |

### IR_R128EFA_002

**Tabela:** R128ESU

| Origem | Destino |
|--------|---------|
| CodRee | CodRee |
| CmpCus | CmpCus |
| AbrSub | AbrSub |

