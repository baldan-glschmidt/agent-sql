# R134IMG

## Descrição

Calendário Cursos Treinamento - Imagens

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| DatCua | Date | Não | Data do Curso |
| SeqCua | Number(002,0) | Não | Sequência do Curso p/ Mesma Data |
| SeqImg | Number(003,0) | Não | Sequência de imagem |
| Imagem | Image | Sim | Imagem |
| DesImg | String(030) | Sim | Descrição da Imagem |

---

## Chave Primária

- CodCua
- DatCua
- SeqCua
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134IMG_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R134IMG_002

**Tabela:** R134DCL

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| DatCua | DatCua |
| SeqCua | SeqCua |

