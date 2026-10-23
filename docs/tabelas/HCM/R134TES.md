# R134TES

## Descrição

Turmas - Testes

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| CodTst | String(005) | Não | Código do Teste |
| QtdPer | Number(003,0) | Sim | Quantidade de Perguntas do Teste |

---

## Chave Primária

- CodCua
- TmaCua
- CodTst

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134TES_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134TES_002

**Tabela:** R136TES

| Origem | Destino |
|--------|---------|
| CodTst | CodTst |

