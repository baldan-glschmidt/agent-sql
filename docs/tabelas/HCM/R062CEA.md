# R062CEA

## Descrição

Coleta de Eventos de Alarme

---

## Resumo

- Campos: 17
- Chave Primária: 0 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEip | String(015) | Sim | Número do endereço IP do dispositivo |
| NumARL | String(002) | Sim | Número do ARL |
| CodTer | String(002) | Sim | Número do Terminal |
| SitEnt | String(030) | Sim | Situação Entradas |
| EstEnt | String(030) | Sim | Estado Entradas |
| DatAlm | Date | Sim | Data do Alarme |
| HorAlm | Number(005,0) | Sim | Hora do Alarme |
| CodSin | Number(003,0) | Sim | Código do Sinal de Alarme |
| TipAlm | Number(002,0) | Sim | Tipo do Alarme |
| EndEnt | Number(003,0) | Sim | Endereço da Entrada no Relógio |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |
| TipDsp | Number(001,0) | Sim | Tipo do Dispositivo |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| LocLei | Number(002,0) | Sim | Localização Leitora |
| CodEve | String(003) | Sim | Código do Evento de Alarme (Honeywell) |
| AlmTmp | String(001) | Sim | Define se o Alarme é Temporário |
| ObsAlm | String(255) | Sim | Observação |

---

## Chave Primária

Não possui.

---

## Índices

### R062CEAIndice1

**Tipo:** Não unico

Campos:
- CodDsp
- CodSin
- EndEnt
- TipAlm
- NumCra
- DatAlm
- HorAlm

---

## Relacionamentos

Nenhum relacionamento cadastrado.
