# R123ITA

## Descrição

Requisições - Itens Avaliação - Temporária

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRqu | Number(009,0) | Não | Código Requisição |
| CodIta | Number(006,0) | Não | Código Item Avaliação |
| AbrRes | String(050) | Sim | Resposta Item Avaliação |
| IndVal | String(001) | Sim | Define se o requisito deve ser considerado na triagem/seletiva |
| PtsIta | Number(002,0) | Sim | Pontuação do Item de Avaliação |

---

## Chave Primária

- CodRqu
- CodIta

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R123ITA_001

**Tabela:** R116ITA

| Origem | Destino |
|--------|---------|
| CodIta | CodIta |

