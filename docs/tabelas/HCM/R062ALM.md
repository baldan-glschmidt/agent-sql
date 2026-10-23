# R062ALM

## Descrição

Alarmes a Serem Tratados

---

## Resumo

- Campos: 24
- Chave Primária: 3 campo(s)
- Índices: 4
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
| StaAlm | Number(001,0) | Sim | Status do Alarme |
| DatRec | Date | Sim | Data do Reconhecimento do Alarme |
| HorRec | Number(005,0) | Sim | Hora do Reconhecimento do Alarme |
| UsuRec | Number(010,0) | Sim | Código do Usuário que Reconheceu o Alarme |
| DesRec | String(255) | Sim | Descrição do Reconhecimento Efetuado pelo Usuário |
| TipRal | Number(001,0) | Sim | Tipo de Reconhecimento Realizado |
| EndEnt | Number(003,0) | Sim | Endereço da Entrada no Relógio |
| ObsAlm | String(255) | Sim | Observação |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| NumEIP | String(015) | Sim | Número do Endereço IP do Dispositivo |
| TipDsp | Number(001,0) | Sim | Tipo do Dispositivo |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| LocLei | Number(002,0) | Sim | Localização Leitora |
| DspRel | Number(009,0) | Sim | Dispositivo relacionado |
| CodEve | String(003) | Sim | Código do Evento de Alarme (Honeywell) |

---

## Chave Primária

- DatCol
- HorCol
- SeqCol

---

## Índices

### R062ALMIndice2

**Tipo:** Não unico

Campos:
- CodPlt
- CodRlg
- CodSin

### R062ALMIndice3

**Tipo:** Não unico

Campos:
- CodSin
- TipAlm
- DatAlm
- HorAlm

### R062ALMIndice4

**Tipo:** Não unico

Campos:
- CodDsp
- CodRlg
- CodSin
- CodPlt
- DatAlm

### R062ALMIndice5

**Tipo:** Não unico

Campos:
- DatAlm
- CodDsp
- CodRlg
- CodSin
- CodPlt

---

## Relacionamentos

### IR_R062ALM_005

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R062ALM_006

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

### IR_R062ALM_007

**Tabela:** R062SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

