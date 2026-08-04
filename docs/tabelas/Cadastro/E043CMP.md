# E043CMP

## Descrição

Tabelas - Modelos de Planos - Controle Processo Validade Modelo de Plano

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipPla | Number(001,0) | Não | Tipo do modelo de plano |
| OpcPro | Number(001,0) | Sim | Opção de Processo |
| CodMpc | Number(004,0) | Não | Código do modelo de plano |
| CodMpa | Number(004,0) | Não | Código do modelo de plano atual |
| DatFim | Date | Não | Data da Validade do Modelo |
| IndRat | String(001) | Sim | Indicador Manter Rateios das Contas |
| IndRel | String(001) | Sim | Indicador Manter Relacionamentos |
| UltPro | Number(004,0) | Sim | Indicador do último processo realizado |
| AbgEmp | String(250) | Sim | Abrangência de empresas |

---

## Chave Primária

- CodMpc
- CodMpa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E043CMP_002

**Tabela:** E043MPC

| Origem | Destino |
|--------|---------|
| CodMpc | CodMpc |

