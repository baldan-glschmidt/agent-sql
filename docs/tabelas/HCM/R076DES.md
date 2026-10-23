# R076DES

## Descrição

Definição Estrutura Tabela Salarial

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEst | Number(004,0) | Não | Código da Estrutura |
| NomEst | String(030) | Sim | Nome da Estrutura |
| TabEst | Number(004,0) | Sim | Define a qual estrutura pertence a Tabela salarial |
| TipFor | String(001) | Sim | Tipo do Formato (ML) |
| TipSis | Number(002,0) | Sim | Tipo do Sistema |
| InfSal | Number(001,0) | Sim | Tipo da Informação |
| HorMes | Number(010,0) | Sim | Horas no Mês |
| NivMer | Number(002,0) | Sim | Nível de Mercado |
| AssSal | String(001) | Sim | Origem do salário na inclusão |
| ConEst | String(001) | Sim | Consiste Estrutura/Classe e Nível Salarial de acordo com Cargo |
| TpoFor | Number(001,0) | Sim | Tipo de Formação da Estrutura Salarial |
| ConSal | String(001) | Sim | Consiste Salário de acordo com Estrutura/Classe/Nível |

---

## Chave Primária

- CodEst

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
