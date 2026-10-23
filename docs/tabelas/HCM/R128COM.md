# R128COM

## Descrição

Cursos Aperfeiçoamento - Composição do módulo

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do curso que é o Módulo |
| CodCur | Number(009,0) | Não | Código do Curso que faz parte do módulo |

---

## Chave Primária

- CodCua
- CodCur

---

## Índices

### R128COMIndice2

**Tipo:** Não unico

Campos:
- CodCur

---

## Relacionamentos

### IR_R128COM_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R128COM_001

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCur | CodCua |

