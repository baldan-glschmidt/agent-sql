# R134EIP

## Descrição

Turmas - Exceção Instrutores (Pessoas)

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| CodPes | Number(009,0) | Não | Código da Pessoa |
| CodHcu | Number(006,0) | Não | Código Horário Curso |
| DatExc | Date | Não | Data da Exceção |
| HorIni | Number(005,0) | Não | Hora Início da Exceção |
| HorTer | Number(005,0) | Sim | Hora Término da Exceção |

---

## Chave Primária

- CodCua
- TmaCua
- CodPes
- CodHcu
- DatExc
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134EIP_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134EIP_002

**Tabela:** R134INP

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |
| CodPes | CodPes |

