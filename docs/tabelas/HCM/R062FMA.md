# R062FMA

## Descrição

Faixas Horárias de Mascaramento de Alarmes

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor |
| EndEnt | Number(003,0) | Não | Endereço da Entrada no Coletor |
| TipAcc | Number(003,0) | Não | Tipo do Acesso |
| DiaSem | Number(001,0) | Não | Dia da Semana |
| SeqFai | Number(002,0) | Não | Sequência da Faixa de Marcação |
| IniFai | Number(005,0) | Sim | Início da Faixa p/ Mascaramento do Alarme |
| FimFai | Number(005,0) | Sim | Fim da Faixa p/ Mascaramento do Alarme |
| TipMas | Number(001,0) | Sim | Entrada Digital 1 |
| TemMas | Number(003,0) | Sim | Tempo mascaramento |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |

---

## Chave Primária

- CodPlt
- CodRlg
- EndEnt
- TipAcc
- DiaSem
- SeqFai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R062FMA_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R062FMA_001

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

