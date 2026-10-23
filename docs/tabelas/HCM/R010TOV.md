# R010TOV

## Descrição

Tipos de Outros Valores

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodOut | Number(004,0) | Não | Código do Outro Valor |
| DesOut | String(100) | Sim | Descrição do Outro Valor |
| TipRub | Number(001,0) | Sim | Tipo do Valor |
| NatRub | Number(004,0) | Sim | Código de classificação da rubrica de acordo com a natureza |
| IniVal | Date | Sim | Data de início da validade das informações prestadas no evento |
| FimVal | Date | Sim | Data final da validade das informações |

---

## Chave Primária

- NumEmp
- CodOut

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
