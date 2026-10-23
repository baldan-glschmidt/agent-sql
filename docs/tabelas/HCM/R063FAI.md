# R063FAI

## Descrição

Faixas Horárias da Ronda de Vigilantes

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRon | Number(003,0) | Não | Código da Ronda |
| DiaSem | Number(001,0) | Não | Dia da Semana |
| SeqFai | Number(002,0) | Não | Sequência da Faixa da Ronda |
| IniFai | Number(005,0) | Sim | Início da Faixa p/ Marcação da Ronda |
| FimFai | Number(005,0) | Sim | Fim da Faixa p/ Marcação da Ronda |

---

## Chave Primária

- CodRon
- DiaSem
- SeqFai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R063FAI_000

**Tabela:** R063RON

| Origem | Destino |
|--------|---------|
| CodRon | CodRon |

