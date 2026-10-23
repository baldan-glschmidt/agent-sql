# R070ADM

## Descrição

Atualizações DataMart

---

## Resumo

- Campos: 20
- Chave Primária: 1 campo(s)
- Índices: 8
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAdm | Number(009,0) | Não | Código da Atualização |
| DatEnv | Date | Sim | Data do Envio da Atualização |
| HorEnv | Number(005,0) | Sim | Hora do Envio da Atualização |
| SeqEnv | Number(002,0) | Sim | Sequência de envio |
| IdtPes | String(023) | Sim | Identificador da Pessoa |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| NumFis | Number(012,0) | Sim | Número Físico do Crachá (Número Serial) |
| CodCmd | Number(003,0) | Sim | Código do Comando |
| ValStr | String(2047) | Sim | Valor atualização |
| DirSvr | String(253) | Sim | Endereço da Central de Gerenciamento |
| RetPen | String(003) | Sim | Retorno da pendência |
| QtdTen | Number(002,0) | Sim | Qtde de Tentativas de Envio do Comando |
| CicAtu | Number(002,0) | Sim | Ciclo Atual para Tentativa de Envio de Comando |
| StaCmd | Number(001,0) | Sim | Status do Comando |
| DatCSM | Date | Sim | Data de Atualização do dado na CSM |
| HorCSM | Number(005,0) | Sim | Hora de Atualização do dado na CSM |
| SeqCSM | Number(002,0) | Sim | Sequência de Atualização do dado na CSM |
| VerRon | String(015) | Sim | Versão do Ronda Acesso em que foi inserido o registro R070ADM |
| MsgRet | String(2046) | Sim | Mensagem de Retorno da Pendência |
| LogPen | String(2047) | Sim | Log da pendência gerada |

---

## Chave Primária

- CodAdm

---

## Índices

### R070ADMIndice2

**Tipo:** Não unico

Campos:
- DatEnv
- HorEnv

### R070ADMIndice3

**Tipo:** Não unico

Campos:
- IdtPes

### R070ADMIndice4

**Tipo:** Não unico

Campos:
- NumFis

### R070ADMIndice5

**Tipo:** Não unico

Campos:
- StaCmd

### R070ADMIndice6

**Tipo:** Não unico

Campos:
- IdtPes
- NumFis
- NumCra
- StaCmd
- CodCmd
- DirSvr

### R070ADMIndice7

**Tipo:** Não unico

Campos:
- StaCmd
- DatEnv
- HorEnv
- NumFis
- IdtPes

### R070ADMIndice8

**Tipo:** Não unico

Campos:
- CodAdm
- StaCmd

### R070ADMIndice9

**Tipo:** Não unico

Campos:
- StaCmd
- CodAdm

---

## Relacionamentos

Nenhum relacionamento cadastrado.
