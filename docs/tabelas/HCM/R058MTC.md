# R058MTC

## Descrição

Módulo Controlador

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| CodSeq | Number(003,0) | Sim | Código da Sequência |
| DesMct | String(050) | Sim | Descrição do Módulo Controlador |
| CmpRef | String(020) | Sim | Campo |
| EndCom | Number(003,0) | Sim | Endereço de Comunicação |
| PorCom | Number(001,0) | Sim | Porta de Comunicação |
| IDPlaca | Number(003,0) | Sim | Identificador da Placa |

---

## Chave Primária

- CodDsp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058MTC_000

**Tabela:** R058DSP

| Origem | Destino |
|--------|---------|
| CodDsp | CodDsp |

