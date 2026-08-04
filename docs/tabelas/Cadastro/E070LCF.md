# E070LCF

## Descrição

Cadastros - Filiais - Ligação de Classificação Filiais X Fases

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodCfc | String(003) | Não | Código da classificação da filial para a análise de crédito |
| CodFcf | Number(004,0) | Não | Código da fase de classificação para crédito da filial |
| SitLcf | String(001) | Sim | Indicativo da situação do registro |
| IndIni | Number(005,2) | Sim | Índice inicial da fase para a classificação da filial para análise de crédito |
| IndFin | Number(005,2) | Sim | Índice final da fase para a classificação da filial para análise de crédito |
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
- CodFcf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
