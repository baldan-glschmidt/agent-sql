# R014AVP

## Descrição

Cadastro de Informações sobre o Aviso Prévio

---

## Resumo

- Campos: 17
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| DatAlt | Date | Não | Data da Alteração do Aviso Prévio |
| ForAvi | Number(001,0) | Sim | Cálculo Médias Aviso Prévio |
| DiaAvi | Number(003,0) | Sim | Dias Aviso Indenizado |
| DiaRea | Number(003,0) | Sim | Dias Aviso Reavido |
| AcrAvi | Number(002,0) | Sim | Acréscimo de dias indenizado por ano |
| AcrRea | Number(002,0) | Sim | Acréscimo de dias reavido por ano |
| IniCon | Number(001,0) | Sim | Início da contagem do acréscimo |
| ForCon | Number(001,0) | Sim | Forma de contagem do acréscimo |
| ProAvi | Number(001,0) | Sim | Dias de Aviso na contagem |
| SomRea | String(001) | Sim | Somar Dias Aviso Reavido ao Direito das Indenizações |
| AviDif | Number(001,0) | Sim | Uso do aviso diferenciado |
| SelIda | String(001) | Sim | Seleção por Idade |
| SelSer | String(001) | Sim | Seleção por Tempo Serviço |
| StaHis | Number(001,0) | Sim | Status do Histórico |
| DesAfa | Number(001,0) | Sim | Forma de desconsiderar dias de afastamento |
| ProAcr | Number(001,0) | Sim | Dias de acréscimo na contagem |

---

## Chave Primária

- CodSin
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
