# R123EXA

## Descrição

Requisições - Exames - Temporária

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
| CodExa | Number(004,0) | Não | Código Exame Médico |
| AbrPar | String(050) | Sim | Abrangência do Parecer Exame Médico |
| IndVal | String(001) | Sim | Define se o requisito deve ser considerado na triagem/seletiva |
| PtsExa | Number(002,0) | Sim | Pontuação do Exame |

---

## Chave Primária

- CodRqu
- CodExa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R123EXA_001

**Tabela:** R108EXA

| Origem | Destino |
|--------|---------|
| CodExa | CodExa |

