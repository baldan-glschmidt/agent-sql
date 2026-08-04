# E085CCA

## Descrição

Cadastros - Clientes - Categorias Clientes para Análise de Crédito

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCca | String(003) | Não | Código da categoria do cliente para a análise de crédito |
| DesCca | String(100) | Sim | Descrição da categoria do cliente para a análise de crédito |
| LimIni | Number(013,4) | Não | Valor limite inicial da faixa da categoria do cliente para a análise de crédito |
| LimFin | Number(013,4) | Não | Valor limite final da faixa da categoria do cliente para a análise de crédito |
| FatSal | Number(015,6) | Sim | Fator salário da faixa da categoria do cliente para a análise de crédito |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodCca

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
