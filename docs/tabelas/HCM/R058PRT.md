# R058PRT

## Descrição

Configuração de Portas de Comunicação

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
| CodDsp | Number(009,0) | Não | Dispositivo gerenciador |
| PrtCom | Number(001,0) | Não | Porta de comunicação |
| ModCom | Number(001,0) | Sim | Modo de comunicação da porta (mode) |
| TXDDly | Number(004,0) | Sim | Delay do driver TXD (TXD delay) |
| RcbDly | Number(004,0) | Sim | Delay de recebimento dos dados (receive delay) |
| PacTim | Number(004,0) | Sim | Timeout de recebimento dos lotes de dados (inter-character timeout) |
| RspTim | Number(004,0) | Sim | Timeout da resposta (controller reply) |
| PolTim | Number(004,0) | Sim | Timeout do recebimento do pacote de eventos (pool timeout) |
| PolOff | Number(004,0) | Sim | Timeout do recebimento do pacote de eventos off-line (off-line device pool timeout) |

---

## Chave Primária

- CodDsp
- PrtCom

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058PRT_000

**Tabela:** R058DSP

| Origem | Destino |
|--------|---------|
| CodDsp | CodDsp |

