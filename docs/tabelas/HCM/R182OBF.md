# R182OBF

## Descrição

PLR - Objetivos - Faixas

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodObj | Number(004,0) | Não | Código do Objetivo |
| FaiObj | Number(002,0) | Não | Faixa do Objetivo |
| DesOfa | String(030) | Sim | Descrição da Faixa |
| VinOfa | Number(011,2) | Sim | Início da Faixa |
| VfiOfa | Number(011,2) | Sim | Fim da Faixa |
| QtdPto | Number(011,2) | Sim | Quantidade de Pontos da Faixa |

---

## Chave Primária

- CodObj
- FaiObj

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R182OBF_000

**Tabela:** R182OBJ

| Origem | Destino |
|--------|---------|
| CodObj | CodObj |

