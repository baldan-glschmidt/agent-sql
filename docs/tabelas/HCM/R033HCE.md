# R033HCE

## Descrição

Histórico de Competências da Pessoa - Evidências

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPes | Number(009,0) | Não | Código da Pessoa |
| SeqHis | Number(008,0) | Não | Sequencia para identificar o histórico |
| CodCpt | Number(009,0) | Não | Competência adquirida na data informada |
| RevCpt | String(010) | Não | Revisão da Competência foi adquirida na data informada |
| PrfApl | Number(004,0) | Não | Perfil de aplicação adquirido para esta competência |
| SeqEvd | Number(004,0) | Não | Evidência da aquisição da competência |
| CodTpr | Number(004,0) | Sim | Tabela de proficiências da evidência da competência adquirida |
| CodCPr | String(010) | Sim | Determina qual Conceito foi percebido para a evidência da competência |
| NotEvd | Number(008,4) | Sim | Determina a nota da evidência da Competência |
| PerEvd | Number(007,4) | Sim | Indica o quanto (%) foi evidenciado em relação a nota máxima |

---

## Chave Primária

- CodPes
- SeqHis
- CodCpt
- RevCpt
- PrfApl
- SeqEvd

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R033HCE_001

**Tabela:** R033HCP

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |
| SeqHis | SeqHis |

### IR_R033HCE_005

**Tabela:** R577EVD

| Origem | Destino |
|--------|---------|
| CodCpt | CodCpt |
| RevCpt | RevCpt |
| PrfApl | PrfApl |
| SeqEvd | SeqEvd |

### IR_R033HCE_007

**Tabela:** R577CPR

| Origem | Destino |
|--------|---------|
| CodTpr | CodTpr |
| CodCPr | CodCPr |

