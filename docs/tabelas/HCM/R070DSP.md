# R070DSP

## Descrição

Pendências para Dispositivos

---

## Resumo

- Campos: 18
- Chave Primária: 1 campo(s)
- Índices: 7
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPen | Number(009,0) | Não | Código da Pendência |
| DatEnv | Date | Sim | Data do Envio da Atualização |
| HorEnv | Number(005,0) | Sim | Hora do Envio da Atualização |
| SeqEnv | Number(002,0) | Sim | Sequência de envio |
| NumFis | Number(012,0) | Sim | Número Físico do Crachá (Número Serial) |
| CodCmd | Number(003,0) | Não | Código do Comando |
| DirSvr | String(253) | Sim | Endereço da Central de Gerenciamento |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| ValStr | String(2047) | Sim | Valor atualização |
| RetPen | String(003) | Sim | Retorno da pendência |
| QtdTen | Number(002,0) | Sim | Qtde de Tentativas de Envio do Comando |
| CicAtu | Number(002,0) | Sim | Ciclo Atual para Tentativa de Envio de Comando |
| StaCmd | Number(001,0) | Sim | Status do Comando |
| DatCSM | Date | Sim | Data de Atualização do dado na CSM |
| HorCSM | Number(005,0) | Sim | Hora de Atualização do dado na CSM |
| SeqCSM | Number(002,0) | Sim | Sequência de Atualização do dado na CSM |
| MsgRet | String(2046) | Sim | Mensagem de Retorno da Pendência |
| LogPen | String(2047) | Sim | Log da pendência gerada |

---

## Chave Primária

- CodPen

---

## Índices

### R070DSPIndice2

**Tipo:** Não unico

Campos:
- DatEnv
- HorEnv

### R070DSPIndice4

**Tipo:** Não unico

Campos:
- NumFis

### R070DSPIndice5

**Tipo:** Não unico

Campos:
- StaCmd

### R070DSPIndice6

**Tipo:** Não unico

Campos:
- NumFis
- StaCmd
- CodCmd
- DirSvr

### R070DSPIndice7

**Tipo:** Não unico

Campos:
- StaCmd
- DatEnv
- HorEnv
- NumFis

### R070DSPIndice8

**Tipo:** Não unico

Campos:
- CodPen
- StaCmd

### R070DSPIndice9

**Tipo:** Não unico

Campos:
- StaCmd
- CodPen

---

## Relacionamentos

Nenhum relacionamento cadastrado.
