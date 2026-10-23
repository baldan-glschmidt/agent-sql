# R017RER

## Descrição

Reestruturação dos Postos de trabalho - Postos - Comandos Rollback

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRee | Number(004,0) | Não | Código da reestruturação dos Postos de trabalho |
| SeqReg | Number(009,0) | Não | Sequencia do posto |
| SeqCom | Number(009,0) | Não | Sequencia comando |
| ComRol | String(8001) | Sim | Comando rollback |
| CamRes | String(700) | Sim | Campo reserva |

---

## Chave Primária

- CodRee
- SeqReg
- SeqCom

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017RER_001

**Tabela:** R017REP

| Origem | Destino |
|--------|---------|
| CodRee | CodRee |
| SeqReg | SeqReg |

