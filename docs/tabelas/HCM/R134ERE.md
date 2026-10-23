# R134ERE

## Descrição

Turmas - Exceção Recursos Instrucionais

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
| CodRei | Number(004,0) | Não | Código do Recurso Instrucional |
| CodHcu | Number(006,0) | Não | Código Horário Curso |
| DatExc | Date | Não | Data da Exceção |
| HorIni | Number(005,0) | Não | Hora Início da Exceção |
| HorTer | Number(005,0) | Sim | Hora Término da Exceção |

---

## Chave Primária

- CodCua
- TmaCua
- CodRei
- CodHcu
- DatExc
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134ERE_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134ERE_002

**Tabela:** R134REI

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |
| CodRei | CodRei |

