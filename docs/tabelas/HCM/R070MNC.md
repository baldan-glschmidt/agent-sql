# R070MNC

## Descrição

Marcações não consideradas

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumNSR | Number(009,0) | Não | Número NSR |
| NumPis | Number(011,0) | Não | Número do PIS/PASEP |
| NumCPF | Number(011,0) | Não | Número do CPF |
| DatAcc | Date | Não | Data do Acesso |
| HorAcc | Number(005,0) | Não | Hora do Acesso |
| SeqMar | Number(002,0) | Não | Sequência do Registro |
| MotNCo | Number(001,0) | Sim | Motivo Marcação Não Considerada |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do Coletor no Acesso |
| FusMar | Number(002,0) | Sim | Fuso Horário |
| StrMar | String(250) | Sim | Valor Criptografado |

---

## Chave Primária

- NumNSR
- NumPis
- NumCPF
- DatAcc
- HorAcc
- SeqMar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
