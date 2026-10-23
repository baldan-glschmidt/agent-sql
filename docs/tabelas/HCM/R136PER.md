# R136PER

## Descrição

Testes Turma - Perguntas

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTst | String(005) | Não | Código do Teste |
| CodPer | String(003) | Não | Código da Pergunta |
| DesPer | String(500) | Sim | Descrição da Pergunta |
| PesPer | Number(002,0) | Sim | Peso da Pergunta |
| NotPer | Number(006,2) | Sim | Nota da Pergunta |
| TemRes | Number(003,0) | Sim | Tempo (minutos) para Responder a Pergunta |
| TipPer | String(001) | Sim | Tipo da Pergunta |

---

## Chave Primária

- CodTst
- CodPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R136PER_000

**Tabela:** R136TES

| Origem | Destino |
|--------|---------|
| CodTst | CodTst |

