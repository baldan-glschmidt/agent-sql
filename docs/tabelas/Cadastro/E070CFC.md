# E070CFC

## Descrição

Cadastros - Filiais - Classificações Filiais para Análise de Crédito

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodCfc | String(003) | Não | Código da classificação da filial para a análise de crédito |
| DesCfc | String(100) | Sim | Descrição da classificação da filial para a análise de crédito |
| IndCfc | Number(007,2) | Sim | Índice de cobrança da classificação de filial para análise de crédito |
| LimApr | Number(011,2) | Não | Valor limite de aprovação de pedidos para a classificação da filial |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodCfc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
