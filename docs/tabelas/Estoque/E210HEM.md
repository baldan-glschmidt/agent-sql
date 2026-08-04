# E210HEM

## Descrição

Estoques - Histórico de Evolução do Estoque Mínimo Automatizado

---

## Resumo

- Campos: 18
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Sim | Código da derivação do produto |
| CodDep | String(010) | Não | Código do depósito |
| MedVen | Number(019,6) | Sim | Média das vendas |
| QtdEmi | Number(014,5) | Sim | Quantidade do estoque mínimo atual inicial |
| QtdEmf | Number(014,5) | Sim | Quantidade do estoque mínimo atual final |
| QtdVen | Number(014,5) | Sim | Quantidade vendida do produto |
| QtdDev | Number(014,5) | Sim | Quantidade devolvida do produto |
| QtdCan | Number(014,5) | Sim | Quantidade cancelada do produto |
| QtdCre | Number(014,5) | Sim | Quantidade permitida para crescimento do estoque mínimo automatizado |
| QtdRed | Number(014,5) | Sim | Quantidade permitida de redução do estoque mínimo automatizado |
| PerAum | Number(005,2) | Sim | Percentual de aumento do estoque mínimo automatizado |
| PerRed | Number(005,2) | Sim | Percentual de redução do estoque mínimo automatizado |
| DatAtu | Date | Sim | Data da última alteração do registro |
| HorAtu | Number(005,0) | Sim | Hora da última alteração do registro |
| ObsAem | String(250) | Sim | Observação da análise do estoque mínimo automatizado |

---

## Chave Primária

- IdeUni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
