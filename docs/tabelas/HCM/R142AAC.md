# R142AAC

## Descrição

Acompanhamento Treinamento

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDia | Number(009,0) | Não | Código do Diagnóstico |
| SitDia | String(001) | Sim | Situação do Acompanhamento |
| NumEmp | Number(004,0) | Sim | Código da Empresa do Responsável |
| TipCol | Number(001,0) | Sim | Tipo de Colaborador Responsável |
| NumCad | Number(009,0) | Sim | Cadastro do Responsável |

---

## Chave Primária

- CodDia

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R142AAC_000

**Tabela:** R142DIA

| Origem | Destino |
|--------|---------|
| CodDia | CodDia |

