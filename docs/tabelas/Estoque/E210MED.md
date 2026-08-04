# E210MED

## Descrição

Estoques - Preço médio por filial

---

## Resumo

- Campos: 14
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do produto |
| PreMed | Number(021,10) | Sim | Preço médio |
| DatMed | Date | Sim | Data base da última atualização do preço médio |
| UsuMed | Number(010,0) | Sim | Usuário responsável pela última atualização do preço médio |
| HorMed | Number(005,0) | Sim | Hora da última atualização do preço médio |
| PreCus | Number(021,10) | Sim | Preço de custo |
| CusIcm | Number(015,6) | Sim | Preço de custo dos produtos com valor de ICMS |
| DatCus | Date | Sim | Data base do preço de custo |
| PrmIcm | Number(015,6) | Sim | Preço Médio do valor total de ICMS |
| DatIcm | Date | Sim | Data base da última atualização do preço médio de icms |
| PrmRci | Number(021,10) | Sim | Preço médio para Transferência de Crédito de ICMS |

---

## Chave Primária

- CodEmp
- CodFil
- CodPro
- CodDer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
