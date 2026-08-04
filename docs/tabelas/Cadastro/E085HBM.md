# E085HBM

## Descrição

Cadastros - Clientes - Histórico de Bens de Cliente

---

## Resumo

- Campos: 16
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do cliente |
| SeqHbm | Number(009,0) | Não | Sequência do Histórico do Bem |
| DesHbm | String(100) | Sim | Descrição do Bem |
| DatHbm | Date | Sim | Data de aquisição do bem |
| VlrHbm | Number(015,2) | Sim | Valor do Bem |
| IndFin | String(001) | Não | Identifica se o bem está financiado |
| SldFin | Number(015,2) | Sim | Saldo devedor do financiamento do bem |
| VlrSld | Number(015,2) | Sim | Valor da parcela que compõe o saldo devedor |
| NumPar | Number(004,0) | Sim | Número de parcelas restantes que compõe o saldo devedor do bem |
| DesFin | String(100) | Sim | Financeira responsável pela alienação do bem |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodCli
- SeqHbm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E085HBM_000

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

