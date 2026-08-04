# E019TIM

## Descrição

Cadastros - Tabela de partilha ICMS Monofásico

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTim | String(003) | Não | Código Tabela de partilha ICMS Monofásico |
| DatIni | Date | Não | Data de início da vigência |
| TipCbt | Number(002,0) | Não | Tipo de Combustível |
| UfsOri | String(002) | Sim | Código da UF origem |
| UfsDes | String(002) | Sim | Código da UF Destino |
| CliCon | String(001) | Não | Indicativo se o cliente é contribuinte de ICMS |
| PerOri | Number(005,2) | Sim | Percentual de partilha de ICMS para o estado de origem |
| PerDes | Number(005,2) | Sim | Percentual de partilha de ICMS para o estado de destino |

---

## Chave Primária

- CodTim

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
