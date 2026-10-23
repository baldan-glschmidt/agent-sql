# R134EDT

## Descrição

Turmas - Exceção Definição

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| CodHcu | Number(006,0) | Não | Código Horário Curso |
| DatExc | Date | Não | Data da Exceção |
| HorIni | Number(005,0) | Não | Hora Início da Exceção |
| HorTer | Number(005,0) | Sim | Hora Término da Exceção |

---

## Chave Primária

- CodCua
- TmaCua
- CodHcu
- DatExc
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134EDT_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R134EDT_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

