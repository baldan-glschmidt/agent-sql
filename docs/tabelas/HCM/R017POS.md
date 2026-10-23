# R017POS

## Descrição

Postos de Trabalho

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Código do Posto de Trabalho |
| DesRed | String(070) | Sim | Descrição reduzida do Posto de Trabalho |
| DesPos | String(150) | Sim | Descrição do Posto de Trabalho |
| DatCri | Date | Sim | Data de Criação do Posto de Trabalho |
| DatExt | Date | Sim | Data de Extinção do Posto de Trabalho |
| PerPos | Number(002,0) | Sim | Código do perfil do posto de trabalho |
| ObsPos | String(2000) | Sim | Observação do posto de trabalho |
| CodUsu | Number(009,0) | Sim | Usuário que realizou a última alteração no Posto de trabalho |
| DthAlt | Number(014,6) | Sim | Data/Hora da última alteração do Posto de trabalho |
| USU_EmaEnv | String(001) | Sim | E-mail Enviado |

---

## Chave Primária

- EstPos
- PosTra

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017POS_000

**Tabela:** R017EST

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |

### IR_R017POS_006

**Tabela:** R017PER

| Origem | Destino |
|--------|---------|
| PerPos | PerPos |

