# R128ESU

## Descrição

Custos Reembolso Específico - Subsídios

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRee | Number(004,0) | Não | Código do reembolso específico |
| CmpCus | Date | Não | Competência do Item de Custo |
| AbrSub | String(030) | Não | Subsídios |
| TipSub | String(001) | Sim | Tipo de Subsídio |
| QtdSub | Number(011,2) | Sim | Subsídio do Item de Custo |
| TipTet | String(001) | Sim | Tipo do Teto |
| QtdTet | Number(011,2) | Sim | Teto p/comprometimento |
| IndSal | String(001) | Sim | Indicar Aplicação % do Salário |
| PerSal | Number(005,2) | Sim | Percentual Salário |

---

## Chave Primária

- CodRee
- CmpCus
- AbrSub

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128ESU_000

**Tabela:** R128RES

| Origem | Destino |
|--------|---------|
| CodRee | CodRee |

### IR_R128ESU_001

**Tabela:** R128ECU

| Origem | Destino |
|--------|---------|
| CodRee | CodRee |
| CmpCus | CmpCus |

