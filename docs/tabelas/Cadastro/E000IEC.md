# E000IEC

## Descrição

Tabelas - Integrações - Controle de Início e Término das Exportações

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodInt | Number(002,0) | Não | Código da integração |
| IdeInt | String(015) | Não | Código identificador do tipo de informação |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| TipExp | Number(002,0) | Não | Tipo de Exportação |
| DatIni | Date | Sim | Data de início do processo |
| HorIni | Number(005,0) | Sim | Hora de início do processo |
| DatFim | Date | Sim | Data de finalização do processo |
| HorFim | Number(005,0) | Sim | Hora de finalização do processo |
| SitIec | String(001) | Sim | Situação do processo de integração completa |

---

## Chave Primária

- CodInt
- IdeInt
- CodEmp
- CodFil
- TipExp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
