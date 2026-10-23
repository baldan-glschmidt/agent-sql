# R070IAA

## Descrição

Informações adicionais do acesso

---

## Resumo

- Campos: 12
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatAcc | Date | Não | Data do acesso |
| HorAcc | Number(005,0) | Não | Hora do acesso |
| SeqAcc | Number(002,0) | Não | Sequência do registro |
| NumCra | Number(012,0) | Não | Número do crachá |
| IdtPes | String(023) | Sim | Identificador da pessoa |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodRlg | Number(005,0) | Sim | Código do coletor de acesso |
| CodDsp | Number(009,0) | Sim | Código do dispositivo |
| Mascar | String(001) | Sim | Pessoa estava usando máscara |
| Temper | Number(004,2) | Sim | Temperatura da pessoa |
| TemAnm | String(001) | Sim | Pessoa estava com temperatura anormal |
| TipAcc | Number(002,0) | Sim | Código do tipo de acesso |

---

## Chave Primária

- NumCra
- DatAcc
- HorAcc
- SeqAcc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
