# E009RAF

## Descrição

Tabelas - Parâmetros - Recuperação de ICMS sobre acréscimo financeiro

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
| SigUfs | String(002) | Não | Sigla do estado |
| QtdPar | Number(003,0) | Não | Quantidade de parcelas da venda |
| PRZINI | Number(003,0) | Não | Prazo inicial de financiamento em dias |
| PRZFIM | Number(003,0) | Não | Prazo final de financiamento em dias |
| PERACR | Number(005,2) | Não | Percentual de acréscimo financeiro total |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- SigUfs
- QtdPar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
