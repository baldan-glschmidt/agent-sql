# R070ONL

## Descrição

Comandos do Acesso

---

## Resumo

- Campos: 20
- Chave Primária: 7 campo(s)
- Índices: 5
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCmd | Number(003,0) | Não | Código do Comando |
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor |
| DatChe | Date | Não | Data de Chegada do Comando |
| HorChe | Number(005,0) | Não | Hora de Chegada do Comando |
| SeqChe | Number(002,0) | Não | Sequência da Chegada |
| StaExe | Number(001,0) | Sim | Status do Comando |
| PriCmd | Number(002,0) | Sim | Prioridade de Execução do Comando |
| DatExe | Date | Sim | Data da Execução do Comando |
| HorExe | Number(005,0) | Sim | Hora da Execução do Comando |
| RetExe | String(2046) | Sim | Retorno da Execução do Comando |
| CodUsu | Number(010,0) | Sim | Código do Usuário do Processamento |
| ParCmd | String(255) | Sim | Parâmetro do Comando |
| TipCmd | Number(001,0) | Sim | Tipo de Comando |
| OriCmd | Number(001,0) | Sim | Origem do Comando |
| PreCmd | Number(003,0) | Sim | Código do Comando Predecessor |
| IdtReg | String(014) | Sim | Identificador do Registro de Atualização do Smart |
| VerRon | String(015) | Sim | Versão do Ronda Acesso em que o registro R070ONL foi inserido |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| CodAdm | Number(009,0) | Não | Código da Atualização |

---

## Chave Primária

- CodAdm
- CodCmd
- CodPlt
- CodRlg
- DatChe
- HorChe
- SeqChe

---

## Índices

### R070ONLIndice2

**Tipo:** Não unico

Campos:
- DatExe
- HorExe

### R070ONLIndice3

**Tipo:** Não unico

Campos:
- CodPlt
- CodRlg

### R070ONLIndice4

**Tipo:** Não unico

Campos:
- CodCmd
- CodPlt
- CodRlg
- IdtReg

### R070ONLIndice5

**Tipo:** Não unico

Campos:
- StaExe

### R070ONLIndice6

**Tipo:** Não unico

Campos:
- CodPlt
- CodRlg
- StaExe

---

## Relacionamentos

Nenhum relacionamento cadastrado.
