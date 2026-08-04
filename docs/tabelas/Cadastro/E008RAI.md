# E008RAI

## Descrição

Tabelas - Cidades para RAIS - SIG

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRai | Number(007,0) | Não | Código da cidade utilizada para RAIS |
| NomCid | String(060) | Não | Nome da cidade |
| SigUfs | String(002) | Não | Sigla do estado da cidade |
| PopCid | Number(009,0) | Sim | População da cidade |
| PotAlf | Number(005,3) | Sim | Percentual do potencial de consumo da cidade |
| LocGeo | String(006) | Sim | Código de localização geográfica |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| NumFeb | Number(005,0) | Sim | Código do município para o Febraban |
| CodAnp | Number(007,0) | Sim | Código do município para a ANP |
| ImgLgt | String(250) | Sim | Logotipo da cidade para guia de recolhimento do ISS |
| IncIss | String(001) | Sim | Incidência do ISSQN |

---

## Chave Primária

- CodRai

---

## Índices

### E008RAIIndice1

**Tipo:** Não unico

Campos:
- SigUfs

---

## Relacionamentos

### IR_E008RAI_002

**Tabela:** E007UFS

| Origem | Destino |
|--------|---------|
| SigUfs | SigUfs |

