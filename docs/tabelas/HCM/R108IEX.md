# R108IEX

## Descrição

Exames - Itens Resultado

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodExa | Number(004,0) | Não | Código do Exame |
| SeqIex | Number(003,0) | Não |  |
| DesIte | String(030) | Sim | Descrição do Ítem |
| ResPad | String(020) | Sim | Resultado Padrão |
| LimMin | Number(014,5) | Sim | Limite Mínimo Referencial da Quantificação |
| LimMax | Number(014,5) | Sim | Limite Máximo Referencial da Quantificação |
| IndOre | String(001) | Sim | Identificação da Orelha |
| IndExa | String(001) | Sim | Tipo de Exame (A-Aérea/O-Óssea) |
| ValFre | Number(010,5) | Sim | Valor da Frequência |

---

## Chave Primária

- CodExa
- SeqIex

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R108IEX_000

**Tabela:** R108EXA

| Origem | Destino |
|--------|---------|
| CodExa | CodExa |

