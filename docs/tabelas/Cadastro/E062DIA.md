# E062DIA

## Descrição

Tabelas - Dias de saída para a Rota de Entrega

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRoe | String(003) | Não | Código da Rota ou Localidade |
| SeqDia | Number(001,0) | Não | Sequência |
| DiaSem | Number(001,0) | Não | Dia da Semana que o caminhão sai para essa Rota |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |

---

## Chave Primária

- CodRoe
- SeqDia

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E062DIA_000

**Tabela:** E062ROE

| Origem | Destino |
|--------|---------|
| CodRoe | CodRoe |

