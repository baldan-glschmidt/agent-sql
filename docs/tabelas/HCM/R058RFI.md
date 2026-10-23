# R058RFI

## Descrição

Formato de Cartões RFID

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdtFmt | Number(002,0) | Não | Identificador do Formato do Cartão RFID |
| DesFmt | String(050) | Sim | Descrição do Formato do Cartão |
| QtdBit | Number(002,0) | Sim | Quantidade de Bits do Cartão (number of bits on card) |
| OfSBit | Number(002,0) | Sim | Deslocamento de Bits (card offset) |
| QtdPar | Number(002,0) | Sim | Quantidade de Bits de Paridade Par (even parity) |
| QtdImp | Number(002,0) | Sim | Quantidade de Bits de Paridade Ímpar (odd parity) |
| CodAce | Number(009,0) | Sim | Código de Acesso (facility code) |
| QtdBCA | Number(002,0) | Sim | Quantidade de Bits do Código de Acesso (number bits facility code) |
| BitICA | Number(002,0) | Sim | Bit de Início do Código de Acesso (index of facility code begin) |
| QtdBNC | Number(002,0) | Sim | Quantidade de Bits do Número do Cartão (number of bits in card number) |
| BitINC | Number(002,0) | Sim | Bit de Início do Número do Cartão (index of card number begin) |

---

## Chave Primária

- IdtFmt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
