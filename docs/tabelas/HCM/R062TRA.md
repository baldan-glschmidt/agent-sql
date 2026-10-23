# R062TRA

## Descrição

Alarmes Tratados

---

## Resumo

- Campos: 25
- Chave Primária: 3 campo(s)
- Índices: 2
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatCol | Date | Não | Data da Coleta do Alarme |
| HorCol | Number(005,0) | Não | Hora da Coleta do Alarme |
| SeqCol | Number(009,0) | Não | Sequência da Coleta do Alarme |
| DatAlm | Date | Sim | Data do Alarme |
| HorAlm | Number(005,0) | Sim | Hora do Alarme |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor Onde Foi Gerado o Alarme |
| CodSin | Number(003,0) | Sim | Código do Sinal de Alarme |
| TipAlm | Number(002,0) | Sim | Tipo do Alarme |
| DatRec | Date | Sim | Data do Reconhecimento do Alarme |
| HorRec | Number(005,0) | Sim | Hora do Reconhecimento do Alarme |
| UsuRec | Number(010,0) | Sim | Código do Usuário que Reconheceu o Alarme |
| DatTra | Date | Sim | Data do Tratamento do Alarme |
| HorTra | Number(005,0) | Sim | Hora do Tratamento do Alarme |
| UsuTra | Number(010,0) | Sim | Código do Usuário que Tratou o Alarme |
| DesTra | String(255) | Sim | Descrição do Tratamento Efetuado pelo Usuário |
| EndEnt | Number(003,0) | Sim | Endereço da Entrada no Relógio |
| DesRec | String(255) | Sim | Descrição do Reconhecimento Efetuado pelo Usuário |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| NumEIP | String(015) | Sim | Número do Endereço IP do Dispositivo |
| TipDsp | Number(001,0) | Sim | Tipo do Dispositivo |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| LocLei | Number(002,0) | Sim | Localização Leitora |
| CodEve | String(003) | Sim | Código do Evento de Alarme (Honeywell) |
| ObsAlm | String(255) | Sim | Observação |

---

## Chave Primária

- DatCol
- HorCol
- SeqCol

---

## Índices

### R062TRAIndice2

**Tipo:** Não unico

Campos:
- DatTra
- HorTra

### R062TRAINDICE3

**Tipo:** Não unico

Campos:
- CodRlg
- CodSin
- DatAlm
- HorAlm

---

## Relacionamentos

### IR_R062TRA_005

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R062TRA_006

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

### IR_R062TRA_007

**Tabela:** R062SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

