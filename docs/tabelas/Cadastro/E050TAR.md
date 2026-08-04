# E050TAR

## Descrição

Cadastros - Tributos - Tarifas bancárias

---

## Resumo

- Campos: 21
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodTar | String(030) | Não | Código da tarifa |
| DesTar | String(100) | Não | Descrição da tarifa |
| VigTar | Date | Não | Data de início de vigência |
| TipSer | Number(002,0) | Sim | Tipo de serviço prestado |
| PreVar | Number(010,0) | Sim | Código da tarifa conforme município |
| RatInt | Number(003,0) | Sim | Código de rateio do resultado interno |
| SerImp | String(010) | Sim | Tipo de Serviço no contexto fiscal baseado na LC 116/2003 |
| CodFim | String(020) | Sim | Código fiscal municipal |
| CtaRed | Number(007,0) | Não | Número reduzido da conta contábil |
| IdeDcm | Number(009,0) | Sim | Identificador de registro |
| CodPri | String(001) | Sim | Período de apuração |
| PerTar | Number(011,6) | Sim | Percentual da tarifa |
| VlrUni | Number(015,2) | Sim | Valor unitário da tarifa |
| VlrMin | Number(015,2) | Sim | Valor mínimo da tarifa |
| VlrMax | Number(015,2) | Sim | Valor máximo da tarifa |
| IdeCtd | Number(009,0) | Não | Ide da tributação da Desif |
| ExpDes | String(001) | Sim | Exportar Descrição do Serviço da DESIF |
| PerIss | Number(015,2) | Sim | Percentual do ISSQN |

---

## Chave Primária

- IdeUni

---

## Índices

### E050TAR_FKIndex1

**Tipo:** Não unico

Campos:
- IdeCtd

### E050TARIndice2

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodTar
- VigTar

---

## Relacionamentos

Nenhum relacionamento cadastrado.
