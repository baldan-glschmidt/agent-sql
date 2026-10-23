# R011SIT

## Descrição

Situações do Banco de Horas

---

## Resumo

- Campos: 8
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBHr | Number(005,0) | Não | Código do Banco de Horas |
| CodSit | Number(003,0) | Não | Situação Base para Banco de Horas |
| DatIni | Date | Não | Data Inicial do Período |
| DatFim | Date | Sim | Data Final do Período |
| SinSit | String(001) | Sim | Sinal da Situação |
| OrdCom | Number(002,0) | Sim | Ordem de Compensação das Situações na Mesma Data |
| CnvBan | Number(006,3) | Sim | Conversão para Banco de Horas (%) |
| CnvEve | Number(006,3) | Sim | Conversão para Geração de Eventos (%) |

---

## Chave Primária

- CodBHr
- CodSit
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R011SIT_000

**Tabela:** R011BHR

| Origem | Destino |
|--------|---------|
| CodBHr | CodBHr |

### IR_R011SIT_001

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

